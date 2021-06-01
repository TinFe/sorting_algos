import time
import math
while True:

#----------------------------------------------------------------------------------------------------------------------------------------#
    #Bubble Sort#
#----------------------------------------------------------------------------------------------------------------------------------------#

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




#----------------------------------------------------------------------------------------------------------------------------------------#
    #Insertion Sort#
#----------------------------------------------------------------------------------------------------------------------------------------#

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





#----------------------------------------------------------------------------------------------------------------------------------------#
    #Merge Sort#
#----------------------------------------------------------------------------------------------------------------------------------------#


    #convert input list into a list of lists of 2 numbers (with one list of one number if input contains an odd number of items) to be sorted later. 
    def pair_sorter(lst):
        #set an index variable to 0
        z = 0
        #create empty output list
        out = []
        #check if input contains odd number of elements
        if len(lst) % 2 != 0:
            #since input contains odd number of items, one item of the output must contain one element rather than 2
            out.append([lst[0]])
            z = 1
        #loop through every other item of input list
        while z < len(lst) - 1:
            #append lists to the output list
            out.append([lst[z],lst[z+1]])
            z += 2
        return out



    #put every individual list in order
    def initial_sort(lst):
        out = []
        # if the first item of the list contains one item e.g. [2], pop that off the list and append it to the output
        if len(lst[0]) == 1:
            out.append(lst.pop(0))
            
        for i in lst:
            #pair is already in order
            if i[0] < i[1]:
                out.append(i)
            #pair is not in order so we reverse it
            if i[0] > i[1]:
                b = i[0]
                a = i[1]
                out.append([a,b])
        return out



    #collates two sorted lists into one sorted list
    def collate(lst0,lst1):
        out = []
        # set variables x and y = to 0. x will be a counter for lst0 and y will be a counter for lst1.
        x = 0
        y = 0
        #initiate a loop. the loop will break when lst0 and lst1 have been iterated through
        while x < len(lst0) or y < len(lst1):
            
            #if lst0 has been fully iterated through, simply add the rest of lst1 to the output (or vice versa)
            if x > len(lst0) - 1:
                out.append(lst1[y])
                y += 1
            elif y > len(lst1) - 1:
                out.append(lst0[x])
                x += 1       

            #if x and y are equal, append x and y to output
            elif lst0[x] == lst1[y]:
                out.append(lst0[x])
                out.append(lst1[y])
                x+=1
                y+=1
            #if x is greater than y, append y to output
            elif lst0[x] > lst1[y]:
                out.append(lst1[y])
                y += 1
            #if x is less than y, append x to output
            elif lst0[x] < lst1[y]:
                out.append(lst0[x])
                x += 1


        return out

    #takes a list of any number of sorted lists, collates them all together and returns one sorted list.
    def final_col(lst):
    
        res = lst
        out = []
        #variable used to increment through the list
        z = 0

        #initiate an infinite loop (loop will break when the list has been fully collated)
        while True:
        
            #begin to traverse accross the res variable
            while z < len(res) -1 :
            
                #because we are traversing through the res variable in increments of 2, the res variable must always contain an even number of elements.
                #if res variable contains an odd number of elements, the first two items are collated together and the res variable now contains an even number of elements.
                if len(res) % 2 != 0:
                    res[0] = collate(res[0],res[1])
                    del res[1]
               
            
                out.append(collate(res[z],res[z+1]))
                z += 2
            #after res has been iterated through, it gets set = to out
            res = out
            #incrementer reset to 0
            z = 0
            #if the length of output = 1, that means we are finished sorting and return the output
            if len(out) == 1:
                return out[0]
            
            out = []
        

    

        


    def merge_sort(lst):
        lst = pair_sorter(lst)
        lst = initial_sort(lst)
        lst = final_col(lst)
        return lst




 
#----------------------------------------------------------------------------------------------------------------------------------------#
    #Random list Generator#
#----------------------------------------------------------------------------------------------------------------------------------------#
    def rand_list_generator(item_lower_bound, item_upper_bound, list_len):
        import random
        lst = []
        while len(lst) < list_len:
            lst.append(random.randint(item_lower_bound,item_upper_bound))
        return lst





#----------------------------------------------------------------------------------------------------------------------------------------#
    #Binary Search algorithm#
#----------------------------------------------------------------------------------------------------------------------------------------#
    def binary_search(lst, target):

        minm = 0
        mid = math.floor(len(lst)/2)
        maxm = len(lst)-1

        while mid < maxm:

            if lst[mid] == target:
                return mid
            
            if lst[mid] > target:
                maxm = mid
                mid = math.floor(maxm/2)

            if lst[mid] < target:
                minm = mid
                mid = math.ceil((maxm - minm)/2) + mid
        
        return "target not found"


    


    

    a = 0
    print("type a big number")
    b = int(input())
    print("Length of list =")
    c = int(input())

    print("list:")


    lst = rand_list_generator(a,b,c)
    print(lst)
    print("insertion, bubble, tim, insertion 2, or merge sort (i/b/t/i2/m)?")
    inpt = input()
    
    if inpt == 'i2':
        start = time.perf_counter()
        lst = insertion_sort2(lst)
        elapsed = time.perf_counter() - start    
    
    if inpt == "i":

        start = time.perf_counter()
        insertion_sort(lst)
        elapsed = time.perf_counter() - start    

    if inpt == "b":
        start = time.perf_counter()
        bubble_sort(lst)
        elapsed = time.perf_counter() - start

    if inpt == "t":
        start = time.perf_counter()
        sorted(lst)
        elapsed = time.perf_counter() - start
    if inpt == 'm':
        start = time.perf_counter()
        lst = merge_sort(lst)
        elapsed = time.perf_counter() - start



    print(lst)
    print('Elapsed %.3f seconds.' % elapsed)
        
    
    
    

    
 
    
    print("enter value to search for")
    target = int(input())

    print("index =")
    print(binary_search(lst, target))

    print('press enter to run again')

    input()


