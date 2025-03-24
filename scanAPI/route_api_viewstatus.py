import subprocess
from flask_restful import Resource, marshal_with, abort
from dbModel import ScanModel
from RespFmt import ViewStatResp

"""
View Status Endpoint
- Purpose: View status for selected scanning
- Route: '/api/view-status/<int:scan_id>' 
- Methods: POST
"""
class viewStatus(Resource):

    # Get Request
    @marshal_with(ViewStatResp)
    def get(self, scan_id):
        scan = ScanModel.query.filter_by(scan_id=scan_id).first()
        if not scan:
            abort(404, message="Scanning not found")
        return scan
