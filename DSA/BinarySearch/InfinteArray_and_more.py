# #####################################################################################################################
# #####################################################################################################################
# #####################################################################################################################


# #######################################################################
# #### 008 Position of an element in infinite length sorted array      ###
# #######################################################################


# # opposite direction of binary search
# # find the range of elements where element could lie, and then do binary search
# # finding range is log(n) and binary search is log(n)
def infinite_array(sorted_array, search_key):
    start, end = find_range(sorted_array, search_key)
    return binary_search(sorted_array, search_key, start, end)


def find_range(sorted_array, search_key):
    if sorted_array[0] == search_key:
        return 0, 0
    else:
        start = end = 1
        while sorted_array[end] < search_key:
            start, end = end + 1, end + (end - start + 1) * 2
        else:
            return start, end


def binary_search(sorted_array, search_key, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if sorted_array[mid] > search_key:
            end = mid - 1
        elif sorted_array[mid] < search_key:
            start = mid + 1
        else:
            return mid
    else:
        return -1


print("Question 8")
for i in range(-2, 10):
    print(i, infinite_array(list(range(50)), i))

# #####################################################################################################################
# #####################################################################################################################
# #####################################################################################################################


# #######################################################################
# #### 008 v2 Position of an element in infinite length sorted array      ###
# #######################################################################
def binary_search_infinte(array, search_key):
    if array[0] == search_key:
        return 0
    start = 1
    stop = 2
    while start<=stop:
        mid = start + (stop - start) // 2
        if array[mid] < search_key:
            start = mid + 1
            stop = 2 * start
        elif array[mid] > search_key:
            stop = mid - 1
        else:
            return mid
    else:
        return -1

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(10):
    print(i, binary_search_infinte(array, i))


# #####################################################################################################################
# #####################################################################################################################
# #####################################################################################################################


# #######################################################################
# #### 009 852. Peak Index in a Mountain Array    ###
# #######################################################################
# https://leetcode.com/problems/peak-index-in-a-mountain-array/

# bitonic array -> increasing and then decreasing array

def find_peak(arr):
    start = 0
    end = len(arr) - 1
    while start<end:
        mid = start + (end - start)//2
        if arr[mid] > arr[mid + 1]:
            end = mid
        elif arr[mid] < arr[mid + 1]:
            start = mid + 1
    else:
        return start

print("Question 9")
arr_list = [[0,1,0],[0,2,1,0], [0,10,5,2], [3,4,5,1], [24,69,100,99,79,78,67,36,26,19]]
for arr in arr_list:
    print(find_peak(arr))

# https://leetcode.com/problems/find-peak-element/  --medium
# https://leetcode.com/problems/find-in-mountain-array/  --hard

# #####################################################################################################################
# #####################################################################################################################
# #####################################################################################################################


# #######################################################################
# #### 010 33. Search in Rotated Sorted Array    ###
# #######################################################################

# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums, target):
    if len(nums) == 1:
        return 0 if nums[0] == target else -1
    else:
        pivot = find_pivot(nums)
        if nums[pivot] == target:
            return pivot
        else:
            target_index = binary_search(nums, target, 0, pivot)
            return binary_search(nums, target, pivot + 1, len(nums) - 1) if target_index == -1 else target_index

def find_pivot(nums):
    start = 0
    end = len(nums) - 1
    while start<end:
        mid = start + (end - start)//2
        print(start, mid, end)
        if mid<end and nums[mid] > nums[mid + 1]:
            return mid
        elif mid>start and nums[mid] < nums[mid - 1]:
            return mid - 1
        elif nums[start] > nums[mid]:
            end = mid - 1
        elif nums[start] <= nums[mid]:
            start = mid + 1
        print(start, mid, end)
    else:
        return start

def binary_search(nums, target, start, end):
    while start<=end:
        mid = start + (end - start)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    else:
        return -1

print("Question 10")
nums = [13,12]
target = 13
print(search(nums,target))

# #####################################################################################################################
# #####################################################################################################################
# #####################################################################################################################


# #######################################################################
# #### 011 How many times, the array is rotated    ###
# #######################################################################

# pivot times

def count_rotation(rotated_array):
    start = 0
    end = len(rotated_array) -1
    while start < end:
        mid = start + (end - start)//2
        if mid < end and rotated_array[mid] > rotated_array[mid + 1]:
            return mid
        elif mid > start and rotated_array[mid] < rotated_array[mid - 1]:
            return mid - 1
        elif rotated_array[mid] <= rotated_array[start]:
            end = mid - 1
        elif rotated_array[mid] > rotated_array[start]:
            start = mid + 1
    else:
        return -1


