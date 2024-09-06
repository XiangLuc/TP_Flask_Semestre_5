from flask import Blueprint, jsonify
from task_db import task_db

task_bp = Blueprint('task_db', __name__)


@task_bp.route('/', methods=['GET'])
def get_tasks():
    return jsonify(task_db)


@task_bp.route('/:id', methods=['GET'])
def get_task_by_id(id):
    return jsonify(task_db.get(id))
