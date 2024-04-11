pos = 0
lst = [4,3,7,6,2,9]
v = 2

def lin(lst,v):
    for i in range(0,len(lst)):
        if lst[i] == v:
            globals()['pos'] = i
            return True
        
    return False
        
if lin(lst,v):
    print("found at position", pos+1)
else:
    print("not found")            
