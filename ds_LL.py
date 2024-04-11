class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head  = node

    def print(self):
        if self.head is None:
            print("LL is empty")
            return

        itr = self.head
        llstr =  ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
            
        print(llstr)   

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)    

    def insert_values(self,data_list):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count+= 1

        return count          

    def remove_at(self,index):
        if index < 0 or index>=self.get_length():
            raise exception("invalid index")
        
        if index == 0:
          self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
               itr.next.prev = itr
               break

            itr = itr.next   
            count += 1

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
                node = Node(data,itr.next)
                itr.next = node
                break 

            itr = itr.next
            count += 1    

    def insert_after_value(self,data_after,data):
        if self.head is None:
            print("LL is empty")
            return
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data,itr.next)
                itr.next = node
                break

            itr = itr.next    

    def remove_by_value(self,data):
        if self.head is None:
            print("LL is empty")
            return
        
        itr = self.head
        count = 0
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break


            itr = itr.next
            count += 1
        

#if __name__ == '__main__':
ll = LinkedList()
#ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_end(45)
ll.insert_values(["banana", "orange","kiwi"])
ll.print()
print("length is",ll.get_length())
ll.remove_at(3)
ll.print()
ll.insert_at(3,"Avocado")
ll.insert_at(0,50)
ll.print()
ll.insert_after_value("banana","pineapple")
ll.print()
ll.insert_after_value(45,30)
ll.print()
ll.remove_by_value("pineapple")
ll.print()
ll.remove_by_value(20)
ll.print()