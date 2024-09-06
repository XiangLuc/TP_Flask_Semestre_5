from flask import Blueprint, jsonify

'''
Une tâche contient les attributs suivants :
task_id : uuid
name : string
description : string
status : string
created_at : str
updated_at : str
task_db est un index qui se présente sous la forme suivante :
{
    "uuid1" : {
        "task_id" : "uuid1",
        "name": "Nom",
        "description": "Desc",
        "status": "TODO",
        "created_at" : "date de création",
        "updated_at" : "date de mise à jour"
    }
}
'''

task_bp = Blueprint('task_db', __name__)

task_db = dict()


@task_bp.route('/', methods=['GET'])
def get_tasks():
    return jsonify(task_db)


@task_bp.route('/:id', methods=['GET'])
def get_task_by_id(id):
    return jsonify(task_db.get(id))
