import socket
import threading

server = socket.socket()
host = socket.gethostname()

def name(name):
    print(f"[STARTING] Nombre del servidor {name}")
    print("[STARTING] Esperando conexiones...")

def abrir(texto,address):
    with open("mensajes.txt","a") as fl:
        fl.write(f"[{address}]: {texto}")
        fl.write("\n")
        fl.close()

name(host)
puerto = 1234

server.bind((host,puerto))
number = []

def main():
    try:
        while True:
            server.listen(2)
            conn, addr = server.accept()
            number.append(addr[0])
            print(f"[SERVER] Conexión recibida de {addr[0]}")
            print(f"[SERVER] Hay {len(number)} persona conectada esperando más conexiones...")
            conn.send("[SERVER] Done".encode("utf-8"))
            break 

        while True:
            try:
                message = conn.recv(1024)
                message = message.decode()
                if "$" in message:
                    while True:
                        print("[INFO] Puedes>> salir, eliminarChat, verChat")
                        prg = input("[Settings]>> ")
                        if prg == "salir":
                            conn.send("[SERVER] Escaped".encode("utf-8"))
                            break
                        elif prg == "eliminarChat":
                            with open("mensajes.txt","w") as fl:
                                fl.write("")
                                fl.close()
                        elif prg == "verChat":
                            with open("mensajes.txt","r") as fl:
                                lines = fl.readlines()
                                fl.close()
                            all_join = "".join(lines)
                            print(all_join)
                        else:
                            pass
                elif "username:" in message:
                    name_client = message[9:]
                    continue
                elif not message:
                    with open("mensajes.txt","r") as fl:
                        lines = fl.readlines()
                        fl.close()
                    msg = "".join(lines)
                    conn.send(msg.encode("utf-8"))
                else:
                    abrir(message,name_client)
                    print(f"[{name_client}] Mensaje recibido>> {message}")
                    with open("mensajes.txt","r") as fl:
                        lines = fl.readlines()
                        fl.close()
                    msg = "".join(lines)
                    conn.send(msg.encode("utf-8"))
            except:
                conn.send("[SERVER] Something failed".encode("utf-8"))
            continue
    except:
        print(f"[SERVER] A host disconected")
        server.close()

if __name__ == "__main__":
    first = threading.Thread(target=main)
    second = threading.Thread(target=main)
    first.start()
    second.start()
