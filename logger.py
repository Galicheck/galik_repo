class Logger:
    _instance = None
    _file_name = 'logs.log'
    def __new__(cls):
        if cls._instance is None:
            print('Create new instance')
            cls._instance =  super().__new__(cls)
            cls._instance._file = open(cls._file_name, 'w')

        return cls._instance

    def write_message(self,message):
        self._file.write(message + '\n')
        self._file.flush()


logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)

logger1.write_message("message 1")