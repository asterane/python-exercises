from threading import Thread
from time import sleep
import sys

def timer():
    for i in range(45):
        sleep(1)
        #print(i) #waits 45 seconds
    sys.exit() #stops program after timer runs out

def question():
    answer = eval(input("foo"))
    print(answer)

t1 = Thread(target=timer)
t2 = Thread(target=question)
t1.start()
t2.start()
