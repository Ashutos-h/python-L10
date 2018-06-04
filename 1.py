#Answer 1
from threading import *
from time import *
def display():
	print("Starting thread:")
	sleep(5)
	print("Ending Thread")
t=Thread(target=display)
t.start()

	
	
