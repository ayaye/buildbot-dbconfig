# buildbot-dbconfig
Buildbot plugin that allows www-plugins to store settings in database.

This plugin creates the endpoint 'dbconfig/api/config?name={cfg}'.
Multiple configurations are supported. The 'name' parameter is a configuration name.
GET/PUT loads/stores configuration in buildbot database.

Add 'dbconfig' to master.cfg:

        c['www'] = dict(plugins=dict(dbconfig={'show_menu':False}...}

The 'show_menu' parameter controls visibility of DbConfig menu item (mostly used for debug).

Example controller code: 

        name=...
        dbConfigUrl = '/dbconfig/api/config?name='

        $scope.loadConfig = () ->
            $http.get(dbConfigUrl+name).then (cfg) ->
                $scope.cfg = cfg.data

        $scope.saveConfig = () ->
            $http.put(dbConfigUrl+name,$scope.cfg)

