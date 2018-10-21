Ext.define('PlacementPortalApp.view.login.LoginForm', {
  extend: 'Ext.form.Panel',
  xtype: 'app-login-form',

  layout: {
    type: 'vbox',
    align: 'stretch'    
  },

  defaults : {
    layout: 'hbox',
    height: "70px"
  },

  items: [
    {
      xtype: 'emailfield',
      name: 'email',
      label: 'Email',
      width: '100%'
    },{
      xtype: 'passwordfield',
      name: 'password',
      label: 'Password',
      width: '100%'
    },
    {
      xtype: 'button',
      text: 'login',
      width: '100%',
      height: '40px',
      ui: 'round',
      style: {
        background: "lightskyblue",
        color: "white" 
      }
    },{
      height: "30px"
    },{
      html: '<a href="https://www.google.com" target="blank">Forgot Password?</a>'
    }
  ]
});