from dbModel import TechFgrPrintResult, db
from config import app

scanResult_dir = "C:/Users/dyani/Desktop/Intern/API_Practice/Osmedeus/"


def read_fgrprint(scan_id,domain_name):
    with app.app_context():
        # Result directory
        result_dir = scanResult_dir + f"{domain_name}/fingerprint/{domain_name}-raw-overview.txt"
        
        try:
            with open(result_dir, 'r') as f:
                # Skip header
                next(f)
                
                for line in f:
                    # Split line & get data
                    url, title, tech, resp_hash = line.strip().split(',')
                    
                    # Create new record
                    new_record = TechFgrPrintResult(
                        scan_id=scan_id,
                        url=url,
                        title=title,
                        tech=tech,
                        resp_hash=resp_hash
                    )
                    
                    db.session.add(new_record)

            # Commit changes
            db.session.commit()
            print(f"\033[92mScanID {scan_id}: Tech Fingerprint result update successfully to database\033[0m")
            
        except Exception as e:
            db.session.rollback()
            print(f"\033[91mError updating database: {str(e)}\033[0m")