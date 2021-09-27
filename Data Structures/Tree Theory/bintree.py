import sys
print(sys.getrecursionlimit())

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, val):
        if self.data:
            if val < self.data:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.data:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.data = val
        
    def printbtree(self):
        if self.left:
            self.left.printbtree()
        print(self.data)
        if self.right:
            self.right.printbtree()

    def searchkey(self, root, val):
        
        if self.data and self.data == val:
            print ("Key is found")
            return
        elif self.left and val < self.data:
             self.left.searchkey(self.left, val)
        elif self.right and val > self.data:
             self.right.searchkey(self.right, val)
        else:
            print ("Key is not present in the tree") 
            return







root = Node(10)
root.insert(6)
root.insert(14)
root.insert(3)
root.printbtree()
root.searchkey(root, 24)
