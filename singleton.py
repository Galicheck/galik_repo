NoneType = type(None)
obj1 = NoneType()
obj2 = NoneType()
# obj1 is obj2 True

#type(Ellipsis) ==  ellipsis True
#ellipsis() is ellipsis()
import math
print(id(math))
print(type(math))

class Logger:
    """Creates logs for the system"""
    _instance = None
    @staticmethod
    def instance():
