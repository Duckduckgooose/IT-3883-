# Program Name: Assignment4.py (use the name the program is saved as) 

# Course: IT3883/Section W01 

# Student Name: Gustavo Gonzalez 

# Assignment Number: Lab4 

# Due Date: 07/10/2026 

# Purpose: What does the program do (in a few sentences)? The program creates a local server built with sockets that listens for incoming connections from a client. When a client connects and sends a message, the server receives the message, converts it to uppercase, and sends it back to the client. The client program allows the user to input a message, sends it to the server, and displays the response received from the server.

# List Specific resources used to complete the assignment. 
# #1. https://www.geeksforgeeks.org/python/network-programming-python-http-server/ 2. https://realpython.com/python-sockets/ 3.https://nshel.github.io/programming/python/tcp_client_server.html

import socket 

# Defining the host and port for the client to connect to
HOST = '127.0.0.1'
PORT = 45000

def run_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the host and port, and start listening for incoming connections
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server is listening on {HOST}:{PORT}")
        # Accept incoming connections in a loop
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received data: {data.decode('utf-8')}")

                upper_string = data.decode('utf-8').upper()  # Convert the received data to uppercase
                conn.sendall(upper_string.encode('utf-8'))  # Send the uppercase string
                

if __name__ == '__main__':
    run_server()
