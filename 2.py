from threading import *
from time import *
def display():
    for i in range(1,11):
        sleep(1)
        print(i)

t=Thread(target=display)
t.start()