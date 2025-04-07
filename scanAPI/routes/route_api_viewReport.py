import subprocess
from flask_restful import Resource, marshal_with, abort
from dbModel import TechFgrPrintResult, SubdomainResult, PortScanResult, VulScanResult
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

        # Subdomain Discovery Result
        subdomain_results = SubdomainResult.query.filter_by(scan_id=scan_id).all()

        # Port Scanning Result
        portscan_results = PortScanResult.query.filter_by(scan_id=scan_id).all()

        # Tech FingerPrint Result
        fgrprint_results = TechFgrPrintResult.query.filter_by(scan_id=scan_id).all()

        # Vulnerability Scanning Result
        vulscan_results = VulScanResult.query.filter_by(scan_id=scan_id).all()

        if not subdomain_results and not portscan_results and not fgrprint_results and not vulscan_results:
            abort(404, message="Scanning not found")


        return{
            "Subdomains": subdomain_results,
            "Port-Scans": portscan_results,
            "Tech-Fingerprint": fgrprint_results,
            "Vul-Scans": vulscan_results
        }
