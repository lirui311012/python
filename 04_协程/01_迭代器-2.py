
from collections import Iterable
from collections import Iterator
import time

class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_index = 0

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.names):
            index = self.current_index
            self.current_index += 1
            return self.names[index]
        else:
            raise StopIteration

#it = ClassIterator()
classmate = Classmate()
classmate.add("张三")
classmate.add("李四")
classmate.add("王五")

for item in classmate:
    print(item)
    time.sleep(1)