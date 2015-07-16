import logging
from console_logger import logger
logger.setLevel(logging.CRITICAL)

if __name__ == '__main__':
    logger.debug( "should not show up" )
    logger.info( "should not show up" )
    logger.warn( "should not show up" )
    logger.error( "should not show up" )
    logger.critical( "kaboom!" )


