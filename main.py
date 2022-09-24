import os
from sys import platform


def startServer():
    if platform == "linux" or platform == "linux2":
        cmd="gnome-terminal -e 'python3 server.py'" #works in linuxv
    elif platform == "win32":
        cmd="start cmd.exe /c py server.py" #works in windows
    
    # os.system("gnome-terminal -e 'bash -c \""+command+";bash\"'")
    os.system(cmd)
    
def startClient():
    if platform == "linux" or platform == "linux2":
        cmd="gnome-terminal -e 'python3 client.py'" #works in linux
    elif platform == "win32":
        cmd="start cmd.exe /c py client.py" #works in windows
        
    os.system(cmd)  


def main():
    while True:
        command = input("Enter Command: ")
        
        if command == "sc":
            startClient()
        elif command == "ss":
            startServer()
        elif command == "exit":
            if platform == "linux" or platform == "linux2":
                cmd="clear"  #used in linux
            elif platform == "win32":
                cmd="cls"    #used in windows 

            os.system(cmd)
            break
        else:
            print("wrong command")

main()