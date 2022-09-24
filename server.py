import socket
import threading

HOST = '192.168.0.128'
PORT = 1234
# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP type of socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # s variable is our TCP/IP socket
s.bind((HOST, PORT))
s.listen(5)

clients = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode('utf-8'))
        except Exception as e:
            print(e)            


def handler():
    while True:
        try:
            message = clientSocket.recv(1024).decode('utf-8')
            
            print("Message from client is: " + message)
            broadcast(message)
        except Exception as e:
            clientSocket.close
            print(f"Connection with {address} has ended.")
            print(e)
            break


print("Server is listening...")
while True:
    # now our endpoint knows about the OTHER endpoint.
    clientSocket, address = s.accept()
    print(f"Connection with {address} has been established.")
    clients.append(clientSocket)
    
    thread = threading.Thread(target=handler)
    thread.start()
