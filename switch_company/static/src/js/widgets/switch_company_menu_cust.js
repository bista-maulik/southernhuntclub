odoo.define('switch_company.switch_company_menu_cust', function(require) {
"use strict";
console.log("comming")
var SwitchCompanyMenu = require('web.SwitchCompanyMenu');
var session = require('web.session');

var switch_company = SwitchCompanyMenu.include({
	/**
     * @override
     * @param {MouseEvent|KeyEvent} ev
     **/
	_onToggleCompanyClick: function (ev) {
        if (ev.type == 'keydown' && ev.which != $.ui.keyCode.ENTER && ev.which != $.ui.keyCode.SPACE) {
            return;
        }
        ev.preventDefault();
        ev.stopPropagation();
        var dropdownItem = $(ev.currentTarget).parent();
        var dropdownMenu = dropdownItem.parent();
        var companyID = dropdownItem.data('company-id');
        var allowed_company_ids = this.allowed_company_ids;
        var arr = [];
        var current_company_id = allowed_company_ids[0];

        if (dropdownItem.find('.fa-square-o').length) {
            dropdownMenu.find('.fa-check-square').removeClass('fa-check-square').addClass('fa-square-o');
            dropdownItem.find('.fa-square-o').removeClass('fa-square-o').addClass('fa-check-square');
            $(ev.currentTarget).attr('aria-checked', 'true');
        } else{
            dropdownItem.find('.fa-check-square').addClass('fa-square-o').removeClass('fa-check-square');
            $(ev.currentTarget).attr('aria-checked', 'false');
        }
        arr.push(companyID)
        session.setCompanies(current_company_id, arr);
    },

});

return switch_company;

});
