from models.resource_model import ResourceManagement
from flask import Blueprint, jsonify, request, abort
from request_util import Request_Util
import datetime

resource_endpoint = Blueprint('resource_endpoint',
                                __name__)

# A GET endpoint to get all the resources
@resource_endpoint.route('/resources', methods=['GET'])
def get_all_capabilities():
    return Request_Util.basic_get_request(ResourceManagement)


# A POST endpoint used to create new resources
@resource_endpoint.route('/resources', methods=['POST'])
def create_resource():
    body = Request_Util.get_body(request)

    projectName = body.get('projectName')
    roles = body.get('roles')
    resourceName = body.get('resourceName')
    status = body.get('status')
    updatedDate = body.get('updatedDate')
    new_resource = ResourceManagement(projectName, roles,
                                      resourceName,
                                      status, updatedDate)

    return Request_Util.basic_post_request(new_resource)

#A Patch endpoint.
@resource_endpoint.route('/resources/<resource_id>', methods=['PATCH'])
def edit_resource(resource_id):
    body = Request_Util.get_body(request)
    resource = ResourceManagement.query.filter(
        ResourceManagement.id == resource_id).one_or_none()
    
    if resource is None:
        abort(404)
    
    if body.get('projectName') is not None:
        resource.projectName = body.get('projectName')
    if body.get('resourceName') is not None:
        resource.resourceName = body.get('resourceName')
    if body.get('status') is not None:
        resource.status = body.get('status')
    if body.get('updatedDate') is not None:
        resource.updatedDate = body.get('updatedDate')
    else:
        resource.updatedDate = datetime.datetime.utcnow()
    if body.get('roles') is not None:
        resource.roles = body.get('roles')

    return Request_Util.basic_patch_request(resource)

# A DELETE endpoint used to delete a resource 
@resource_endpoint.route('/resources/<resource_id>', 
                         methods=['DELETE'])
def delete_project(resource_id):
    return Request_Util.basic_delete_request(ResourceManagement, 
                                        resource_id)