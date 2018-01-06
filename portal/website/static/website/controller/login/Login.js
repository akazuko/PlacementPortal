Ext.define('PlacementPortal.controller.login.Login', {

    extend: 'Ext.app.Controller',
    alias: 'controller.login',

    views : ["PlacementPortal.view.login.Login"],

    onLoginClick: function() {
        console.log("Worked!");
    }
});