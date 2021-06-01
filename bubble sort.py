#Considers a list and a position z in the list
def swapper_b(lst, z):
    # if position z in the list is greater than the element to the right of z (z and the element to the right are out of order), swap the two elements to put them in order
    if lst[z] > lst[z+1]:
        b = lst[z]
        a = lst[z+1]
        lst[z] = a
        lst[z+1] = b   

#Runs one iteration of bubble sort through an entire list
def bubble_sort_iteration(lst):
    
    #use variable z initialized to 0 to increment through a list
    z=0
         
    #traverse the entire list, comparing every element to the element to the right of it via the swapper function
    while z < len(lst) - 1:
        swapper_b(lst, z)
        z += 1
    
def bubble_sort(lst):
    
    x = 0
    
    #traverse the entire list, trigger an iteration of bubble sort if any element x is out of order (greater than) with respect to the element to its right
    while x < len(lst) - 1:
        if lst[x] > lst [x+1]:
            bubble_sort_iteration(lst)
            #after a completion of bubble sort iteration, reset x to 0 
            x=0
        else:
            x += 1
    return lst
