"""
lst_arr = [2200, 2350, 2600, 2130, 2190]
val = 0

print('extra expense in month of feb is:', lst_arr[1] - lst_arr[0])

for i in range(0,3):
    val += lst_arr[i]

print('quarterly exoense is', val)   

for i in range(0,5):
    if lst_arr[i] == 2000:
        print(true)
        break
    
print('not found')
    
lst_arr.append(1980)    
print(lst_arr)

print(lst_arr[3])
lst_arr[3] = lst_arr[3] - 2000
print(lst_arr[3])

"""

"""
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))

heros.append('black panther')
print(heros)

heros.remove('black panther')
print(heros)
heros.insert(3, 'black panther')
print(heros)

heros[1:3] = ['doctor strange']
print(heros)

heros.sort()
print(heros)

"""

n = int(input('enter a max no'))
lst = []

for i in range(1,n+1):
    if i%2 != 0:
        lst.append(i)

print(lst)        

    


    
    

