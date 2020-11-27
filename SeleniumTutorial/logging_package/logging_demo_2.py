import logging
import logging_package.custom_logger as cl

class LoggingDemo2():
    log = cl.customLogger(logging.DEBUG)

    def method1(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method2(self):
        m2log = cl.customLogger(logging.INFO)
        m2log.debug('debug message')
        m2log.info('info message')
        m2log.warning('warn message')
        m2log.error('error message')
        m2log.critical('critical message')

    def method3(self):
        m3log = cl.customLogger(logging.WARNING)
        m3log.debug('debug message')
        m3log.info('info message')
        m3log.warning('warn message')
        m3log.error('error message')
        m3log.critical('critical message')

demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method3()