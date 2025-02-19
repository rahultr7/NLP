import multiprocessing
import multiprocessing.pool
import multiprocessing.process
import time

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"Square:{i*i}")
        
def cube():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube:{i*i*i}")
        
        
        
if __name__ == "__main__":        
    ## create 2 process
    t = time.time()   
    p1 = multiprocessing.Process(target=square_number)
    p2 = multiprocessing.Process(target=cube)

    p1.start()
    p2.start()


    p1.join()
    p2.join()

    finish_time = time.time()-t

    print(finish_time)