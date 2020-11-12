import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
            format='%(asctime)s:%(levelname)s:%(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'
            )
        logger = logging.getLogger()   
        #print(logger)
        logger.setLevel(logging.INFO)
        return logger

logs = LogGen.loggen()
logs.info("xxx")
logs.info("***** Test_001_Login *****")
#print(x)