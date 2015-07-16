import logging
import traceback

logging.basicConfig(level=logging.INFO)
import time
#from trac

class TrackerCM(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        logging.info('Entering: {}'.format(self.name))
        return 'blah'

    def __exit__(self, exc_type, exc, exc_tb):
        logging.info('Exiting: {}'.format(self.name))
        if exc_type == TypeError:
            logging.info(traceback.print_tb(exc_tb))
            return True
        else:
            return False

def work():
    time.sleep(3)
    logging.info('Doing lots of work here...')
    raise TypeError('barf foo...!')


if __name__ == '__main__':

    with TrackerCM('work') as something:
        logging.info('[ SOMETHING ]: {}'.format(something))
        work()
        
        
# NOTE: 
# enter return statement
# exit with NO exc log value
# with exc and True
# with exc and False

