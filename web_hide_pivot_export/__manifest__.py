# Copyright 2026 Munin
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Web Hide Pivot Export',
    'description': """
        Ability to hide export for users without custom group (Odoo Enterprise version)""",
    'version': '15.0.1.0.0',
    'license': 'OPL-1',
    'author': 'Munin',
    'website': 'https://github.com/AxeldelosReyes/odoo_web_modules',
    'depends': [
        'web', 'documents_spreadsheet'
    ],
    'assets': {
        'web.assets_backend': [
            'web_hide_pivot_export/static/src/js/web_hide_pivot_export.js',
        ],
        "web.assets_qweb": [
            "web_hide_pivot_export/static/src/xml/*.xml",
        ],
    },
    'data': [
        'security/pivot_manager.xml',
    ],
    'demo': [
    ],
}
