import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

import os
import operator

from flask import Blueprint, jsonify, Response, make_response, request, \
    current_app as app

health_bp = Blueprint('eazy_health_routes', __name__)

@health_bp.route('/health', methods=['GET'])
def health():
    response = {
        "status": "UP",
        "checks": []
    }
    return jsonify(response)

@health_bp.route('/ready', methods=['GET'])
def ready():
    response = {
        "status": "UP",
        "checks": []
    }
    return jsonify(response)
