# Copyright 2021-Coopdevs Treball SCCL (<https://coopdevs.org>)
# - César López Ramírez - <cesar.lopez@coopdevs.org>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Auto setup bank on Res Partner Bank creation",
    "version": "12.0.1.0.0",
    "depends": ["base", "base_bank_from_iban"],
    "author": "Coopdevs Treball SCCL",
    "category": "Accounting & Finance",
    "website": "https://coopdevs.org",
    "license": "AGPL-3",
    "summary": """
        When a Res Partner Bank is created, a bank is set for it if it's empty
    """,
    "data": [],
    "installable": True,
}
