import subprocess
import time
from docker import DockerClient
from docker.errors import NotFound, APIError

"""
This file is for some code testing purpose
"""

client = DockerClient.from_env()
container_name = "osmedeus-scanner"
container = client.containers.get(container_name)

# Execute the command
exit_code, output = container.exec_run("osmedeus scan -t example.com", tty=True)
print("Exit Code:", exit_code)
print("Output:", output.decode())

# Remove scan result
exit_code, output = container.exec_run("osmedeus config delete -w example.com", tty=True)

# try:
#     # Get the container object
#     container = client.containers.get(container_name)
    
#     # Start the container if it's not already running
#     if container.status != "running":
#         container.start()
#         print(f"Container '{container_name}' started.")
#     else:
#         print(f"Container '{container_name}' is already running.")
# except NotFound:
#     print(f"Container '{container_name}' does not exist.")
# except APIError as e:
#     print("Docker API error:", str(e))
# except Exception as e:
#     print("Unexpected error:", str(e))

# command = f"docker start osmedeus-scanner"
# subprocess.Popen(command, shell=True)

# time.sleep(5)

# type = "general"
domain = "example.com"
command = f"docker exec -it osmedeus-scanner  osmedeus scan -f {type} -t {domain} "
subprocess.Popen(command, shell=True)