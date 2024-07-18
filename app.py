from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv

load_dotenv()

host_name = getenv('HOST_NAME')
db_name = getenv('DB_NAME')
db_username = getenv('DB_USERNAME')
db_password = getenv('DB_PASSWORD')
port = getenv('PORT')

app = Flask(__name__)
app.json.sort_keys = False
 
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_username}:{db_password}@{host_name}:{port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    status = db.Column(db.String(50), default='0')
    url = db.Column(db.String(100), unique=True)

with app.app_context():
    db.create_all()

@app.route('/')
def get_statuses():
    return render_template('statuses.html', values=Project.query.all())

@app.route('/all', methods=['GET'])
def get_statuses_json():
    projects = Project.query.all()
    response = {
        project.name: {
            "status": project.status,
            "url": project.url
        }
        for project in projects
    }
    return jsonify(response)

@app.route('/status/<project>', methods=['GET'])
def get_status(project):
    project = Project.query.filter_by(name=project).first()
    if project:
        response = {
            project.name: {
                "status": project.status,
                "url": project.url
            }
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Project not found"}), 404
    
# to było używane żeby zmieniać rzeczy poprzez jaką kolwiek
# apkę sql używając post co działało tymczasowo,
# przeniesione na używanie bazy dan oraz discordpy

if __name__ == "__main__":
    app.run(debug=True)