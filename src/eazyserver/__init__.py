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
__version__ = '0.2.7'


import logging
import logging.config
logging.config.fileConfig(LOGGER_CONFIG)
logger = logging.getLogger(__name__)
logger.debug("Loaded " + __name__)

from .eazyserver import Eazy
