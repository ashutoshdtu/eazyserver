import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

# from ..core.function_mapper import FunctionMapper 
# mongo_pipelines = FunctionMapper()

from function_mapper import *
from utils import *
from influxdb_connector import *