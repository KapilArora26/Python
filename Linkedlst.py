#Basic Linked List Problem

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

    def AtBegining(self,newdata):
      NewNode = Node(newdata)
# Update the new nodes next val to existing node
      NewNode.nextval = self.headval
      self.headval = NewNode

    def AtEnd(self,newdata):
        NewNode = Node(newdata)
# Update the existing last node to point to the new node added in the end
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while (laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

    def InBetween(self, middlenode, newdata):
        if middlenode is None:
            print ("the mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middlenode.nextval
        middlenode.nextval = NewNode


    

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

#Link first node to second

list1.headval.nextval = e2

#Link second node to third

e2.nextval = e3

list1.listprint()

list1.AtBegining("Sun")
print('\n',"*******************************", '\n', "printing new row" , '\n', "******************************")
list1.listprint()

list1.AtEnd("Thu")
print('\n',"*******************************", '\n', "printing new row" , '\n', "******************************")
list1.listprint()

print('\n',"*******************************", '\n', "printing new row" , '\n', "******************************")


list1.InBetween(list1.headval.nextval,"Fri")

list1.listprint()