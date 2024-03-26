# Copyright 2026 Munin
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Web Chatter Hide Send Btn',
    'description': """
        Web Chatter Send Message Hide Button""",
    'version': '15.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Munin',
    'depends': [
        'mail', 'web'
    ],
    'assets': {
        "web.assets_backend": [
            "web_chatter_hide_send_btn/static/src/js/composer.js",
        ],
        "web.assets_qweb": [
            "web_chatter_hide_send_btn/static/src/xml/composer.xml",
        ],
    },
}
