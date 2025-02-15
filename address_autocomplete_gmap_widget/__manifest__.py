# -*- coding: utf-8 -*-
{
    'name': "Address Autocomplete Widget",

    'summary': "Google Map Address Autocomplete Widget",

    'description': """
        Enhances Odoo address fields with real-time Google Maps address suggestions, improving data entry accuracy and speed.  Retrieves detailed address components and geocodes addresses. Requires a Google Maps API key.
    """,

     'author': "Dhrushil Butani",
    'maintainer': 'Dhrushil Butani',
    'category': 'Extra Tools',
    'version': '18.0.1.0',

    'depends': ['base','base_setup'],

    # always loaded
    'data': [
        'views/res_config_settings_view.xml',
        'views/res_partner_test.xml'
    ],
    "assets": {
        "web.assets_backend": [
            "address_autocomplete_gmap_widget/static/src/**/*",
            "address_autocomplete_gmap_widget/static/src/**/*",

        ]
    },

    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

