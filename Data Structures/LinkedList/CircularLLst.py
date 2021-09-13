#Circular Linked List

class Node:
    def __init__(self, dataval):
        self.datav = dataval
        self.next = None

class CLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, dataval):
        var = Node(dataval)
        var.next = self.head
        #print("Curr Value is {} and next value is {}".format(var.datav,var.next))
        if self.head is None:
            self.head = var
            return
        else:
            start = self.head
            while start is not None:
                if start.next is None:
                    start.next = var 
                    return
                elif start.next == self.head:
                     start.next = var
                     return   
                else:
                    print("Next value is {}".format(start.next))
                    start = start.next
        return


    def printlist(self):
        printval = self.head
        while printval is not None:
            print (printval.datav)
            printval = printval.next
            if printval == self.head:
                break
           


list = CLinkedList()
list.insert(1)
list.insert(2)
list.insert(3)
list.printlist()






        
