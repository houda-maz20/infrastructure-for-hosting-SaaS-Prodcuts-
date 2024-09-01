import os
import subprocess

def is_port_in_use(port):
    result = subprocess.run(["docker", "ps", "--filter", f"publish={port}", "--format", "{{.ID}}"], capture_output=True, text=True)
    return result.stdout.strip() != ""

def get_next_port(port_range):
    start_port, end_port = port_range
    port_file = f'last_port_{start_port}.txt'

    if not os.path.exists(port_file):
        with open(port_file, 'w') as f:
            f.write(str(start_port - 1))

    with open(port_file, 'r') as f:
        last_port = int(f.read())

    next_port = last_port + 1
    if next_port > end_port:
        next_port = start_port

    while next_port <= end_port:
        if not is_port_in_use(next_port):
            with open(port_file, 'w') as f:
                f.write(str(next_port))
            return next_port
        next_port += 1

    return None

def run_nginx_container():
    image_name = "my-nginx-image"
    port_range = (8080, 8090)
    next_port = get_next_port(port_range)

    if next_port is None:
        return None, "No available ports for Nginx."

    command = [
        "ansible-playbook", 
        "playbooks/nginx_playbook.yml",  
        "-e", f"next_port={next_port}",
        "-e", f"port={next_port}",
        "-e", f"image_name={image_name}"
    ]

    subprocess.run(command)

    return f"nginx_container_{next_port}", next_port
