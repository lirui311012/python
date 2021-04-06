
from collections import Iterable
from collections import Iterator
import time

class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        return ClassIterator(self)

class ClassIterator(object):
    def __init__(self,obj):
        self.obj = obj
        self.current_index = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_index < len(self.obj.names):
            index = self.current_index
            self.current_index += 1
            return self.obj.names[index]
        else:
            raise StopIteration

#it = ClassIterator()
classmate = Classmate()
classmate.add("张三")
classmate.add("李四")
classmate.add("王五")

#print(isinstance(classmate,Iterable))
#print(isinstance(classmate,Iterator))
#print(isinstance(it,Iterator))
#print(isinstance(it,Iterator))
for item in classmate:
    print(item)
    time.sleep(1)