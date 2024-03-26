# Copyright 2026 Munin
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Web Sale Move Trash Icon',
    'description': """
        Modify trash icon to first row.""",
    'version': '15.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Munin',
    'depends': ['web'],
    'assets': {
        'web.assets_backend': [
            ('append', 'web_sale_move_trash_icon/static/src/js/*.js'),
        ]
    },
    'data': [
    ],
    'demo': [
    ],
}
