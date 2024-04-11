
"""

def swap(start,end,elements):
    elements[start], elements[end] =   elements[end], elements[start]  


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end

elements = [45,34,21,78,47,36,25,76]
#elements = ["mona", "dhaval", "aamir", "tina", "chang"]
quick_sort(elements, 0, len(elements)-1)
print(elements)


"""
def partition(elements,start,end):
     if start < end:
        part = quick(elements,start,end)
        quick(elements,start,part-1)
        quick(elements,part+1,end)



def swap(start,end,elements):
    elements[start], elements[end] =   elements[end], elements[start]  


def quick(elements,start,end):

    pivot_index = start
    pivot = elements[pivot_index]

    #pivot_index = elements[start]
    start = pivot_index + 1 
    end  = end

   
    while start < end :
                while  start <= end and elements[start] <= pivot:
                    start += 1

                while start <= end and elements[end] > pivot:
                    end -= 1

                if start < end :
                    swap(start,end,elements)
               

    swap(pivot_index,end,elements)    

    return end 

#elements[start] < pivot:


elements = [45,34,21,78,47,36,25,76]

print(elements)
partition(elements,0,len(elements)-1 )
print(elements)



