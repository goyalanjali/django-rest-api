pos = 0
lst = [2,4,8,45,67,78,90]
v = 78


def bin(lst, v):
    l = 0
    u = len(lst) - 1
    for i in lst:    # while l <= u: , we can use this as well
        mid = (l+u) // 2

        if lst[mid] == v:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < v:
                l = mid
            else:
                u = mid    
    
    return False

if bin(lst, v):
    print("found at position", pos+1)
else:
    print("not found")    

        

