import socket
import subprocess

HOST = ''          # Listen on all available network interfaces
PORT = 5000        # Choose an available port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server listening on port {PORT}...")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                command = data.decode().strip()
                print(f"Received command: {command}")
                
                if command.lower() == 'update':
                    # Change directory to your repository and run git pull
                    result = subprocess.run(
                        ['git', 'pull'],
                        cwd='/home/ari/tcprover',  # update this to your repo location
                        capture_output=True,
                        text=True
                    )
                    response = f"\n{result.stdout}\n{result.stderr} \n\n Type 'reload' to apply changes"
                    conn.sendall(response.encode())
                
                if command.lower() == 'reload':
                    response = f"\n{result.stdout}\n{result.stderr} \n\n Reloading..."
                    conn.sendall(response.encode())
                    exit()
                    
                
                if command.lower() == 'ping':
                    response = f"pong"
                    conn.sendall(response.encode())
                
                else:
                    conn.sendall(b"Unknown command")
                
