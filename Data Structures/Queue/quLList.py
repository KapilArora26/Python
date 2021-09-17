#Queue implementaion using link list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.head = None

    def enqueue(self, val):
        var = Node(val)

        if self.head is None:
            self.head = var
            return
        else:
            last = self.head
            while last is not None:
                if last.next is None:
                    last.next = var
                    return
                else:
                    last = last.next
        return

    def dqueue(self):
        if self.head is None:
            return "Queue is empty"
        else:
            self.head = self.head.next
            return


    def printq(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
        return

list1 = queue()
list1.enqueue(1)
list1.enqueue(2)
list1.enqueue(3)
list1.enqueue(4)
list1.printq()
list1.dqueue()
print('\n', "ELements in queue after first dqueue operation")
list1.printq()