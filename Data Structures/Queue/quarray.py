from array import *

class quarray:

    def __init__(self):
        self.arr = array('i', [])
        return None

    def enqueue(self,val):
        self.arr.append(val)
        return

    def dqueue(self):
        if len(self.arr) == 0:
            return "There are no elements left in the queue for dqueue operation"
        else:
            self.arr.pop(0)
            return

    def printq(self):
        if len(self.arr) == 0:
            return "There are no elements left in the queue"
        else:
            for x in self.arr:
                print(x)
            return

val = quarray()
val.enqueue(1)
val.enqueue(2)
val.enqueue(3)
val.enqueue(4)
val.printq()
val.dqueue()
print('\n', "Elements left in the queue after first dqueue operation")
val.printq()