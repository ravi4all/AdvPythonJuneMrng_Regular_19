import threading
import time
import logging

# Logging Levels
# CRITICAL	    50
# ERROR	        40
# WARNING	    30
# INFO	        20
# DEBUG	        10
# NOTSET	    0

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-9s) %(message)s')

def worker():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

for i in range(3):
    th = threading.Thread(target=worker)
    th.start()