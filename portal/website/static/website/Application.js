Ext.define('PlacementPortal.Application', {
    extend: 'Ext.app.Application',
    appFolder : '/static/website',
    name: 'PlacementPortal',

    controllers : ['PlacementPortal.controller.login.Login'],

    launch : function() {
        Ext.create({
            xtype: 'login'
        });
        console.log("Worked");
//        Ext.create('Ext.panel.Panel', {
//            title: 'Sencha App',
//            width: 300,
//            height: 300,
//            bodyPadding:10,
//            renderTo: Ext.getBody(),
//            html:'Hello World'
//        });
    },

     onAppUpdate: function () {
        Ext.Msg.confirm('Application Update', 'This application has an update, reload?',
            function (choice) {
                if (choice === 'yes') {
                    window.location.reload();
                }
            }
        );
    }

});