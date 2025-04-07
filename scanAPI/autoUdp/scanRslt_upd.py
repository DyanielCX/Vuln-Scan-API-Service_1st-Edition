from dbModel import TechFgrPrintResult, SubdomainResult, PortScanResult, VulScanResult, db
from config import app
import json

## Scanning Result Directory
scanResult_dir = "C:/Users/dyani/Desktop/Intern/API_Practice/Osmedeus/"


## Load Subdomain Function
def read_subdomain(scan_id,domain_name):
    with app.app_context():
        # Result directory
        result_dir = scanResult_dir + f"{domain_name}/subdomain/final-{domain_name}.txt"

        try:
            with open(result_dir, 'r') as f:
                
                for line in f:                    
                    cleaned_data = line.strip()
                    if cleaned_data:
                        # Create new record
                        new_record = SubdomainResult(
                            scan_id = scan_id,
                            domain_url = cleaned_data
                        )
                    
                    db.session.add(new_record)

            # Commit changes
            db.session.commit()
            print(f"\033[92mScanID {scan_id}: Subdomain Discovery result update successfully to database\033[0m")
            
        except Exception as e:
            db.session.rollback()
            print(f"\033[91mError updating database(Subdomain): {str(e)}\033[0m")


## Load Port Scanning Function
def read_portscan(scan_id,domain_name):
    with app.app_context():
        # Result directory
        result_dir = scanResult_dir + f"{domain_name}/portscan/raw-open-ports.txt"

        try:
            with open(result_dir, 'r') as f:
                
                for line in f:                    
                    # Split line & get data
                    ip_addr, openedPorts = line.strip().split(' -> ')

                    # Convert the ports set from string to array
                    openedPorts = [str(port) for port in openedPorts.strip('[]').split(',')]

                    for opened_port in openedPorts:
                        # Create new record
                        new_record = PortScanResult(
                            scan_id = scan_id,
                            ip_addr = ip_addr,
                            opened_port = opened_port
                        )
                        
                        db.session.add(new_record)

            # Commit changes
            db.session.commit()
            print(f"\033[92mScanID {scan_id}: Port Scanning result update successfully to database\033[0m")
            
        except Exception as e:
            db.session.rollback()
            print(f"\033[91mError updating database(portscan): {str(e)}\033[0m")


## Load Tech Fingerprint Function
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
                        scan_id = scan_id,
                        url = url,
                        title = title,
                        tech = tech,
                        resp_hash = resp_hash
                    )
                    
                    db.session.add(new_record)

            # Commit changes
            db.session.commit()
            print(f"\033[92mScanID {scan_id}: Tech Fingerprint result update successfully to database\033[0m")
            
        except Exception as e:
            db.session.rollback()
            print(f"\033[91mError updating database(Tech Fingerprint): {str(e)}\033[0m")


## Load Vulnerability Scanning Function
def read_vulscan(scan_id,domain_name):
    with app.app_context():
        # Result directory
        result_dir = scanResult_dir + f"{domain_name}/vuln/nuclei/{domain_name}-nuclei-json.txt"
        
        try:
            # Read and parse JSONL
            with open(result_dir, 'r') as f:
                # Load all entries into a list of dictionaries
                vulscan_results = [json.loads(line.strip()) for line in f]
                
                # Create new record
                new_record = VulScanResult(
                    scan_id = scan_id,
                    result = vulscan_results
                )
                
                db.session.add(new_record)

            # Commit changes
            db.session.commit()
            print(f"\033[92mScanID {scan_id}: Vulnerability Scanning result update successfully to database\033[0m")
            
        except Exception as e:
            db.session.rollback()
            print(f"\033[91mError updating database(Vul Scan): {str(e)}\033[0m")