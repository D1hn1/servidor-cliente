import socket
import time

client = socket.socket()

puerto = 1234
host = input("[CLIENT] introduce el nombre del host>> ")

try:
    client.connect((host,puerto))
    client.recv(1024)
    while True:
        name = input("[CLIENT] Pon usename: y tu nombre>> ")
        if "username:" in name:
            client.send(name.encode("utf-8"))
            break
        else:
            print("\n[INFO] You have to put username: to enter your name\n")

    while True:
        msg = input("[CLIENT] mensaje>> ")
        time.sleep(0.2)
        if msg:
            client.send(msg.encode("utf-8"))
            message = client.recv(1024)
            print(message.decode())
        elif not msg:
            continue
except:
    client.close()
    print("\nBye\n")
    pass
