'''Library import'''
import subprocess
from flask import Flask
from flask_restful import Api
from apscheduler.schedulers.background import BackgroundScheduler
'''Local file import'''
from dbModel import db
from config import app
from scanStat_upt import check_exec_status
from route_api_scan import Scan
# from Inhe_UserResq import User

# Initialize REST API
api = Api(app)

# Create database if not exist
with app.app_context():
    db.create_all()

# Start docker container
container_name = "osmedeus-scanner"
command = f"docker start {container_name}"
subprocess.Popen(command, shell=True)

# Create Endpoint
api.add_resource(Scan, '/api/scan/')
# api.add_resource(User, '/api/user/<int:id>')

# Update the scan status every 30 seconds
scheduler = BackgroundScheduler()
scheduler.add_job(check_exec_status, 'interval', seconds=30)
scheduler.start()

# Prepare Route
@app.route('/')
def index():
    return '<h1>Vunlerability Scan API Service</h1>'

if __name__ == '__main__':
    app.run(debug=True)