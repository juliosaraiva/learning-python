import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)

logging.debug('Log debug message')
logging.info('Log info message')
logging.warning('Log warning message')
logging.error('Log Error message')
logging.critical('Log critical message')
