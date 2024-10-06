'''
Real world example : Multi-processing o CPU-bound tasks 
Scenario : Factorial Calculation 

Factorial calculation, especially for large numbers, involve significant computation work. Multiprocessing can be used to distribute the workload across multiple CPU cores, improving performance. 
'''

import multiprocessing 
import math 
import sys 
import time 

## increase the maximum numbers of digits for integer conversion 
sys.set_int_max_str_digits(100000)

## function to compute factorial 

def compute_functorial(number):
    print(f"Calculating factorial for {number}")
    fact = math.factorial(number)
    # print(f"The factorial of {number} is {fact}")
    return fact

if __name__ == '__main__':
    numbers = [5000, 8000, 10000, 9000]
    start_time = time.time()

    ## creating a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_functorial, numbers)
    
    end_time = time.time()
    # print(results)
    print(f"duration : {end_time - start_time}")

