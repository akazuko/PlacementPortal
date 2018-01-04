Ext.define('PlacementPortal.Application', {
    extend: 'Ext.app.Application',
    name: 'PlacementPortal',
    launch : function() {
        var loggedIn;

        // Check to see the current value of the localStorage key
        loggedIn = localStorage.getItem("UserLoggedIn");
        console.log(loggedIn);
        // This ternary operator determines the value of the TutorialLoggedIn key.
        // If TutorialLoggedIn isn't true, we display the login window,
        // otherwise, we display the main view
        Ext.create({
            xtype: loggedIn ? 'app-main' : 'login'
        });
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