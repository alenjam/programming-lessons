# when ever, question comes related to a continuous series, cycli sort should be the first to come into our mind
# https://leetcode.com/problems/missing-number/
# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.


# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# 448. Find All Numbers Disappeared in an Array
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in
# the range [1, n] that do not appear in nums.

num_list = [4, 3, 2, 7, 8, 2, 7, 1]


def find_disappeared_numbers(nums):
    for i in range(len(nums)):
        while nums[i] != (i + 1):
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            if nums[nums[i] - 1] == nums[i]:
                break
    disappearing_numbers = [i + 1 for i in range(len(nums)) if nums[i] != i + 1]
    return disappearing_numbers


print(num_list)
print(find_disappeared_numbers(num_list))


# https://leetcode.com/problems/find-the-duplicate-number/
# 287. Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers
# where each integer is in the
# range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only
# constant extra space.


def find_duplicate(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            if nums[i] == nums[nums[i] - 1]:
                break
    for j in range(len(nums)):
        if nums[j] != j + 1:
            return nums[j]


nums_list = [1, 2, 3, 5, 4, 1, 1]
print(nums_list)
print(find_duplicate(nums_list))

# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Given an integer array nums of length n where all the integers of nums are in the
# range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
#
# You must write an algorithm that runs in O(n) time and uses only constant extra space.

nums = [1, 1, 2]
print(nums)


def find_duplicates(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            if nums[i] == nums[nums[i] - 1]:
                break
    duplicates = []
    for j in range(len(nums)):
        if nums[j] != j + 1:
            duplicates.append(nums[j])
    return duplicates


# https://leetcode.com/problems/set-mismatch/
# 645. Set Mismatch
# You have a set of integers s, which originally contains all the numbers from 1 to n.
# Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
# which results in repetition of one number and loss of another number.
#
# You are given an integer array nums representing the data status of this set after the error.
#
# Find the number that occurs twice and the number that is missing and return them in the form of an array.

def find_error_nums(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            if nums[i] == nums[nums[i] - 1]:
                break

    for j in nums:
        if nums[j] != j + 1:
            return [nums[j], j + 1]


nums = [1, 1]
print(find_error_nums(nums))


# https://leetcode.com/problems/first-missing-positive/
# 41. First Missing Positive
# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

def first_missing_positive(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1 and nums[i]<len(nums) and nums[i]>0:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            if (nums[i] < 1):
                break
    print(nums)
    for j in range(len(nums)):
        if nums[j] != j + 1:
            return (j + 1)
    else:
        return nums[j] + 1


nums = [1,2,3]
print(nums)
print(first_missing_positive(nums))
