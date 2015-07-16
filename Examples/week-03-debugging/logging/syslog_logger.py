import logging
import logging.handlers

# create logger
logger = logging.getLogger('syslog_example')
logger.setLevel(logging.DEBUG)

# create syslog handler and set level to debug
# make sure address is pointing to the syslog socket
handler = logging.handlers.SysLogHandler(address='/dev/log')
handler.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to handler
handler.setFormatter(formatter)

# add handler to logger
logger.addHandler(handler)

if __name__ == '__main__':
    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')
