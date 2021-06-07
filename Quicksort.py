def quicksort(arr):
    left = []
    right = []
    pivot_list = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        for i in arr:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                pivot_list.append(i)

        left = quicksort(left)
        right = quicksort(right)
        return left + pivot_list + right
