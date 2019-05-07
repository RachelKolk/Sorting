# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO
    print("Merging ", arrA, " and ", arrB)
    for i in arrA:
        for x in arrB:
            if i > x:
                merged_arr.append(x)
                merged_arr.append(i)
            else:
                merged_arr.append(i)
                merged_arr.append(x)                
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        # 1. While your data set contains more than one item, split it in half
        #divide arr into half recursively
        print("Splitting array - length is " + str(len(arr)))
        print("Slice", arr[0:int(len(arr)//2)])
        left = merge_sort(arr[0:int(len(arr)//2)])
        print("Slice", arr[int(len(arr)//2):])
        right = merge_sort(arr[int(len(arr)//2):])
        print("Left:", left)
        print("Right:", right)
       
    # conquer using merge helper function
    if len(arr) == 1:
        return arr
    if right != None:
        if len(left) == len(right):
            arr = merge(left, right)
            return arr
    else:
        return left


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
