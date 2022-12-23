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
"""
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
"""

while True:
    if msg ==  "1":
        res = cur.execute(f"SELECT Movimento FROM Percorso WHERE ID = {1}")
        movement = res.fetchone()
        mov = movement.split(";")
        mov = mov.split(",")
        for i in mov:  #bot. i[0] --> w (i[1]) --> 1000
            if i[0] == "w":
                bot.left(int(i[1]))
            if i[0] == "a":
                bot.left(int(i[1]))
            if i[0] == "d":
                bot.left(int(i[1]))
            if i[0] == "x":
                bot.stop()
            
        #print(mov)
    elif msg == "2":
        print("sinistra")
        res = cur.execute(f"SELECT Movimento FROM Percorso WHERE ID = {2}")
        movement = res.fetchone()
        mov = movement.split(";")
        mov = mov.split(",")
        for i in mov:  #bot. i[0] --> w (i[1]) --> 1000
            if i[0] == "w":
                bot.left(int(i[1]))
            if i[0] == "a":
                bot.left(int(i[1]))
            if i[0] == "d":
                bot.left(int(i[1]))
            if i[0] == "x":
                bot.stop()

    elif msg == "3":
        res = cur.execute(f"SELECT Movimento FROM Percorso WHERE ID = {3}")
        movement = res.fetchone()
        mov = movement.split(";")
        mov = mov.split(",")
        for i in mov:  #bot. i[0] --> w (i[1]) --> 1000
            if i[0] == "w":
                bot.left(int(i[1]))
            if i[0] == "a":
                bot.left(int(i[1]))
            if i[0] == "d":
                bot.left(int(i[1]))
            if i[0] == "x":
                bot.stop()

    elif msg == "4":
        res = cur.execute(f"SELECT Movimento FROM Percorso WHERE ID = {4}")
        movement = res.fetchone()
        mov = movement.split(";")
        mov = mov.split(",")
        for i in mov:  #bot. i[0] --> w (i[1]) --> 1000
            if i[0] == "w":
                bot.left(int(i[1]))
            if i[0] == "a":
                bot.left(int(i[1]))
            if i[0] == "d":
                bot.left(int(i[1]))
            if i[0] == "x":
                bot.stop()
s.close()




