/** @odoo-module **/

import {PivotView} from "@web/views/pivot/pivot_view";
import {patch} from "@web/core/utils/patch";
import {useService} from "@web/core/utils/hooks";


const {hooks} = owl;
const {onWillStart} = hooks;

patch(PivotView.prototype, "hide_pivot_export", {
    setup() {
        this._super.apply(this, arguments);
        this.userService = useService("user");
        onWillStart(async () => {
            this.canViewExport = await this.userService.hasGroup("web_hide_pivot_export.group_manager");
        });
    },

})