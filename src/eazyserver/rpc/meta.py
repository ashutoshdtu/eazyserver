import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

import json
from ..rpc import methods

@methods.add
def __list_methods():
    result = []
    for method in methods:
        result.append(str(method))
    return result

@methods.add
def __ping():
    logger.info("Inside Ping Pong")
    return 'pong'
