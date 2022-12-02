import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.0.149",5000))

while True:
    movimento = input("Inserisci un movimento")
    s.sendall(movimento.encode())

s.close()