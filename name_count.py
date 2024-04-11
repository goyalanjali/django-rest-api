lst = []
n = int(input('ENTER A LIST OF NAMES'))
for i in range(0,n):
    ele = input()
    lst.append(ele)

#print(lst[0])
#print("helllo")

def count(lst):
    c = 0
    for i in lst:
        
        if len(i)<=5:
            pass
        else:
            c += 1
        
     #   print(i)
    return c



b = count(lst)
print(b)        
