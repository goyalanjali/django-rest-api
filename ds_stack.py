from collections import deque

# instead of array we use deque here for putting data for stack, deque provide features like append, etc.

class stack:

    def __init__(self):
        self.container = deque()


    def push(self,val):
        self.container.append(val)


    def pop(self):
        return self.container.pop()    
    

    def size(self):
        return len(self.container)
    

    def peek(self):
        return self.container[-1]
    

    def is_empty(self):
        return len(self.container)==0
    
    
    def reverse_string(self,data):
        for ch in data:
            st.push(ch)

        rstr = ''
      
        while st.size()!=0:
            rstr += st.pop()

        return rstr  
    

    def balance(self,data):
        for ch in data:
            if ch =='(' or ch =='[' or ch =='{':
                st.push(ch)
             
            if ch ==  ')' or ch ==']' or ch =='}':
                if st.size() == 0:
                    return False
                if ch == ')' and st.pop() !='(':
                    return False
                elif ch == ']' and st.pop() !='[':
                    return False
                elif ch == '}' and st.pop() !='{':
                    return False
            
        return True
                
           # else:
               # continue       


            

            

    


        #print(self.container)  
#statement = input('enter a string to reverse')

st = stack()
#st.container = deque()  
output = st.reverse_string("my name is anjali")
print(output)
out = st.balance("[a+b]*(x+2y)*{gg+kk}")
print(out)
out = st.balance("))")
print(out)
st.push(4)   
st.push(43) 
st.push(47) 
print(st.peek())  
print(st.size())





"""
s = deque()
dir(s)
s.append(90)
s.append(78)
s.append(89)
s.append(56)
print(s)
s.pop()
print(s)
s.pop()
print(s)
"""

"""
stac = []
stac.append(32)
stac.append(43)
stac.append(78)
stac.append(67)

print(stac)
stac.pop()
print(stac)
stac.pop()
print(stac)
"""

# deque -> 'deck' -> double ended queue(doubly link list)