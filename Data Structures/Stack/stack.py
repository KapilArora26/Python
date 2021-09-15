class stack:

    def __init__(self):
        self.stack = []

    def add(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    
    def peek(self):
        return self.stack[-1]

    def pop(self):
        if len(self.stack) == 0:
            return ("No element in the stack")
        else:
            return self.stack.pop()


astack = stack()
astack.add("Mon")
astack.add("Tue")
astack.add("Wed")
print(astack.peek())
astack.add("Thu")
print(astack.peek())

astack.pop()
print(astack.peek())
