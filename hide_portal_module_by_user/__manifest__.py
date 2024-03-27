# Copyright 2026 Munin
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Hide Portal Module By User',
    'description': """
        Show / Hide Specific Portal Docs on res.users""",
    'version': '15.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Munin',
    'website': 'https://github.com/AxeldelosReyes/odoo_web_modules',
    'depends': [
        'base', 'portal'
    ],
    'data': [
        'views/portal_home.xml',
        'views/res_groups.xml',
    ],
    'demo': [
    ],
    'post_init_hook': 'post_init_hook',
}
