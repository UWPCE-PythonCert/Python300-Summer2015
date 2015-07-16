import logging
import worker
format='%(asctime)s %(message)s'
logging.basicConfig(filename='basic.log', format=format, level=logging.DEBUG)

if __name__ == '__main__':
    logging.debug("debug level message")
    logging.warning("warning level message")
    worker.worker()
    logging.info("test complete")

'''
NOTE:
1. where are messages?
2. worker import logging
3. handles handler magic
'''