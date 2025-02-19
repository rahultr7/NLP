## Multi thread
## When to Use - I/O Bound task(Task that takes more time for IO operations)
## Concorrent operations

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Printing number {i}")

def print_letters():
    for letters in "abcde":
        time.sleep(2)
        print(f"Letter are {letters}")

###Thraed Creation
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)


###Starting thread 
t = time.time()   
t1.start()
t2.start()

#Waiting for thread to complete
t1.join()
t2.join()


finish_time = time.time()-t

print(finish_time)