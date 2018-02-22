### ###############################################################################################
#
#   This module contains all configuration for the build process
#
### ###############################################################################################
ANGULAR_TAG = "~1.5.3"
module.exports =

    ### ###########################################################################################
    #   Name of the plugin
    ### ###########################################################################################
    name: 'dbconfig'
    dir: build: 'buildbot_dbconfig/static'
    bower:
        testdeps:
            # vendors.js includes jquery, angularjs, etc in the right order
            "guanlecoja-ui":
                version: '~1.6.0'
                files: ['vendors.js', 'scripts.js']
            "angular-mocks":
                version: ANGULAR_TAG
                files: "angular-mocks.js"
            "d3":
                version: "3.4.11"
                files: "d3.js"
            'buildbot-data':
                version: '~2.0.0'
                files: 'dist/buildbot-data.js'
    karma:
        files: ["tests.js", "scripts.js", 'fixtures.js']
