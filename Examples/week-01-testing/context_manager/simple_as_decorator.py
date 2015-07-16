import time
import logging
logging.basicConfig(level=logging.INFO)
from contextlib import contextmanager

@contextmanager
def tracker_cm(name):
    logging.info('Entering: {}'.format(name))
    yield 'blah'
    logging.info('Exiting: {}'.format(name))

def work():
    logging.info('Doing lots of work here...')
    time.sleep(3)
    raise Exception('barf foo!')

if __name__ == '__main__':

    with tracker_cm('work') as something:
        try:
            logging.info('[ SOMETHING ]: {}'.format(something))
            work()
        except Exception:
            pass
        
# NOTE: 
# enter yield something
# exit exc become harder

