import uuid
from datetime import datetime

from flask import Blueprint, jsonify, request
from task_db import task_db

task_bp = Blueprint('task_bp', __name__)


@task_bp.route('/', methods=['GET'])
def get_tasks():
    status = request.args.get('status')
    if status in ['DONE', 'IN_PROGRESS', 'TODO']:
        filtre_status = [task for task in task_db.values() if task['status'] == status]
        return jsonify(filtre_status)
    return jsonify(task_db)


@task_bp.route('/<string:id>', methods=['GET'])
def get_task_by_id(id):
    task = task_db.get(id)
    if task:
        return jsonify(task_db.get(id))
    return jsonify(task), 404


@task_bp.route('/', methods=['POST'])
def create_task():
    data = request.get_json()

    task_id = str(uuid.uuid4())
    current_time = datetime.now()

    if 'name' not in data or 'description' not in data or 'status' not in data:
        return jsonify({"erreur": "il manque des champs pour créer la tache."}), 404

    if data['status'] not in ['DONE', 'IN_PROGRESS', 'TODO']:
        return jsonify({"erreur": "le status saisi n'est pas conforme."}), 404

    new_task = {
        "task_id": task_id,
        "name": data['name'],
        "description": data['description'],
        "status": data['status'],
        "created_at": current_time,
        "updated_at": current_time
    }

    task_db[task_id] = new_task

    return jsonify({"true": f"La tache a été créer"}), 201


@task_bp.route('/id', methods=['PUT'])
def update_task(id):
    if id not in task_db:
        return jsonify({"erreur": f"l'identifiant de la tache : {id} n'existe pas"}), 404

    data = request.get_json()

    # Pas eu le temps d'écrire les conditions de vérification

    task = task_db[id]
    update_task = {
        "task_id": id,
        "name": data['name'],
        "description": data['description'],
        "status": data['status'],
        "created_at": task['created_at'],
        "updated_at": datetime.now()
    }

    task_db[id] = update_task

    return jsonify(update_task), 200


@task_bp.route('/<string:id>', methods=['DELETE'])
def delete_task(id):
    if id not in task_db:
        return jsonify({"erreur": f"l'identifiant de la tache : {id} n'existe pas."})
    del task_db[id]
    return jsonify({"true": f"La tache : {id} a été supprimer."})