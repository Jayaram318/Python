# demonstrate to threading in python

import threading
import time
# step : create a thread ---> sub class of thread

class thread1(threading.Thread):
    def run(self):
        for index in range(10):
            print("thread 1 :\n",+index)
            time.sleep(6)

class thread2(threading.Thread):
    def run(self):
        for index in range(10):
            print("thread 2\n :",+index)
            time.sleep(2)
            
t1 = thread1()
t1.start()        
t2 = thread2()
t2.start()