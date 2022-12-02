import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.0.144",5000))

while True:
    movimento = input("Inserisci movimento: ")
    s.sendall(movimento.encode())
    
s.close()