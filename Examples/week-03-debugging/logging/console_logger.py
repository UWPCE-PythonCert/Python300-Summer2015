import logging

# create logger
logger = logging.getLogger('console_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to handler
handler.setFormatter(formatter)

# add handler to logger
logger.addHandler(handler)

if __name__  == '__main__':
    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')
