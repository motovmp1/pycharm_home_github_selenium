import logging

# the most low level is debug stage

# time:      level:     message:
logging.basicConfig(filename="test.txt", format='%(asctime)s:,'
                                                ' %(levelname)s:,'
                                                ' %(message)s:',
                    level=logging.DEBUG)

logger = logging.getLogger()
logger.setLevel(logging.WARNING)


# This is need to be set
logger.debug("This is a debug message")
logger.info("This is a info message")

# this is default system
logger.warning("This is a warning message")
logger.error("This is a error message")
logger.critical("This is a critical message")
