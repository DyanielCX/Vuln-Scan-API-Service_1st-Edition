import subprocess
from flask_restful import Resource
from dbModel import ScanModel, TechFgrPrintResult, db
from autoUdp.scanRslt_upd import read_fgrprint
from RespFmt import ViewStatResp

"""
Test Route
- Purpose: For any tetsing action purpose
- Route: '/api/test' 
- Methods: POST
"""
class Testing(Resource):
    # Post Request
    def post(self):

        # # Test read & save result
        # scan = ScanModel.query.filter_by(status='done').first()
        # if scan:
        #     cur_scanID = scan.scan_id
        #     cur_domain = scan.domain
        #     if not TechFgrPrintResult.query.filter_by(scan_id=cur_scanID).first():
        #         read_fgrprint(cur_scanID, cur_domain)
        # else:
        #     print("scanning not found")

        # Test remove unused result
        result_ID = 10
        result = TechFgrPrintResult.query.filter_by(id=result_ID).first()
        db.session.delete(result)
        db.session.commit()
    
        return ("Testing...")
