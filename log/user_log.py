import logging
import os
import datetime


class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 控制台输出日志
        # consle = logging.StreamHandler()
        # logger.addHandler(consle)


        base_dir = os.path.dirname(os.path.abspath(__file__))  # 获取当前项目的路径
        log_dir = os.path.join(base_dir, 'logs')
        log_file = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
        log_name = log_dir+'/'+log_file
        # 文件输出日志
        self.file_handle = logging.FileHandler(log_name)
        formatter = logging.Formatter('%(asctime)s %(filename)s --> %(funcName)s %(levelno)s: %(levelname)s --> %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ == '__main__':
    log = UserLog()
    log.get_log().debug('222')
