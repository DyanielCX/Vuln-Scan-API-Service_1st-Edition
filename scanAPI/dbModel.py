from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Database Model
class ScanModel(db.Model):
    scan_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), nullable=False)
    domain = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(80), nullable=False)
    exec_id = db.Column(db.String(255))

    def __repr__(self):
        return f"Scan(scan_id={self.scan_id}, type={self.type}, domain={self.domain}, status={self.status}, exec_id={self.exec_id})"