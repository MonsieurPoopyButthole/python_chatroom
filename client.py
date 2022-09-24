import socket
import threading
from time import sleep

HOST = '192.168.0.128'
PORT = 1234

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
except:
    print("unable to connect")

def receiveFromServer():
    while True: 
        try:
                message = s.recv(1024).decode('utf-8')
                print(message)
        except Exception as e:
            print(e)
            sleep(5)
            print("connection closed")
            s.close()
            break


def write():
    while True:
        try:
            message = input("==")
            
            s.send(message.encode('utf-8'))
        except Exception as e:
            print(e)
            break


rcv_thread = threading.Thread(target=receiveFromServer)
rcv_thread.start()

wrt_thread = threading.Thread(target=write)
wrt_thread.start()

# sleep(5)