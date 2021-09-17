# Python code for queue operation (this uses list as a data type)

class queue:

    def __init__(self):
        self.queue = list()
        return
    
    def enqueue(self, val):
        self.queue.append(val)
        return

    def dqueue(self):
        if len(self.queue) == 0:
            print ("There are no elements in the queue")
            return
        else:
            self.queue.pop(0)
            return


    def printq(self):

        if len(self.queue) == 0:
            print ("There are no elements in the queue")
            return
        else:
            for x in self.queue:
                print (x)
            return


qu = queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
qu.printq()
qu.dqueue()
print('\n', "elements in queue after for dqueue operation")
qu.printq()