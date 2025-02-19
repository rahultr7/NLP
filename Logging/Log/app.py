from logger import logging

logger = logging.getLogger('Arithamtic App')

def add(a,b):
    logger.debug(f'Adding {a} and {b} gets {a+b}')
    return a + b

def divide(a,b):
    try:
        res = a/b
        logger.debug(f"Dividing {a} and {b} gets {res}")
        return res
    except ZeroDivisionError:
        logger.error("Zero division error")
        return 0

add(2,3)
divide(3,0)