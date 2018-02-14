class Dbconfig extends Controller

    dbConfigUrl = '/dbconfig/api/config?name='

    constructor: ($scope,$state,$log,$http,config,dataService,resultsService,bbSettingsService) ->
        # make resultsService utilities available in the template
        _.mixin($scope, resultsService)

        console.log('dbconfig start')

        $scope.settings = bbSettingsService.getSettingsGroup("DbConfig")
        $scope.$watch('settings', ->
            bbSettingsService.save()
        , true)

        $scope.getName = () ->
            return $scope.settings['name'].value

        $scope.loadConfig = () ->
            console.log('dbconfig.loadConfig()')
            $http.get(dbConfigUrl+$scope.getName()).then (cfg) ->
                $scope.cfg = JSON.stringify(cfg.data)
                console.log('  name: ' + $scope.getName())
                console.log('  cfg: ' + $scope.cfg)

        $scope.saveConfig = () -> 
            console.log('  name: ' + $scope.getName())
            console.log('dbconfig.saveConfig(): ' + $scope.cfg)
            $http.put(dbConfigUrl+$scope.getName(),$scope.cfg)

        $scope.loadConfig()

        console.log('dbconfig end')
