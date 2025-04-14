from dbModel import ScanModel, TechFgrPrintResult, SubdomainResult, PortScanResult, VulScanResult, db
from autoUdp.scanRslt_upd import read_fgrprint, read_subdomain, read_portscan, read_vulscan
from docker import DockerClient
from config import app
import subprocess

# Initialize Docker client
client = DockerClient.from_env()
container_name = "osmedeus-scanner"

def check_exec_status():
    with app.app_context():
        # Update the scanning status
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

        # Update the scanning result
        scans = ScanModel.query.filter_by(status='done').all()
        for scan in scans:
            cur_scanID = scan.scan_id
            cur_domain = scan.domain

            # status Flag
            FgrPrint_flag = False
            PortScan_flag = False
            Subdomain_flag = False
            VulScan_flag = False

            if not TechFgrPrintResult.query.filter_by(scan_id=cur_scanID).first():
                read_fgrprint(cur_scanID, cur_domain)
                FgrPrint_flag = True

            if not PortScanResult.query.filter_by(scan_id=cur_scanID).first():
                read_portscan(cur_scanID, cur_domain)
                PortScan_flag = True

            if not SubdomainResult.query.filter_by(scan_id=cur_scanID).first():
                read_subdomain(cur_scanID, cur_domain)
                Subdomain_flag = True

            if not VulScanResult.query.filter_by(scan_id=cur_scanID).first():
                read_vulscan(cur_scanID, cur_domain)
                VulScan_flag = True
            
            # Delete the added osmedeus scanning result
            if any([FgrPrint_flag,PortScan_flag,Subdomain_flag,VulScan_flag]):
                subprocess.Popen(f"docker exec -it osmedeus-scanner osmedeus config delete -w {cur_domain}", shell=True)
