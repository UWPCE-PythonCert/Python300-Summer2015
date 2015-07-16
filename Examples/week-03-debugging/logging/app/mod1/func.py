import logging
func_logger = logging.getLogger('app.mod1')

def blah():
    func_logger.debug('[ FUNC1 ]')