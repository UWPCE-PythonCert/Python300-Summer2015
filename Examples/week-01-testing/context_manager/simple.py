import logging
logging.basicConfig(level=logging.INFO)
import time

class TrackerCM(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        logging.info('Entering: {}'.format(self.name))

    def __exit__(self, exc_type, exc, exc_tb):
        logging.info('Exiting: {}'.format(self.name))

def work():
    logging.info('Doing lots of work here...')
    time.sleep(3)

if __name__ == '__main__':
    with TrackerCM('work') as something:
        logging.info('[ SOMETHING ]: {}'.format(something))
        work()
        
        
# NOTE: 
# enter return statement
# exit with NO exc log value
# with exc and True
# with exc and False

