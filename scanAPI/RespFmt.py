from flask_restful import fields, reqparse
from sqlalchemy.dialects.sqlite import JSON

'''
Scanning Endpoint
Route: '/api/scan/' 
'''
# Define Scanning Args
scan_agrs = reqparse.RequestParser()
scan_agrs.add_argument('domain', type=str, required=True, help="Domain cannot be blank")

# Scanning Route Response Format
ScanResp = {
    'scan_id':fields.Integer,
    'domain':fields.String, 
    'status':fields.String
}


'''
Scanning Endpoint
Route: '/api/view-status/<int:scan_id>' 
'''
# View Status Route Response
ViewStatResp = {
    'scan_id':fields.Integer,
    'domain':fields.String, 
    'status':fields.String
}


"""
View Report Endpoint
- Route: '/api/view-report/<int:scan_id>' 
"""
# Subdomain Response Format
SubdomainResp = {
    'id': fields.Integer,
    'scan_id': fields.Integer,
    'domain_url': fields.String
}

# Port Scan Response Format
PortScanResp = {
    'id': fields.Integer,
    'scan_id': fields.Integer,
    'ip_addr': fields.String,
    'opened_port': fields.String
}

# Tech Fingerprint Response Format
TechFgrPrintResp = {
    'id': fields.Integer,
    'scan_id': fields.Integer,
    'url': fields.String,
    'title': fields.String,
    'tech': fields.String,
    'resp_hash': fields.String
}

# Vulnerability Scanning Response Format
VulScanResp = {
    'id': fields.Integer,
    'scan_id': fields.Integer,
    'result': fields.Raw
}

# Combined Report Response Format
ReportResp = {
    'Subdomains': fields.List(fields.Nested(SubdomainResp)),
    'Port-Scans': fields.List(fields.Nested(PortScanResp)),
    'Tech-Fingerprint': fields.List(fields.Nested(TechFgrPrintResp)),
    'Vul-Scans': fields.List(fields.Nested(VulScanResp))
}