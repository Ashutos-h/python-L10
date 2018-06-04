#Answer 3

from threading import *
from time import *
def displayList(l1):
    j=0
    for i in range(2,11,2):
        print(l1[j])
        print('Going to sleep for {} seconds'.format(i))
        sleep(i)
        j+=1
        
l1=['a','b','c','d','e']
print('The complete list is as follows:\n{}'.format(l1))
t=Thread(target=displayList,args=(l1,))
t.start()
t.join()