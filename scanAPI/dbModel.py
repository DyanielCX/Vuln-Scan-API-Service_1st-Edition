from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.sqlite import JSON

db = SQLAlchemy()

# Scan Info Database Model
class ScanModel(db.Model):
    scan_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), nullable=False)
    domain = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(80), nullable=False)
    exec_id = db.Column(db.String(255), nullable=False)

    db.relationship('ScanResults', backref='scan', uselist=False, lazy=True)

    def __repr__(self):
        return f"Scan(scan_id={self.scan_id}, type={self.type}, domain={self.domain}, status={self.status}, exec_id={self.exec_id})"
    
# Scan Result Database Model
class ScanResults(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scan_id = db.Column(db.Integer, db.ForeignKey('scan_model.scan_id'), unique=True, nullable=False)
    subdomain = db.Column(JSON)
    port_scan = db.Column(JSON)
    tech_fgrprint = db.Column(JSON)
    vul_scan = db.Column(JSON)
