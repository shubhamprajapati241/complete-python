from logger import logging


logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger("Arithmetic APP")

def add(a,b):
    result = a + b 
    logger.debug(f"Adding {a} + {b} = {result}")
    return result 

def subtract(a,b):
    result = a - b 
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result  

def multiple(a,b):
    result = a * b 
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result  

def divide(a,b):
    try:
        result = a/b 
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result 
    except ZeroDivisionError:
        logger.error("Division by zero errror")
        return None
    
add(10,20)
subtract(20, 3)
multiple(5,2)
divide(10,4)