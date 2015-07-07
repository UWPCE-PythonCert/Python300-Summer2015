import time
import logging
logging.basicConfig(level=logging.INFO)
from contextlib import contextmanager

@contextmanager
def tracker_cm(name):
    logging.info('Entering: {}'.format(name))
    yield
    logging.info('Exiting: {}'.format(name))

def work():
    logging.info('Doing lots of work here...')
    time.sleep(3)

if __name__ == '__main__':
    with tracker_cm('work') as something:
        logging.info('[ SOMETHING ]: {}'.format(something))
        work()
        
# NOTE: 
# enter yield something
# exit exc become harder

