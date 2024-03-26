/** @odoo-module **/



var core = require('web.core');
var ListRenderer = require('web.ListRenderer');
require('web.EditableListRenderer');
var _t = core._t;

ListRenderer.include({
    /**
     * @override
     * @private
     */
    _renderFooter: function () {
        const $footer = this._super.apply(this, arguments);
        if (this.addTrashIcon && this.state.model === 'sale.order.line') {
            $footer.find('tr td:last').remove();
            $footer.find('tr').prepend($('<td>'));
        }
        return $footer;
    },
    /**
     * Override to optionally add a th in the header for the remove icon column.
     *
     * @override
     * @private
     */
    _renderHeader: function () {
        var $thead = this._super.apply(this, arguments);
        if (this.addTrashIcon && this.state.model === 'sale.order.line') {
            $thead.find('tr td.o_list_record_remove_header').remove();

            $thead.find('tr').prepend($('<th>', {class: 'o_list_record_remove_header'}));
        }
        return $thead;
    },
    /**
     * Overriden to add a resize handle in editable list column headers.
     * Only applies to headers containing text.
     *
     * @override
     * @private
     */

    /**
     * Editable rows are possibly extended with a trash icon on their right, to
     * allow deleting the corresponding record.
     * For many2many editable lists, the trash bin is replaced by X.
     *
     * @override
     * @param {any} record
     * @param {any} index
     * @returns {jQueryElement}
     */
    _renderRow: function (record, index) {

        var $row = this._super.apply(this, arguments);
        if (this.addTrashIcon && this.state.model === 'sale.order.line') {
            $row.find('td.o_list_record_remove').remove();

            var $icon = this.isMany2Many ?
                $('<button>', {
                    'class': 'fa fa-times',
                    'name': 'unlink',
                    'aria-label': _t('Unlink row ') + (index + 1)
                }) :
                $('<button>', {
                    'class': 'fa fa-trash-o',
                    'name': 'delete',
                    'aria-label': _t('Delete row ') + (index + 1)
                });
            var $td = $('<td>', {class: 'o_list_record_remove'}).append($icon);
            $row.prepend($td);
        }
        return $row;
    },
});


