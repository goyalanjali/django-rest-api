
def insert_sort(elements):
    n = len(elements)

    for i in range(1,n):
        key = elements[i]
        j = i-1

        while j >= 0 and key < elements[j]:
            elements[j+1] = elements[j]
            j = j-1

        elements[j+1] = key    


elements = [54,35,2,4,67,89]
insert_sort(elements)
print(elements)