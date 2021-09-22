class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
         self.right.printtree()           

        

    def insert(self,data):
        #Comparing the value with parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# left -> root -> right
    def inorderTraverse(self, root):
        res = []
        if root:
            res = self.inorderTraverse(root.left)
            res.append(root.data)
            res = res + self.inorderTraverse(root.right)
        return res


# root -> left -> right
    def preorderTraverse(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.inorderTraverse(root.left)
            res = res + self.inorderTraverse(root.right)
        return res


# left -> right -> root
    def postorderTraverse(self, root):
        res = []
        if root:
            res = self.inorderTraverse(root.left)
            res = res + self.inorderTraverse(root.right)
            res.append(root.data)
        return res

root = Node(10)
root.insert(6)
root.insert(14)
root.insert(3)
#root.printtree()
##Inserting into a tree
print(root.inorderTraverse(root))
print()
print(root.preorderTraverse(root))
print()
print(root.postorderTraverse(root))
