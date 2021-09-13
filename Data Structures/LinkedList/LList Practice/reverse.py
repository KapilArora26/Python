#Challenge 1: Print in reverse

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
        return

    def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
      return

    def printinreverse(self):
        var = self.headval
        
        if var.nextval is None:
            print(var.dataval)
            return None
        else:
            while var is not None:
                last = var.nextval
                if last.nextval is None:
                    print(last.dataval)
                    var.nextval = None
                    if self.printinreverse() is None:
                        return
                else:
                    var = var.nextval
            return

list1 = SLinkedList()
list1.headval = Node(1)
e2 = Node(2)
e3 = Node(3)

#Link first node to second

list1.headval.nextval = e2

print(list1.headval.nextval)
#Link second node to third

e2.nextval = e3

list1.listprint()
list1.printinreverse()