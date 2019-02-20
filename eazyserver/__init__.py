# -*- coding: utf-8 -*-

"""Top-level package for eazyserver."""

__author__ = """Ashutosh Mishra"""
__email__ = 'ashutoshdtu@gmail.com'
__version__ = '0.1.0'


import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
SETTINGS_INI = os.path.join(BASE_DIR, 'settings.ini')
LOGGER_CONFIG = os.path.join(BASE_DIR, 'logger.conf')

#########################
# Initialize app before any imports
#########################
import logging
import logging.config
print "Logger config location", LOGGER_CONFIG
logging.config.fileConfig(LOGGER_CONFIG)
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

from jsonrpcserver import methods
from jsonrpcserver.exceptions import *

import core
import rpc
import blueprints

from exceptions import *
from eazyserver import Eazy
