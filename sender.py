import socket

def send_command(command, host='192.168.1.27', port=5000):
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the robot's server
        s.connect((host, port))
        # Send the command to the server
        s.sendall(command.encode('utf-8'))
        # Receive the response from the server
        response = s.recv(1024)
        print(f"> {response.decode('utf-8')}")

if __name__ == "__main__":
    # Example command input
    
    while True:
            command = input("\033[31m$ \033[0m") 
            try:
                send_command(command)
            except:
                print("Failed to send command, try again.")