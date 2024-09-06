from flask import Flask
from flask_cors import CORS
from task_db import task_bp

app = Flask(__name__)
cors = CORS(app)


app.register_blueprint(task_bp, url_prefix='/task')

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
