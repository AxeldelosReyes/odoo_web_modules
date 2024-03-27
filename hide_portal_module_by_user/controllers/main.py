# Copyright 2026 Munin
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
from werkzeug.exceptions import NotFound

WHITELISTED_ROUTES = ['/my/home', '/my', '/my/account', '/my/security', '/my/payment_method']


class CustomerPortalPolicy(CustomerPortal):
    def _prepare_portal_layout_values(self):
        vals = super()._prepare_portal_layout_values()
        current_routes = request.endpoint.routing.get('routes', [])
        for route_url in current_routes:
            if request.env.user.validate_portal_url(route_url) or route_url in WHITELISTED_ROUTES:
                return vals
        if all('/my/' not in x for x in current_routes):
            return vals
        raise NotFound()
