# Copyright 2026 Munin
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo import Command


class ResUsers(models.Model):
    _inherit = "res.users"

    portal_url = fields.Char(string='Portal URL')

    def validate_portal_url(self, url):
        group = self.sudo().env['res.groups'].search([('portal_url', '=', url)])
        if self.env.user in group.users:
            return True
        return False
