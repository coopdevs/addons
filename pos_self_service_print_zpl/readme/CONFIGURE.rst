Printer
~~~~~~~

Add printer to the OS.

Browse to the CUPS configuration page to get the name of the printer that will be used: http://localhost:631/printers. Set this name as the printer name in the POS self-service configuration page.

Center the barcode by trial and error using the label offset and size configuration values of the POS self-service configuration page.

Configure printer to accept several jobs in a row::

    lpadmin -p <PRINTERNAME> -o usb-no-reattach-default=true

And restart CUPS to apply the new configuration::

    sudo service cups restart


Reverse proxy with nginx
~~~~~~~~~~~~~~~~~~~~~~~~

Install nginx::

    apt install nginx

Start nginx::

    sudo systemctl start nginx.service

Copy this file in::

    /etc/nginx/sites-available/cups

.. code-block::

    upstream cups-reverse-proxy {
        server 127.0.0.1:631 weight=1 fail_timeout=60s;
    }

    server {
        # server port and name
        listen 8631;
        listen [::]:8631;
        server_name _;

        # ssl log files
        access_log /var/log/nginx/cups-access.log;
        error_log /var/log/nginx/cups-error.log;


        # increase proxy buffer to handle some Odoo web requests
        proxy_buffers 16 64k;
        proxy_buffer_size 128k;

        location / {
            proxy_pass http://cups-reverse-proxy;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Host $server_name;

            add_header 'Access-Control-Allow-Origin' $http_origin always;
            add_header 'Access-Control-Allow-Credentials' * always;
            add_header 'Access-Control-Allow-Methods' * always;
            add_header 'Access-Control-Allow-Headers' * always;
            # required to be able to read Authorization header in frontend
            add_header 'Access-Control-Expose-Headers' * always;

            if ($request_method = 'OPTIONS') {
                # Tell client that this pre-flight info is valid for 20 days
                add_header 'Access-Control-Max-Age' 1728000;
                add_header 'Content-Type' 'text/plain charset=UTF-8';
                add_header 'Content-Length' 0;
                add_header 'Access-Control-Allow-Origin' $http_origin always;
                add_header 'Access-Control-Allow-Credentials' * always;
                add_header 'Access-Control-Allow-Methods' * always;
                add_header 'Access-Control-Allow-Headers' * always;
                # required to be able to read Authorization header in frontend
                add_header 'Access-Control-Expose-Headers' * always;

                return 204;
            }

            # by default, do not forward anything
            proxy_redirect off;
        }
    }

Create symbolic link::

    sudo ln -s /etc/nginx/sites-available/cups /etc/nginx/sites-enabled/

Check the syntax is ok::

    sudo nginx -t
    sudo systemctl restart nginx.service
