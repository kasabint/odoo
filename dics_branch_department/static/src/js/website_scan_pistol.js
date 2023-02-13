odoo.define('dics_web_pistol_scan_picking.scan_pistol', function (require) {
'use strict';

var sAnimations = require('website.content.snippets.animation');


sAnimations.registry.websiteScanPistol= sAnimations.Class.extend({
    selector: '.scan_pistol_web',
    events: {
        'input .pistol_number': '_onInputScanPistol',
    },

    /**
     * @constructor
     */
    init: function () {
        this._super.apply(this, arguments);
    },
    /**
     * @override
     */
    start: function () {
        var def = this._super.apply(this, arguments);
        return def;
    },
    _onInputScanPistol: function(){
        var val = $('.pistol_number').val();
        this._rpc({
            route: "/scan/pistol/redirect",
            params: {
                picking_number: val,
            },
        }).then(function (data) {
            if (data.url && data.url != false){
                window.location.href = data.url
            }
            else{
                $(".warning_message").text("Picking Number is mendatory or Entered Picking is Wrong")
            }
        });
    },
});

});
