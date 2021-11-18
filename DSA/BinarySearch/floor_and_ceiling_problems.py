# #######################################################################
# #### 004 Find Ceiling of a number in an array                       ###
# #######################################################################

## ceiling of x is the smallest element in array greater than or equal to x,
## and the floor is the greatest element smaller than or equal to x

def find_ceiling(sorted_array, search_key):
    start = 0
    end = len(sorted_array) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if search_key == sorted_array[mid]:
            return sorted_array[mid]
        elif search_key > sorted_array[mid]:
            start = mid + 1
        elif search_key < sorted_array[mid]:
            end = mid - 1
    else:
        return sorted_array[start] if start < len(sorted_array) else -1


print("Question 004")
array = [1, 3, 5, 7]
for i in range(9):
    print(i, find_ceiling(array, i))
print("------------------------------------------------------")


# #######################################################################
# #### 005 Find Floor of a number in an array                       ###
# #######################################################################

## ceiling of x is the smallest element in array greater than or equal to x,
## and the floor is the greatest element smaller than or equal to x

def find_floor(sorted_array, search_key):
    start = 0
    end = len(sorted_array) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if search_key == sorted_array[mid]:
            return sorted_array[mid]
        elif search_key > sorted_array[mid]:
            start = mid + 1
        elif search_key < sorted_array[mid]:
            end = mid - 1
    else:
        return sorted_array[end] if end >= 0 else -1


print("Question 005")
array = [1, 3, 5, 7]
for i in range(9):
    print(i, find_floor(array, i))
print("------------------------------------------------------")


# #######################################################################
# #### 006 744. Find Smallest Letter Greater Than Target              ###
# #######################################################################

# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Given a characters array letters that is sorted in non-decreasing order
# and a character target, return the smallest character in the array
# that is larger than target.
#
# Note that the letters wrap around.
#
# For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.

# # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# # Whenever we think about binary search, remember that we are reducing the search space
# # in each iteration -- >
# # like squeezing the number out of the array
# # in this case, we cant go very near to the target (need to be always greater than the target) from the
# # RHS (bigger number side), hence ord(letters[mid]) > ord(target)
# # From LHS, we can go to very near the target, hence ord(letters[mid]) <= ord(target)




def next_greatest_letter(letters, target):
    start = 0
    end = len(letters) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if ord(letters[mid]) <= ord(target):
            start = mid + 1
        elif ord(letters[mid]) > ord(target):
            end = mid - 1
    else:
        return letters[start] if start < len(letters) else letters[0]


print("Question 006")
letters = ["c", "f", "j"]
target = "j"
print(next_greatest_letter(letters, target))


# #######################################################################
# #### 007 34. Find First and Last Position of Element in Sorted Array  ###
# #######################################################################

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Given an array of integers nums sorted in non-decreasing order, find the starting and
# ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.


# if target is available
# When approaching from left,
# start will be first index of the target
# end will be element in index before the target
#
# When approaching from the right
# end will be the last index of the target
# start will be the element in index after the target

# (start,end),(nums[start], nums[end])
# left hand approaching
# right hand approaching
# 30
# [3, 8, 11, 30, 30, 30, 50, 50, 50, 52]
# ((3, 2), (30, 11))
# ((6, 5), (50, 30))
# -------------------------------------------
# 35
# [3, 8, 11, 30, 30, 30, 50, 50, 50, 52]
# ((6, 5), (50, 30))
# ((6, 5), (50, 30))
# -------------------------------------------
# 50
# [3, 8, 11, 30, 30, 30, 50, 50, 50, 52]
# ((6, 5), (50, 30))
# ((9, 8), (52, 50))
# -------------------------------------------

def find_end_pos(nums, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] <= target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
    else:
        return end if end>=0 and nums[end] == target else -1


def find_start_pos(nums, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] >= target:
            end = mid - 1
    else:
        return start if start<len(nums) and nums[start] == target else -1


def search_range(nums, target):
    start_pos = 0
    end_pos = len(nums) - 1
    if not nums:
        start_pos = -1
    else:
        start_pos = find_start_pos(nums, target, start_pos, end_pos)
    end_pos = -1 if start_pos == -1 else find_end_pos(nums, target, start_pos, end_pos)
    return [start_pos, end_pos]


print("Question 007")
nums = [8,8]
target = 8
print(search_range(nums, target))
