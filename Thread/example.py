import multiprocessing
import math
import sys
import time


sys.set_int_max_str_digits(1000000)

def compute_factorial(n):
    print(f"The factoral of the given number {n}")
    result = math.factorial(n)
    print(f"The factorial of {n} is {result}")
    return result

if __name__ == "__main__":
    number = [10000,20000,30000,40000]
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        result = pool.map(compute_factorial,number)

    end_time = time.time()

    print(result) 
    print(f"Time taken to compute factorial of {number} is {end_time-start_time} seconds")
