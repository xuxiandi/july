# -*- coding: utf-8 -*-

"""July Tornado
"""

import os

#: always use utc time
os.environ['TZ'] = 'UTC'

#: always place python3 egg cache in /tmp
os.environ["PYTHON_EGG_CACHE"] = "/tmp/egg"


#: library
from july.web import JulyHandler, ApiHandler
from july.web import run_server
from july.app import JulyApp, JulyApplication


__version__ = '0.1'
__author__ = 'Hsiaoming Young'


#: initialize options
from tornado.options import define

_first_run = True
if _first_run:
    #: server configuration
    define('address', default='', type=str, help='run server at this address')
    define('port', default=8000, type=int, help='run server on this port')
    define('settings', default='', type=str, help='setting file path')

    #: application settings
    define('locale_path', type=str, help='absolute path of locale directory')
    define('default_locale', default='en_US', type=str)
    define('enable_app_static', default=True, type=bool)

    _first_run = False
