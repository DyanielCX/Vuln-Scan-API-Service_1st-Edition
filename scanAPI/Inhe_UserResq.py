from flask_restful import Resource, marshal_with, abort
from dbModel import ScanModel, db
from RespFmt import scan_agrs, ScanResp

"""
User Resource (Single User)
- Purpose: Manage individual user data (GET/PATCH/DELETE)
- Route: '/api/user/<int:id>' 
- Methods: GET, PATCH, DELETE
"""
# class User(Resource):
#     # Get Request
#     @marshal_with(ScanModel)
#     def get(self, id):
#         user = ScanModel.query.filter_by(id=id).first()
#         if not user:
#             abort(404, message="User not found")
#         return user
    
#     # Patch Request
#     @marshal_with(ScanModel)
#     def patch(self, id):
#         agrs = scan_agrs.parse_args()
#         user = ScanModel.query.filter_by(id=id).first()
#         if not user:
#             abort(404, message="User not found")
#         user.name = agrs["name"]
#         user.email = agrs["email"]
#         db.session.commit()
#         return user
    
#     # Delete Request
#     @marshal_with(ScanModel)
#     def delete(self, id):
#         user = scan_agrs.query.filter_by(id=id).first()
#         if not user:
#             abort(404, message="User not found")
#         db.session.delete(user)
#         db.session.commit()
#         users = scan_agrs.query.all()
#         return users