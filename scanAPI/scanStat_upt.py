from dbModel import ScanModel, db
from scanRslt_upd import read_fgrprint
from docker import DockerClient
from config import app

# Initialize Docker client
client = DockerClient.from_env()

def check_exec_status():
    with app.app_context():
        # Get all running scans info
        running_scans = ScanModel.query.filter_by(status='running').all()
        
        for scan in running_scans:
            try:
                # Get the exec instance
                exec_info = client.api.exec_inspect(scan.exec_id)
                
                if exec_info['Running'] is False:
                    # Retrieve exit code
                    exit_code = exec_info['ExitCode']
                    
                    # Update status based on exit code
                    if exit_code == 0:
                        scan.status = "done"
                        
                        # cur_scanID = scan.scan_id
                        # read_fgrprint(cur_scanID)
                        
                    elif exit_code == 1:
                        scan.status = "failed"
                    else:
                        print(exit_code)
                        scan.status = "error"
                    
                    db.session.commit()
            except Exception as e:
                print(e)
                scan.status = "error"
                db.session.commit()
