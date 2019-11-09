import sys
import datetime


class Logger:
    def __init__(self, output_file=sys.stdout, loglevel=1):
        self.logfile = output_file

        # Уровни логирования (например, уровень стоит 2, значит 1 и 0 не выводим)
        self.DEBUG = 0
        self.INFO = 1
        self.WARNING = 2
        self.ERROR = 3
        self.CRITICAL = 4
        self.FATAL = 5

        self.loglevel = loglevel

    def log(self, level, msg):
        strlevel = ['\033[37mDEBUG   \033[00m', '\033[01mINFO    \033[00m', '\033[01;33mWARNING \033[00m',
                    '\033[31mERROR   \033[00m', '\033[41mCRITICAL\033[00m', '\033[01;31mFATAL   \033[00m']
        if level >= self.loglevel:
            self.logfile.write(f'{datetime.datetime.now()} [{strlevel[level]}] {msg}\n')


# logger = Logger(0)
# logger.log('Hello!', logger.DEBUG)
# logger.log('Connection successful!', logger.INFO)
# logger.log('What?', logger.WARNING)
# logger.log('Error(', logger.ERROR)
# logger.log('Fuc&^Q*&Q$*Q!!!!!', logger.CRITICAL)
# logger.log('I can`t help you...', logger.FATAL)
