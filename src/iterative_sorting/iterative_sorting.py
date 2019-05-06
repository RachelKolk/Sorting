# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # set swap_occured to default true so that the while loop fires
    swap_occured = True
    while swap_occured:
        # 1. Loop through your array
        # set swap to false, so that when swaps no longer happen the loop will break/end
        swap_occured = False
        for i in range(0, len(arr)-1):
            # create temp variable to hold item to swap
            temp = arr[i]
            # Compare each element to its neighbor
            if arr[i] > arr[i + 1]:
                # If elements in wrong position (relative to each other, swap them)
                arr[i] = arr[i+1]
                # uses the temp value to populate the i+1 index if a swapped occured
                arr[i + 1] = temp
                swap_occured = True
            i +=1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr