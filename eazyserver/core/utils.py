import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

import json
import HTMLParser
from bson import json_util
from bson.son import SON
from bson.objectid import ObjectId
from eve.utils import str_to_date, date_to_rfc1123
from flask import current_app as app

def bson_to_json(_object):
    return json.loads(json.dumps(_object, default=json_util.default))

def json_to_bson(_object):
    return json_util.loads(json.dumps(_object))

def toJSON(_object):
    return json.dumps(_object, default= lambda o: o.__str__(), 
        sort_keys=True)

def unescape(s):
    h= HTMLParser.HTMLParser()
    return h.unescape(s)

def get_app_config_as_dict():
    response = {}
    for key in app.config.iterkeys():
        response[key] = app.config[key]
    return response

def list_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        route = {
            "title": rule.endpoint,
            "href": unescape( str(rule) ),
            "methods": sorted(rule.methods)
        }
        routes.append(route)
    return routes
