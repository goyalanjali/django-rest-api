class BinarySearchTree:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


    def add_child(self,value):
        if value == self.data:
            return
        
        if value < self.data:
            if self.left:
                self.left.add_child(value)
            else:
                self.left = BinarySearchTree(value)    

        if value > self.data:
            if self.right:
                self.right.add_child(value)
            else:
                self.right = BinarySearchTree(value) 
                


    def inorder_traversal(self):
        out = []

        if self.left:
            out += self.left.inorder_traversal()

        out.append(self.data)

        if self.right:
            out += self.right.inorder_traversal()

        return out    
    
 
    def search(self,val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False   

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False      




elements = [67,45,23,46,21,89,34,98,78]

root = BinarySearchTree(elements[0])

for i in range(1,len(elements)):
    root.add_child(elements[i])     

print(root.inorder_traversal())      

print(root.search(89))
