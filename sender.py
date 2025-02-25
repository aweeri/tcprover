import socket
import logging
hostname = "192.168.1.27"

welcome = (
    "\033[31m\n"
    "  _____ ___ ___ ___  _____   _____ ___ \n"
    " |_   _/ __| _ \\ _ \\/ _ \\ \\ / / __| _ \\\n"
    "   | || (__|  _/   / (_) \\ V /| _||   /\n"
    "   |_| \\___|_| |_|_\\\\___/ \\_/ |___|_|_\\\n"
    "\033[0m"
)

def check_connection(host=hostname, port=5000, timeout=2):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0  # Returns True if the connection is successful

def send_command(command, host=hostname, port=5000, timeout=1):
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)  # Set timeout for the connection
        try:
            # Connect to the robot's server
            s.connect((host, port))
            # Send the command to the server
            s.sendall(command.encode('utf-8'))
            # Receive the response from the server
            response = s.recv(1024)
            print(f"> {response.decode('utf-8')}")
        except socket.timeout:
            print("> Connection timed out")
        except socket.error as e:
            print(f"> Socket error: {e}")

if __name__ == "__main__":
    print(welcome)
    connected = False
    while not connected:
        print(f"Connecting to {hostname} ... ", end="", flush=True)
        connected = check_connection()
        if connected:
            print(f"Connection established.")
        else:
            print(f"Failed to connect. Retrying...")
            
    # Example command input
    
    while connected:
            command = input("\033[31m$ \033[0m") 
            try:
                send_command(command)
            except:
                print("Failed to send command, try again.")