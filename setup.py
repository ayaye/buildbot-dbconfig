#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

try:
    from buildbot_pkg import setup_www_plugin
except ImportError:
    import sys
    print("Please install buildbot_pkg module in order to install that package, or use the pre-build .whl modules available on pypi", file=sys.stderr)
    sys.exit(1)


setup_www_plugin(
    name='buildbot-dbconfig',
    description='Buildbot DbConfig plugin',
    author=u'Alexey Demakov',
    author_email=u'moris.aye.aye@gmail.com',
    packages=['dbconfig'],
    package_data={
        '': [
            'VERSION',
            'static/*'
        ]
    },
    entry_points="""
        [buildbot.www]
        dbconfig = dbconfig:ep
    """,
    install_requires=[
          'klein',
    ],
)
