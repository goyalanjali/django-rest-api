def merge_sort(elements):
    if len(elements) <= 1:
        return elements


    mid = len(elements) // 2
    left = elements[:mid]
    right = elements[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)


def merge(left,right):
    new_list = []
    i,j = 0,0

    while i< len(left) and j < len(right):
        if left[i] < right[j]:
            new_list.append(left[i])
            i += 1
        else:
            new_list.append(right[j])
            j += 1

    new_list.extend(left[i:])  
    new_list.extend(right[j:])        

    return new_list





elements = [45,32,46,78,24,79,20] 
lst = []   
lst = merge_sort(elements)
print(lst)