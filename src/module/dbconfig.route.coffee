# Register new state
class State extends Config
    constructor: ($stateProvider, config, glMenuServiceProvider, bbSettingsServiceProvider) ->

        # Name of the state
        name = 'dbconfig'

        # Configuration
        glMenuServiceProvider.addGroup
            name: name
            caption: 'DbConfig'
            icon: 'th-list'
            order: 10 
        cfg =
            group: name
            caption: 'DbConfig'

        # Register new state
        state =
            controller: "#{name}Controller"
            controllerAs: "w"
            templateUrl: "dbconfig/views/#{name}.html"
            name: name
            url: "/#{name}"
            data: cfg

        if config.plugins.dbconfig['show_menu']
            $stateProvider.state(state)

        bbSettingsServiceProvider.addSettingsGroup
            name:'DbConfig'
            caption: 'DbConfig related settings'
            items:[
                type:'text'
                name:'name'
                caption:'Config name'
                default_value:''
            ]

