import socket
import subprocess
import logging

HOST = ''          # Listen on all available network interfaces
PORT = 5000        # Choose an available port

logging.basicConfig(level=logging.INFO)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server listening on port {PORT}...")
    logging.info(f"Server listening on port {PORT}...")

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
                logging.info(f"Received command: {command}")
                
                
                if command.lower() == 'help':
                    response = "List of allowed commands:\nhelp\nupdate\nreload\nping"
                    
                    conn.sendall(response.encode())
                
                elif command.lower() == 'update':
                    # Change directory to your repository and run git pull
                    result = subprocess.run(
                        ['git', 'pull'],
                        cwd='/home/ari/tcprover',  # update this to your repo location
                        capture_output=True,
                        text=True
                    )
                    response = f"\n{result.stdout}\n{result.stderr}\nType 'reload' to apply changes"
                    
                
                elif command.lower() == 'reload':
                    response = f"\nReloading..."
                    conn.sendall(response.encode())
                    conn.shutdown(socket.SHUT_RDWR)
                    exit()
                    

                elif command.lower() == 'ping':
                    response = f"pong"
                    conn.sendall(response.encode())
                
                else:
                    conn.sendall(b"Unknown command")
                
