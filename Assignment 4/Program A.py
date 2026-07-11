# Program Name: Assignment4.py (use the name the program is saved as) 

# Course: IT3883/Section W01 

# Student Name: Gustavo Gonzalez 

# Assignment Number: Lab4 

# Due Date: 07/10/2026 

# Purpose: What does the program do (in a few sentences)? The program creates a local server built with sockets that listens for incoming connections from a client. When a client connects and sends a message, the server receives the message, converts it to uppercase, and sends it back to the client. The client program allows the user to input a message, sends it to the server, and displays the response received from the server.

# List Specific resources used to complete the assignment. 
#1. https://www.geeksforgeeks.org/python/network-programming-python-http-server/ 2. https://realpython.com/python-sockets/ 3.https://nshel.github.io/programming/python/tcp_client_server.html


import socket
# Defining the host and port for the client to connect to
HOST = '127.0.0.1'
PORT = 45000

def run_client():
    # Creating a user input to send to the server
    user_input = input("Enter a message to send to the Program B: ") 

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            # Connecting to the server
            client_socket.connect((HOST, PORT))
            # Sending the user input to the server
            client_socket.sendall(user_input.encode('utf-8'))
            # Receiving the response from the server
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Response from Program B: {response}")
        # Handling the instance where the connection is refused
        except ConnectionRefusedError:
            print("Connection refused. Make sure Program B is running and listening on the specified port.")

if __name__ == '__main__':
    run_client()

