## Multi-processing 
## Creating the processs runs in parallel 
# 1. CPU-bound tasks : Tasks that are heavy on CPU usage (e.g. mathematical computation, data processing)
# 2. Parallel execution : Multiple cores of the CPU 

import multiprocessing
import time 

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"Square : {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Cube : {i*i*i}")


if __name__ == '__main__':
    # creating 2 processes
    p1 = multiprocessing.Process(target=square_number)
    p2 = multiprocessing.Process(target=cube_numbers)

    start_time = time.time()
    # square_number()
    # cube_numbers()

    # start the processs
    p1.start()
    p2.start()

    # Wait for the process to complete
    p1.join()
    p2.join()

    duration = time.time() - start_time
    print(f"Duration : {duration}")
