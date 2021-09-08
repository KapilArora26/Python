#Double Linked List

class Node:

    def __init__(self, dataval):
        self.data = dataval
        self.next = None
        self.previous = None
    
class DLinkedList:

    def __init__(self):
        self.head = None

    
    def printfwdlist(self):
        
        printval = self.head 
        while (printval is not None):
            print(printval.data)
            printval = printval.next

    def delekey(self, dataval):

        srchval = self.head
        if (srchval.data == dataval and srchval.previous is None):
            self.head = srchval.next
            return
        
        while (srchval is not None):
            
            if (srchval.data == dataval and srchval is not None):
                self.head.next = srchval.next
                print ("Found the {} and deleted".format(dataval))
                return
            srchval = srchval.next
        
        print ("Key not found in the list")
        return




    

    
list1 = DLinkedList()
list1.head = Node(1)

val2 = Node(2)
val3 = Node(3)
#LInking the list

list1.head.next = val2
val2.previous = list1.head
val2.next = val3
val3.previous = val2
 
list1.printfwdlist()

list1.delekey(7)
print('\n\n\n\n')
list1.printfwdlist()




        