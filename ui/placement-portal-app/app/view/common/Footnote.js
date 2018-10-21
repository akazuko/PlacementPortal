Ext.define('PlacementPortalApp.view.common.Footnote', {
  extend: 'Ext.form.Panel',
  xtype: 'app-footnote',

  requires: [
    'Ext.Panel',
  ],

  layout: 'hbox',
  
  items: [{
    flex: 6,
    xtype: 'panel'
  },{
    flex:1,
    xtype: 'panel',
    layout: 'hbox',
    items:[{
      style: {
        'padding-right': '5px'
      },
      html: 'Made with'
    }, {
      style: {
        color: "red",
        'padding-right': '5px'
      },
      html: '<i class="fa fa-heart" style="color:red"></i>'
    }, {
      html: 'by  <a href="akazuko.github.io" target="blank">Ayush Sharma</a>'
    }]
  }]
});