import subprocess
from flask_restful import Resource, marshal_with
from dbModel import ScanModel, db
from RespFmt import scan_agrs, ScanResp
from docker import DockerClient

"""
Scanning Endpoint
- Purpose: Start scanning for a domain
- Route: '/api/scan' 
- Methods: POST
"""
class Scan(Resource):

    # Post Request
    @marshal_with(ScanResp)
    def post(self):
        container_name = "osmedeus-scanner"

        # Parse request data
        agrs = scan_agrs.parse_args()
        domain = agrs["domain"]

        # Start scanning in the background
        client = DockerClient.from_env()
        container = client.containers.get(container_name)
        
        # Step 1: Create the exec instance and get exec_id
        exec_id = container.client.api.exec_create(
            container.id,  # ID of the container
            cmd=f"osmedeus scan -f API-custom -t {domain}",
            tty=True
        )["Id"]

        # Step 2: Start the exec instance in detached mode
        container.client.api.exec_start(exec_id, detach=True)


        # Save scan info to the database
        new_scan = ScanModel(
            domain=domain,
            status="running",
            exec_id=exec_id
        )

        db.session.add(new_scan)
        db.session.commit()

        return new_scan, 201