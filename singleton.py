# NoneType = type(None)
# obj1 = NoneType()
# obj2 = NoneType()
# obj1 is obj2 True

#type(Ellipsis) ==  ellipsis True
#ellipsis() is ellipsis()
# import math
# print(id(math))
# print(type(math))

class Logger:
    """Creates logs for the system"""
    _file.name = logs.log
    _instance = None
    _reference_no = 0

    def __init__(self):
        raise RuntimeError('Call instance() instead!')
    @classmethod
    def instance(cls):
        cls._reference_no += 1
        if cls._instance is None:
            print("Create new instance")
            cls._instance = cls.__new__(cls)
            cls._instance._file = open(cls._filename,'w')
        return cls._instance

        # lub
        # if Logger._instance is None:
        #     pass

    def write_message(self, message):
        self._file.write(message + '\n')
        self._file.flush()

    def __delete__(self):
        type(self)._reference_no -= 1

        if not type(self)._reference_no:
            print('Closing file')
            self._file.close()


my_singleton = Logger.instance()
my_singleton2 = Logger.instance()

# my_singleton is my_singleton2 = True
# my_singleton is my_singleton3 = False

