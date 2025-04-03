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

    # One-to-many relationship btw tables
    db.relationship('ScanResults', backref='scan', lazy=True)

    def __repr__(self):
        return f"Scan(scan_id={self.scan_id}, type={self.type}, domain={self.domain}, status={self.status}, exec_id={self.exec_id})"
    
# Scan Result Database Model
## Subdomain
class SubdomainResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scan_id = db.Column(db.Integer, db.ForeignKey('scan_model.scan_id'), nullable=False, index=True)
    data = db.Column(db.String(100), nullable=False)

## Port Scanning
class PortScanResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scan_id = db.Column(db.Integer, db.ForeignKey('scan_model.scan_id'), nullable=False, index=True)
    data = db.Column(db.String(80), nullable=False)

## Tech Finger Print
class TechFgrPrintResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scan_id = db.Column(db.Integer, db.ForeignKey('scan_model.scan_id'), nullable=False, index=True)
    url = db.Column(db.String(120), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    tech = db.Column(db.String(100), nullable=False)
    resp_hash = db.Column(db.String(255), nullable=False)

## Vul Scan
class VulScanResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scan_id = db.Column(db.Integer, db.ForeignKey('scan_model.scan_id'), nullable=False, index=True)
    data = db.Column(JSON, nullable=False)

