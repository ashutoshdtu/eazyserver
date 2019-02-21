import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

import os
import operator

from eazyserver.rpc.meta import __list_methods

from flask import Blueprint, jsonify, Response, make_response, request, \
    current_app as app

jsonrpc_bp = Blueprint('eazy_jsonrpc_routes', __name__)

@jsonrpc_bp.route('/' + app.config["API_VERSION"] + '/' + app.config["RPC_BASE_ROUTE"] + '/' + app.config["RPC_ROUTE_NAME"], methods=['POST'])
def rpc():
    req = request.get_data().decode()
    response = app.methods.dispatch(req)
    return Response(str(response), response.http_status,
        mimetype='application/json')

@jsonrpc_bp.route('/' + app.config["API_VERSION"] + '/' + app.config["RPC_BASE_ROUTE"] + '/' + app.config["RPC_ROUTE_NAME"], methods=['GET'])
def list_aggregates():
    response = {
        "methods": __list_methods()
    }
    return jsonify(response)

