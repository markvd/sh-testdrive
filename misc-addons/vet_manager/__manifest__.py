# -*- coding: utf-8 -*-
# Copyright 2017 West IT Solutions
{
    "name": "Vet Manager",
    "summary": "This module will help veterinary clinic manage ther business",
    "version": "11.0.1.0.0",
    "category": "Uncategorized",
    # "website": "https://github.com/OCA/<repo>" or "https://github.com/OCA/<repo>/tree/<branch>/<addon>",
    "author": "Mark van Deursen - West IT Solutions",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    # "pre_init_hook": "pre_init_hook",
    # "post_init_hook": "post_init_hook",
    # "post_load": "post_load",
    # "uninstall_hook": "uninstall_hook",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
        "purchase",
        # "sales",
    ],
    "data": [
        # "security/some_model_security.xml",
        # "security/ir.model.access.csv",
        # "templates/assets.xml",
        # "views/report_name.xml",
        # "views/res_partner_view.xml",
        # "wizards/wizard_model_view.xml",
    ],
    "demo": [
        # "demo/res_partner_demo.xml",
    ],
    "qweb": [
        # "static/src/xml/module_name.xml",
    ]
}
