Ext.define('PlacementPortalApp.view.login.Login', {
  extend: 'Ext.Panel',
  xtype: 'app-login',
  
  requires: [
    'Ext.Panel',
    'Ext.Label',
    'PlacementPortalApp.view.login.LoginForm',
    'PlacementPortalApp.view.common.Footnote'
  ],
  layout: 'vbox',

  items: [{
    xtype: 'panel',
    layout: 'hbox',
    flex: 10,
    items: [
      {
        xtype: 'panel',
        flex: 1,
      },{
        xtype: 'panel',
        flex: 1,

        layout: 'vbox',

        defaults: {
          flex: 1
        },

        items: [
          {
            xtype: 'panel',
            items: [{
              xtype: 'label',
              style: {
                'font-size': 'xx-large',
                'text-align': 'center',
                'padding-top': '40px',
                'color': 'skyblue'
              },
              html: 'Placement Portal',
              flex:1
            }]
          },{
            xtype: 'app-login-form',
            flex: 2
          },{
            xtype: 'panel'
          }
        ]
      },{
        xtype: 'panel',
        flex: 1
      }
    ]
  },{
    xtype: 'app-footnote',
    flex: 1
  }]
  
  
});