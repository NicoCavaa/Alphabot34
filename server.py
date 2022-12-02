import socket
import Alphabot
import time
import sqlite3

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
bot = Alphabot.AlphaBot()
comandi = {"w": "forward", "s": "backward","a": "left","d": "right"}
connect = sqlite3.connect("Percorso.db")
cur = connect.cursor()


s.bind(("192.168.0.149", 5000))
s.listen()

connection, address = s.accept()

while True:
    msg = connection.recv(4090)
    msg = msg.decode()

    if msg == "w":
        print("avanti")
        bot.forward()
    elif msg == "s":
        print("indietro")
        bot.backward()
    elif msg == "a":
        print("sinistra")
        bot.left()
        time.sleep(0.36)
        bot.stop()
    elif msg == "d":
        print("destra")
        bot.right()
        time.sleep(0.36)
        bot.stop()
    elif msg == "x":
        print("stop")
        bot.stop()
    elif msg == "1":
        print("CurvaDestra")
        bot.forward()
        time.sleep(4.5)
        bot.right()
        time.sleep(0.36)
        bot.stop()


    elif msg == "0":
        print("Stop")
        res = cur.execute(f"SELECT Movimento FROM Percorso WHERE ID = {0}")
        movement = res.fetchall()
        movement = movement[0][0]
        print(movement)
    elif msg == "1":
        print("Avanti")
        res = cur.execute(f"SELECT Movimento FROM Percorso WHERE ID = {1}")
        movement = res.fetchall()
        movement = movement[0][0]
        print(movement)
    elif msg == "2":
        print("Destra")
        res = cur.execute(f"SELECT Movimento FROM Percorso WHERE ID = {2}")
        movement = res.fetchall()
        movement = movement[0][0]
        print(movement)
    elif msg == "3":
        print("Dietro")
        res = cur.execute(f"SELECT Movimento FROM Percorso WHERE ID = {3}")
        movement = res.fetchall()
        movement = movement[0][0]
        print(movement)
    elif msg == "4":
        print("Sinistra")
        res = cur.execute(f"SELECT Movimento FROM Percorso WHERE ID = {4}")
        movement = res.fetchall()
        movement = movement[0][0]
        print(movement)
    elif msg == "5":
        print("CurvaDestra")
        res = cur.execute(f"SELECT Movimento FROM Percorso WHERE ID = {5}")
        movement = res.fetchall()
        movement = movement[0][0]
        print(movement)
    elif msg == "6":
        print("CurvaSinistra")
        res = cur.execute(f"SELECT Movimento FROM Percorso WHERE ID = {6}")
        movement = res.fetchall()
        movement = movement[0][0]
        print(movement)

s.close()




