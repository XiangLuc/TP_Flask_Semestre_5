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


task_db = dict(
    {
        "1": {
            "task_id" : "1",
            "name": "Première tache",
            "description": "Voici la première tache",
            "status": "TODO",
            "created_at": "6/11/2024",
            "updated_at": "6/11/2024"
        }
    }
)