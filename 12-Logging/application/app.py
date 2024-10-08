from logger import logging

def sum(num1, num2):
    logging.info("Adding 2 number")
    return num1, num2

result = sum(4,5)
print(f"result is {result}")
logging.info("execution completed")