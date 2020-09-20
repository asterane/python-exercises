from threading import Thread
from time import sleep
import sys

x = 1

def echoer():
    global x
    while True:
        x = input()


def printer():
    y = x
    while True:
        if y != x:
            print(x)
            y = x
        sleep(1)

try:
    t1 = Thread(target=echoer)
    t2 = Thread(target=printer)
    t1.start()
    t2.start()
    while True:
        sleep(100)
except (KeyboardInterrupt,):
    print("goodbye")
    exit()
# t2 = DisplayToScreen()

# t2.start()
