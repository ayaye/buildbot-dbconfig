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
    license='LGPLv3',
    url='https://github.com/ayaye/buildbot-dbconfig',
    long_description=open('README.rst', 'r').read(),
    packages=['buildbot_dbconfig'],
    package_data={
        '': [
            'VERSION',
            'static/*'
        ]
    },
    entry_points="""
        [buildbot.www]
        dbconfig = buildbot_dbconfig:ep
    """,
    install_requires=[
          'klein',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
