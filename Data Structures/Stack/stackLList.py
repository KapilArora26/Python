#This  is stack implementation using linked list

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:

    def __init__(self):
        self.head = None
        return

    def push(self, data):
        var = Node(data)
        last = self.head
        self.head = var
        self.head.next = last
        return

    def pop(self):

        self.head = self.head.next
        return


    def printlist(self):

        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
        return

stck = SLinkedList()
stck.push(1)
stck.push(2)
stck.push(3)
stck.push(4)
stck.push(5)
stck.printlist()
stck.pop()
print('\n', "List after removing top element")
stck.printlist()
