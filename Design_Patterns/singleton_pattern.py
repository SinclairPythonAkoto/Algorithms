# You are building a logging system for yoru application 
# and want to make sure there is only one instance of the 
# logger throughout the application.
# A Singleton design pattern would guarentee only one logger instance


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._log = []
        return cls._instance
    
    def log(self, message):
        self._log.append(message)
    
    def print_log(self):
        print("\n".join(self._log))


# implementation

logger1: Logger = Logger()
logger2: Logger = Logger()
print(logger1 == logger2)
logger1.log("Log message 1")
logger2.log("Log message 2")
logger1.print_log()
logger2.print_log()