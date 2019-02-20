import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

from ..rpc import methods
from eazyserver.core import write_points

@methods.add
def write_to_influx(db, measurement, elements):
    write_points(db, measurement, elements)
