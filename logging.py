import logging

logging.basicConfig(level=logging.INFO, filename='myblog.log')

logging.info('Starting program')

logging.info('Trying to divide 1 by 0')


print 1/0

logging.info('The dicision succeeded')

logging.info('Ending program')
