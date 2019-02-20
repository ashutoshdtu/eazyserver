import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

import datetime
from flask import current_app as app

from influxdb import InfluxDBClient
clients = {}

def init_influxdb_client(db):
    if db not in clients.keys():
        clients[db] = InfluxDBClient(
            app.config["INFLUX_HOST"], 
            app.config["INFLUX_PORT"],
            app.config["INFLUX_USER"],
            app.config["INFLUX_PASSWORD"],
            db
        )
    return clients

def get_current_time():
    # return datetime.datetime.utcnow().isoformat()
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

def write_points(db, measurement, elements):
    init_influxdb_client(db)
    for element in elements:
        if "time" not in element:
            element["time"] = get_current_time()
        element["measurement"] = measurement
    logger.debug("Write points: {0}".format(elements))
    clients[db].write_points(elements)
