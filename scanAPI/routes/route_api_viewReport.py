import subprocess
from flask_restful import Resource, marshal_with, abort
from dbModel import TechFgrPrintResult
from RespFmt import ReportResp

"""
View Report Endpoint
- Purpose: View all reports for the selected scanning
- Route: '/api/view-report/<int:scan_id>' 
- Methods: GET
"""
class viewReport(Resource):

    # Get Request
    @marshal_with(ReportResp)
    def get(self, scan_id):

        # Tech FingerPrint Result
        tech_results = TechFgrPrintResult.query.filter_by(scan_id=scan_id).all()

        if not tech_results:
            abort(404, message="Scanning not found")


        return{
            "Tech-Fingerprint": tech_results
        }
