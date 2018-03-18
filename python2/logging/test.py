import logging


logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ex")

logger.debug('debug message')
logger.info('info message')
#logging.debug('debug message')
