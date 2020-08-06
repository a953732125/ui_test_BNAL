import logging.handlers
import os

logger = logging.getLogger()

log_path = './Log' + os.sep + 'log_info.log'

log_file = logging.handlers.TimedRotatingFileHandler(filename=log_path, when='midnight', interval=1
                                                     , backupCount=5, encoding='utf-8')

log_stream = logging.StreamHandler()

# 格式化字符串
fm = "%(asctime)s-%(levelname)s-[%(filename)s-%(funcName)s-%(lineno)d]-%(message)s"
# 格式化器
formatter = logging.Formatter(fmt=fm)

log_file.setFormatter(formatter)
log_stream.setFormatter(formatter)

logger.addHandler(log_file)
logger.addHandler(log_stream)
