from flask_restful import fields, reqparse

'''
Scanning Endpoint
Route: '/api/scan/' 
'''
# Define Scanning Args
scan_agrs = reqparse.RequestParser()
scan_agrs.add_argument('type', type=str, required=True, help="Type cannot be blank")
scan_agrs.add_argument('domain', type=str, required=True, help="Domain cannot be blank")

# Scanning Response Format
ScanResp = {
    'scan_id':fields.Integer,
    'type':fields.String,
    'domain':fields.String, 
    'status':fields.String, 
}