from dbModel import TechFgrPrintResult, db
from config import app

def read_fgrprint(scan_id):
    with app.app_context():
        # Result directory
        result_dir = f"C:/Users/dyani/Desktop/Intern/API_Practice/Osmedeus/webapp8.wimify.xyz/fingerprint/webapp8.wimify.xyz-raw-overview.txt"
        
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
            print(f"Successfully updated {f.tell()} bytes of fingerprint data")
            
        except Exception as e:
            db.session.rollback()
            print(f"Error updating database: {str(e)}")