# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrL, arrR ):
    elements = len( arrL ) + len( arrR )
    merged_arr = [0] * elements
    # TO-DO
    # need these so that the index range doesn't error
    arrL.append(99999999)
    arrR.append(99999999)
    l = 0
    r = 0
    for i in range(0, elements):
        if arrL[l] <= arrR[r]:
            merged_arr[i] = arrL[l]
            l += 1
        else:
            merged_arr[i] = arrR[r]
            r += 1
    print(merged_arr)                
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) > 1:
        # 1. While your data set contains more than one item, split it in half
        #divide arr into half recursively
        print("Splitting array - length is " + str(len(arr)))
        print("Slice", arr[0:int(len(arr)//2)])
        print("Slice", arr[int(len(arr)//2):])
        left = merge_sort(arr[0:int(len(arr)//2)])
        
        right = merge_sort(arr[int(len(arr)//2):])
        arr = merge(left, right)
    return arr
      

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
