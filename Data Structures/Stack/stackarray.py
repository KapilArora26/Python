#This  is stack implementation using array

from array import *


class sarray:

    def __init__(self):
        self.arr = array('i', [])
        return None
    
    def push(self, data):
        self.arr.insert(0, data)
        return None
    
    def pop(self):
        size = len(self.arr)
        if size == 0:
            return "There is no element in the stack"
        else:
            self.arr.pop(0)
            return None

    def printarr(self):
        for x in self.arr:
            print (x)
        return



arr = sarray()
arr.push(1)
arr.push(2)
arr.push(3)
arr.printarr()
arr.pop()
print('\n', "Values in stack after first pop")
arr.printarr()
arr.pop()
print('\n', "values in stack after 2nd pop")
arr.printarr()

