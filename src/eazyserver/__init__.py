# -*- coding: utf-8 -*-

"""Top-level package for eazyserver."""

import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
SETTINGS_INI = os.path.join(BASE_DIR, 'settings.ini')
LOGGER_CONFIG = os.path.join(BASE_DIR, 'logger.conf')
# VERSION_FILE = os.path.join(BASE_DIR, 'VERSION')
# with open('VERSION') as version_file:
#     version = version_file.read().strip()


__author__ = """Ashutosh Mishra"""
__email__ = 'ashutoshdtu@gmail.com'
__version__ = '0.1.8'


import logging
import logging.config
print "Logger config location", LOGGER_CONFIG
logging.config.fileConfig(LOGGER_CONFIG)
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)


import core
import rpc
import blueprints

from exceptions import *
from eazyserver import Eazy
