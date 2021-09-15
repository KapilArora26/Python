#this code finds the middle node in a linked list

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:

    def __init__(self):
        self.head = None
        return

    def insert(self, data):
        
        var = Node(data)
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

    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print ("The middle element is {}".format(slow.data))
        return 

            
        
    def printlist(self):
        printval = self.head


        while printval is not None:
            print(printval.data)
            printval = printval.next
        return

list = SLinkedList()
list.insert(1)
list.insert(2)
list.insert(3)
list.insert(4)
list.printlist()
list.middle()