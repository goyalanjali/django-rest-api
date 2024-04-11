class Tree:

    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []


    def add_child(self,child):
        child.parent = self
        self.children.append(child)


    def print_tree(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        spaces = '  ' * level    

        print(spaces + self.data)
        if self.children:
            for val in self.children:
                  val.print_tree()
                #print(val.data)   
              



root = Tree("Electronics")  


laptop = Tree("Laptop")
laptop.add_child(Tree("mac"))
laptop.add_child(Tree("hp"))
laptop.add_child(Tree("dell"))

mobile = Tree("Mobile")
mobile.add_child(Tree("android"))
mobile.add_child(Tree("ios"))

root.add_child(laptop) 
root.add_child(mobile) 

root.print_tree()
