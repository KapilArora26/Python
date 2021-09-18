# This code is about implementation of priority queue in puthon

class priorityq:

    def __init__(self):
        self.pq = list()

    def enqueue(self,val):
        if len(self.pq) == 0:
            self.pq.append(val)
            return
        else:
            size = len(self.pq)
            print (self.pq)
            for x in reversed(range(size-1)):
                if self.pq[x] > val:
                    temp = self.pq[x]
                    self.pq[x] = val
                    self.pq.append(temp)
                else:
                    self.pq.append(val)
            return
                    
    def dqueue(self):
        if len(self.pq) == 0:
            return "There are no elements in the queue"
        else:
            self.pq.pop(0)
            return

    def printq(self):
        if len(self.pq) == 0:
            return "There are no elements in the queue"
        else:
            for x in self.pq:
                print(x)
            return

pq = priorityq()
pq.enqueue(1)
pq.enqueue(2)
pq.enqueue(3)
pq.printq()