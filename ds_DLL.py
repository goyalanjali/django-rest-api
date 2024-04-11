class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev



class DLL:
    def __init__(self):
        self.head = None


    def insert_at_beginning(self,data):
        if self.head == None:
           node = Node(data,self.head,None)
           self.head = node
        else:
           node = Node(data,self.head,None)
           self.head.prev = node
           self.head = node     
         


    def print_forward(self):
        itr = self.head
        dllstr = ''
        while itr:
            dllstr += str(itr.data) + '-->'
            itr = itr.next

        print(dllstr)


    def print_backward(self):
      
        itr = self.head
        while itr.next: 
         #   itr.prev = itr.next.prev
            #itr.prev = itr
            itr = itr.next
           
        dllstr = ''

        #ptr = itr.prev
        while itr:
            dllstr += str(itr.data) + '<--'
            #itr.prev = itr.next.prev
            itr = itr.prev
            

        print(dllstr)     


    


    def insert_at_end(self,data):      
        if self.head is None:
            node = Node(data,None,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        node = Node(data,None,itr)
        itr.next = node  


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1

        return count    
    

    def insert_at(self,index,data):
        if index < 0 or index>=self.get_length():
            raise exception("invalid index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next,itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next    
            count += 1


    def insert_after(self,data_after,data):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data,itr.next,itr)
                itr.next = node
                break

            itr = itr.next
            


    def insert_before(self,data_before,data):
            itr = self.head
            while itr:
                if itr.data == data_before:    
                    node = Node(data,itr,itr.prev)
                    #itr.prev = node
                    itr.prev.next = node
                    break    
                 
                itr = itr.next
                
                
               # ptr = itr.prev
               #if node.next:
                #        node.next.prev = node


    def remove_at(self,index):
        if index < 0 or index>=self.get_length():
            raise exception("invalid index")
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                if itr.next:
                     itr.next.prev = itr
               
                break

        
            itr = itr.next
            count += 1


    def remove_by_value(self,data):
        itr = self.head

        while itr:
            if data == itr.next.data:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                break

            itr = itr.next        









dll = DLL()
dll.insert_at_beginning(30)
dll.insert_at_beginning(20)
dll.insert_at_end(60)
dll.insert_after(30,50)
dll.insert_before(30,40)
dll.insert_at_end(70)
dll.print_forward()
dll.remove_at(5)
dll.print_forward()
dll.insert_at(4,80)
dll.print_forward()
dll.remove_by_value(80)
dll.print_forward()
dll.insert_at_end(90)
dll.print_forward()
dll.remove_by_value(90)
dll.print_forward()
dll.insert_at(2,35)
dll.print_forward()
dll.print_backward()

print("length is",dll.get_length())

"""
dll.insert_at_end(90)
dll.print_forward()
dll.print_backward()
print("length is",dll.get_length())
#dll.insert_at(2,50)
dll.insert_after(35,50)
dll.print_forward()
dll.insert_after(50,70)
dll.insert_after(70,80)
dll.insert_after(30,35)
dll.print_forward()
dll.insert_before(35,40)
#dll.print_forward()
"""

