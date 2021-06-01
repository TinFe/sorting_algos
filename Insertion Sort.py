# considers a list and an element in that list at index z
def swapper_i(lst,z):

    #Loop: if element z is larger than the element to its right (out of order), move element z one to the left.
    while lst[z]>lst[z+1] and z >= 0:
        a = lst[z]
        b = lst[z+1]
        lst[z] = b
        lst[z+1] = a
        z-=1
  

def insertion_sort(lst):

    z = 0
    
    #traverse the entire list from left to right.
    while z < len(lst) - 1:
        #if element z is out of order with respect to the element to its right, run an iteration of the swap loop at index z
        if lst[z]>lst[z+1]:
            swapper_i(lst,z)
            z += 1
        else:
            #as the list is traversed accross every element to the left of z will always be in order
            z+=1


    return lst



