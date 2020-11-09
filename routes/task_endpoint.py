from models.task_model import Task 
from flask import Blueprint, jsonify, request, abort
from request_util import Request_Util

task_endpoint = Blueprint('task_endpoint',
                            __name__)

# Get endpoint
@task_endpoint.route('/tasks', methods=['GET'])
def get_all_tasks():
    body = request.get_json()
    if body is not None:
        category = body.get('category')
        if category is None:
            abort(400)

        tasks = Task.query.filter(
            Task.category == category).all()
        return jsonify({
            'success': True,
            'items': [task.format() for task in tasks]
        })
    else:
        return Request_Util.basic_get_request(Task)
        
    

#A Post endpoint
@task_endpoint.route('/tasks', methods=['POST'])
def create_task():
    body = Request_Util.get_body(request)

    description = body.get('description')
    category = body.get('category')

    new_task = Task(description, category)

    return Request_Util.basic_post_request(new_task)

#A Delete endpoint
@task_endpoint.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    return Request_Util.basic_delete_request(Task, task_id)
