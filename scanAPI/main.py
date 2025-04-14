'''Library import'''
import subprocess
from flask_restful import Api
from apscheduler.schedulers.background import BackgroundScheduler
'''Local file import'''
from dbModel import db
from config import app
from autoUdp.scanStat_upt import check_exec_status
from routes.route_api_scan import Scan
from routes.route_api_viewStatus import viewStatus
from routes.route_api_viewReport import viewReport

from routes.route_api_test import Testing

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
api.add_resource(viewStatus, '/api/view-status/<int:scan_id>')
api.add_resource(viewReport, '/api/view-report/<int:scan_id>')

# Testing route
api.add_resource(Testing, '/api/test')

# Update the scan status every 2 minutes
scheduler = BackgroundScheduler()
scheduler.add_job(check_exec_status, 'interval', minutes=2)
scheduler.start()

# Prepare Route
@app.route('/')
def index():
    return '<h1>Vunlerability Scan API Service</h1>'

if __name__ == '__main__':
    app.run(debug=True)