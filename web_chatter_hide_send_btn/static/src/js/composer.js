/** @odoo-module **/

import {Composer} from "@mail/components/composer/composer";
import {patch} from "@web/core/utils/patch";


patch(Composer.prototype, "patch_composer_send_message", {
    setup() {
        this._super.apply(this, arguments);
    },

    /**
     * @override
     */
    _onComposerTextInputSendShortcut() {
        if (this.showSendButton) {
            this._super.apply(this, arguments);
        }
    },
    /**
     * @override
     */
    _onClickSend() {
        if (this.showSendButton) {
            this._super.apply(this, arguments);
        }
    },

    get showSendButton() {
        if (!this.composerView) {
            return false;
        }
        return this.composerView.composer.isLog;
    }

})

