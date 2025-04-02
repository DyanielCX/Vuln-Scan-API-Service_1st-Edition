import subprocess
from flask_restful import Resource
from dbModel import ScanModel, TechFgrPrintResult
from scanRslt_upd import read_fgrprint
from RespFmt import ViewStatResp

"""
Test Route
- Purpose: To do testing
- Route: '/api/test' 
- Methods: POST
"""
class Testing(Resource):
    # Post Request
    def post(self):
        # Testing
        scan = ScanModel.query.filter_by(status='done').first()
        if scan:
            cur_scanID = scan.scan_id
            if not TechFgrPrintResult.query.filter_by(scan_id=cur_scanID).first():
                read_fgrprint(cur_scanID)
        else:
            print("scanning not found")
        return ("Testing...")
