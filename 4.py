#Answer 4

from threading import *
from time import *
from math import *
def displayFactorial(num):
	print("The factorial of 5 is:", factorial(num))
 
        
t=Thread(target=displayFactorial,args=(5,))
t.start()
t.join()