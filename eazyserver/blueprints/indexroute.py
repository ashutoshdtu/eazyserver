import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

import os
import operator

from eazyserver.core.utils import list_routes, get_app_config_as_dict, toJSON

from flask import Blueprint, jsonify, Response, make_response, request, \
    current_app as app

index_bp = Blueprint('eazy_index_route', __name__)

@index_bp.route('/', methods=['GET'])
def index():
    response = {
        "_links": {
            "all": list_routes()
        },
        "_meta": {
            "build": {
                "href": os.environ.get('CI_BUILD_LINK', '-')
            }
        }
    }
    return jsonify(response)
