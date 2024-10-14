import logging
logging.basicConfig(filename="GLOBAL_LOG.log", 
                    format='%(asctime)s %(message)s', 
                    datefmt='%m/%d/%Y %I:%M:%S %p')
class Log:

    def registerInfo(msg):
        logging.info(msg)

    def registerWarning(warningMsg):
        logging.warning(warningMsg)

    def registerError(errorMsg):
        logging.error(errorMsg)

    def registerCritical(criticalMsg):
        logging.critical(criticalMsg)    