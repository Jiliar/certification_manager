import logging
from app.utils.error import Error
from app.utils.config import Config as config
from datetime import datetime

class Log():
    
    def init_log_config():
        current_datetime = datetime.now()
        logging.basicConfig(filename=config.get_param('paths','logs'), level=logging.INFO)
        try:
            banner_log = open(config.get_param('paths','banner'), "r")
            file_log = open(config.get_param('paths','logs'), "a")
            file_log.write(banner_log.read())
            file_log.write("Execution: "+current_datetime.strftime("%c")+"\n")
            file_log.close()
            banner_log.close()
        except Exception as e:
            logging.error("init_log_config(): {0} - Details: {1}".format(Error.E001.value, str(e)))
        return logging