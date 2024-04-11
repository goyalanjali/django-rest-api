def bubble(elements):
    size = len(elements)
    for i in range(size-1):
        for j in range(size-1):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp




elements = [45,67,33,34,89,12]
print(elements)
bubble(elements)    
print(elements)