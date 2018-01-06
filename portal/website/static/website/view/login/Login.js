Ext.define('PlacementPortal.view.login.Login', {
    extend: 'Ext.container.Container',
    renderTo: Ext.getBody(),
    xtype: 'login',

    requires: [
        'Ext.form.Panel',
        'Ext.plugin.Viewport'
    ],

    plugins: 'viewport',

    bodyPadding: 10,
    title: 'Login Window',
//    closable: false,
//    autoShow: true,

    items: [{
        xtype: 'panel',
        height: 50,
        html: '<h1>Placement Portal</h1>',
    },{
        xtype: 'panel',

        layout: {
            type: 'hbox',
            pack: 'start',
            align: 'stretch'
        },

        items: [{
            html: 'panel 1',
            flex: 1
        },{
            xtype: 'form',
            reference: 'form',
            items: [{
                xtype: 'textfield',
                name: 'username',
                fieldLabel: 'Username',
                allowBlank: false
            }, {
                xtype: 'textfield',
                name: 'password',
                inputType: 'password',
                fieldLabel: 'Password',
                allowBlank: false
            }, {
                xtype: 'displayfield',
                hideEmptyLabel: false,
                value: 'Enter any non-blank password'
            }],
            buttons: [{
                text: 'Login',
                formBind: true,
                listeners: {
                    click: 'onLoginClick'
                }
            }]
        }]
    },{
        xtype: 'panel',
        height: 50,
        html: '(c) : Ayush Sharma',
    }]
});