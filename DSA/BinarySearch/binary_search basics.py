# #######################################################################
# #### 001 Binary Search without Recursion                            ###
# #######################################################################
def binary_search_without_recursion(sorted_array, search_key):
    start = 0
    end = len(sorted_array) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if search_key == sorted_array[mid]:
            return mid
        elif search_key > sorted_array[mid]:
            start = mid + 1
        elif search_key < sorted_array[mid]:
            end = mid - 1
    else:
        return -1


print("Question 001")
array = [1, 2, 3, 4]
for i in range(6):
    print(i, binary_search_without_recursion(array, i))
print("------------------------------------------------------")


# #######################################################################
# #### 002 Binary Search with Recursion                            ###
# #######################################################################

def binary_search_with_recursion(sorted_array, search_key):
    start = 0
    end = len(sorted_array) - 1
    return helper(sorted_array, search_key, start, end)


def helper(sorted_array, search_key, start, end):
    mid = start + (end - start) // 2
    if start > end:
        return -1
    elif sorted_array[mid] == search_key:
        return mid
    elif sorted_array[mid] > search_key:
        end = mid - 1
    elif sorted_array[mid] < search_key:
        start = mid + 1
    return helper(sorted_array, search_key, start, end)


print("Question 002")
array = [1, 2, 3, 4]
for i in range(6):
    print(i, binary_search_with_recursion(array, i))
print("------------------------------------------------------")


# #######################################################################
# #### 003 Binary Search with reverse sorted array                    ###
# #######################################################################

def binary_search_reverse_sorted_array(sorted_array, search_key):
    start = 0
    end = len(sorted_array) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if search_key == sorted_array[mid]:
            return mid
        elif search_key < sorted_array[mid]:
            start = mid + 1
        elif search_key > sorted_array[mid]:
            end = mid - 1
    else:
        return -1


print("Question 003")
array = [4, 3, 2, 1]
for i in range(5, -1, -1):
    print(i, binary_search_reverse_sorted_array(array, i))
print("------------------------------------------------------")
