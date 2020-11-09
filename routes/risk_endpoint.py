from models.risks_model import Risk
from flask import Blueprint, jsonify, request, abort
from request_util import Request_Util
import datetime

risk_endpoint = Blueprint('risk_endpoint',
                            __name__)

# Get endpoint
@risk_endpoint.route('/risks', methods=['GET'])
def get_all_risks():
    return Request_Util.basic_get_request(Risk)

#A Post endpoint
@risk_endpoint.route('/risks', methods=['POST'])
def create_risk():
    body = Request_Util.get_body(request)

    riskItem = body.get('riskItem')
    actions = body.get('actions')
    impact = body.get('impact')
    impactDate = body.get('impactDate')
    status = body.get('status')

    new_risk = Risk(riskItem, actions, impact, impactDate, status)

    return Request_Util.basic_post_request(new_risk)

@risk_endpoint.route('/risks/<risk_id>', methods=['PATCH'])
def edit_risk(risk_id):
    body = Request_Util.get_body(request)
    risk = Risk.query.filter(
        Risk.id == risk_id).one_or_none()
    
    if risk is None:
        abort(404)
    if body.get('riskItem') is not None:
        risk.riskItem = body.get('riskItem')
    if body.get('actions') is not None:
        risk.actions = body.get('actions')
    if body.get('impact') is not None:
        risk.impact = body.get('impact')
    if body.get('impactDate') is not None:
        risk.impactDate = body.get('impactDate')
    else:
        risk.impactDate = datetime.datetime.utcnow()
    if body.get('status') is not None:
        risk.status = body.get('status')
    
    return Request_Util.basic_patch_request(risk)

#A Delete endpoint
@risk_endpoint.route('/risks/<risk_id>', methods=['DELETE'])
def delete_risk(risk_id):
    return Request_Util.basic_delete_request(Risk, risk_id)
