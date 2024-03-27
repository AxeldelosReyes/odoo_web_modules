from odoo import api, SUPERUSER_ID


def post_init_hook(cr, registry):
    """Loaded after installing the module.
    This module's DB modifications will be available.
    :param odoo.sql_db.Cursor cr:
        Database cursor.
    :param odoo.modules.registry.RegistryManager registry:
        Database registry, using v7 api.
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    portal_views = env['ir.ui.view'].search([('inherit_id.xml_id', '=', 'portal.portal_my_home')])
    if portal_views:
        for p in portal_views:
            p.create_group_from_view()
    return True
