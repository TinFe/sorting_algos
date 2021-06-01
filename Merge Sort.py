
#convert input list into a list of lists of 2 numbers (with one list of one number if input contains an odd number of items) to be sorted later. 
def initial_divide(lst):
#set an index variable to 0
    z = 0
    #create empty output list
    out = []
    #traverse the input list
    while z < len(lst) - 1:
        #append each item of input as a new array in the output
        out.append([lst[z]])
        z += 1
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
    lst = initial_divide(lst)
    lst = final_col(lst)
    return lst




 
