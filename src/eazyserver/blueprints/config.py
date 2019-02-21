import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

import os
import operator

from eazyserver.core.utils import list_routes, get_app_config_as_dict, toJSON

from flask import Blueprint, jsonify, Response, make_response, request, \
    current_app as app

config_bp = Blueprint('eazy_config_routes', __name__)

@config_bp.route('/config', methods=['GET'])
def config():
    response = get_app_config_as_dict()
    return Response(toJSON(response), 200,
        mimetype='application/json')

@config_bp.route('/info', methods=['GET'])
def get_info():
    response = {
        "name": app.config["NAME"],
        "description": app.config["DESCRIPTION"],
        "version": app.config["VERSION"],
        "build": {
            "href": os.environ.get('CI_BUILD_LINK', '-')
        },
        "repo": {
            "name": os.environ.get('CI_REPO_NAME', '-'),
            "href": os.environ.get('CI_REPO_LINK', '-')
        },
        "commit": {
            "href": os.environ.get('CI_COMMIT_LINK', '-'),
            "author": os.environ.get('CI_COMMIT_AUTHOR_EMAIL', '-'),
        }
    }
    return jsonify(response)
