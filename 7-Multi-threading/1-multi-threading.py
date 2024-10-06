## Multi-threading 
import threading
import time 

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for l in "asdfghjhgds":
        time.sleep(2)
        print(f"Letter : {l}")

# creating 2 thread 
t1 = threading.Thread(target= print_numbers)
t2 = threading.Thread(target= print_letter)

start = time.time()
t1.start()
t2.start()

## wait for the threads to complete
t1.join()
t2.join()

duration = time.time() - start
print(f"duration : {duration}")