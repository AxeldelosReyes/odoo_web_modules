# Copyright 2026 Munin
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from lxml import etree

from odoo import _, api, fields, models


class ResGroups(models.Model):
    _inherit = "res.groups"

    portal_url = fields.Char(string='Portal URL', index=True)


class IrUiView(models.Model):
    _inherit = "ir.ui.view"

    custom_portal_group = fields.Boolean(string='Custom Portal Group', default=False)
    portal_group = fields.Many2one('res.groups', string='Portal Group')

    @api.model_create_multi
    def create(self, vals_list):
        res = super(IrUiView, self).create(vals_list)
        for view in res:
            if view.inherit_id.xml_id == 'portal.portal_my_home':
                view.create_group_from_view()
        return res

    def create_group_from_view(self):
        self.ensure_one()

        def _generate_name(name):
            return f"show_portal_{name}".lower().replace(' ', '_')

        # self = self.with_context(lang='es_MX')  # change to your language if needed since the default is 'en_US'
        view_xml = etree.fromstring(self.arch)
        groups_from_view = {}
        for option in view_xml.xpath("//t[@t-call='portal.portal_docs_entry']"):  # type: etree._Element
            has_title = option.find("t[@t-set='title']")
            if has_title is not None:
                title = has_title.text
            else:
                title = self.name

            k = _generate_name(title)
            target_url = option.find("t[@t-set='url']")
            if target_url is not None:
                target_url = target_url.get('t-value').replace("'", '')
            else:
                raise ValueError(_("No target url found"))
            groups_from_view[k] = target_url

        search_groups = self.env['res.groups'].sudo().search([('portal_url', 'in', list(groups_from_view.values()))])
        for group in groups_from_view.keys():
            portal_group = search_groups.filtered(lambda g: g.portal_url == groups_from_view[group])
            if not portal_group:
                self.env['res.groups'].sudo().create(
                    {'name': group, 'portal_url': groups_from_view[group]})
        return True
