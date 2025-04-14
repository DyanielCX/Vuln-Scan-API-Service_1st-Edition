import subprocess
from flask_restful import Resource
from dbModel import ScanModel, TechFgrPrintResult, SubdomainResult, PortScanResult, VulScanResult, db
from autoUdp.scanRslt_upd import read_fgrprint, read_subdomain, read_portscan, read_vulscan
from RespFmt import ViewStatResp

"""
Test Route
- Purpose: For any testing action purpose
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

        #     if not PortScanResult.query.filter_by(scan_id=cur_scanID).first():
        #         read_portscan(cur_scanID, cur_domain)

        #     if not SubdomainResult.query.filter_by(scan_id=cur_scanID).first():
        #         read_subdomain(cur_scanID, cur_domain)

        #     if not VulScanResult.query.filter_by(scan_id=cur_scanID).first():
        #         read_vulscan(cur_scanID, cur_domain)
        # else:
        #     print("scanning not found")

        # # Test remove unused Subdomain result
        # result_ID = 1
        # result = SubdomainResult.query.filter_by(id=result_ID).first()
        # db.session.delete(result)
        # db.session.commit()

        # # Test remove unused Port Scanning result
        # result_ID = 3
        # result = PortScanResult.query.filter_by(id=result_ID).first()
        # db.session.delete(result)
        # db.session.commit()

        # # Test remove unused Fingerprint result
        # result_ID = 1
        # result = TechFgrPrintResult.query.filter_by(id=result_ID).first()
        # db.session.delete(result)
        # db.session.commit()

        # # Test remove unused Vulnerability Scanning result
        # result_ID = 1
        # result = VulScanResult.query.filter_by(id=result_ID).first()
        # db.session.delete(result)
        # db.session.commit()

        # # Test remove unused Scanning Info
        # scan_ID = 3
        # result = ScanModel.query.filter_by(scan_id=scan_ID).first()
        # db.session.delete(result)
        # db.session.commit()
    
        return ("Testing...")
