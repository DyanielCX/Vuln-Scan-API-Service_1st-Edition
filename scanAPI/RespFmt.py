from flask_restful import fields, reqparse

'''
Scanning Endpoint
Route: '/api/scan/' 
'''
# Define Scanning Args
scan_agrs = reqparse.RequestParser()
scan_agrs.add_argument('type', type=str, required=True, help="Type cannot be blank")
scan_agrs.add_argument('domain', type=str, required=True, help="Domain cannot be blank")

# Scanning Route Response Format
ScanResp = {
    'scan_id':fields.Integer,
    'type':fields.String,
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
# Tech Fingerprint Response Format
TechFgrPrintResp = {
    'id': fields.Integer,
    'url': fields.String,
    'scan_id': fields.Integer,
    'title': fields.String,
    'tech': fields.String,
    'resp_hash': fields.String
}

# Subdomain Response Format
SubdomainResp = {
    'id': fields.Integer,
    'scan_id': fields.Integer,
    'data': fields.String
}

# Port Scan Response Format
PortScanResp = {
    'id': fields.Integer,
    'scan_id': fields.Integer,
    'data': fields.String
}

# Combined Report Response Format
ReportResp = {
    'Tech-Fingerprint': fields.List(fields.Nested(TechFgrPrintResp))
    # 'Subdomains': fields.List(fields.Nested(SubdomainResp)),
    # 'Port-Scans': fields.List(fields.Nested(PortScanResp))
}