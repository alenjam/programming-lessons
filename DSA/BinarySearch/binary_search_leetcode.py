def mySqrt(x):
    start = 0
    end = x
    while start <= end:
        mid = start + (end - start) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            start = mid + 1
        elif mid * mid > x:
            end = mid - 1
    else:
        return end


for i in range(17):
    print(i, mySqrt(i))


# rotated_array

def find_pivot(rotated_array):
    start = 0
    end = len(rotated_array) - 1
    while start <= end:
        mid = start + (end - start) // 2
        # print(start, mid, end)
        if mid < end and rotated_array[mid] > rotated_array[mid + 1]:
            return mid
        elif mid > start and rotated_array[mid] < rotated_array[mid - 1]:
            return mid
        elif rotated_array[start] > rotated_array[mid]:
            end = mid - 1
        elif rotated_array[start] < rotated_array[mid]:
            start = mid + 1
        elif start == mid:
            return -1
    # print(start, mid, end)
    else:
        return -1


def binary_search(array, start, end, target):
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    else:
        return -1


def search_rotated_array(array, target):
    pivot = find_pivot(array)
    print(f"printing the pivot: {pivot}")
    if pivot == -1:
        return binary_search(array, 0, len(array) - 1, target)
    elif array[pivot] == target:
        return pivot
    elif target >= array[0]:
        return binary_search(array, 0, pivot - 1, target)
    elif target < array[0]:
        return binary_search(array, pivot + 1, len(array) - 1, target)


print("searching in a rotated array")
nums = [9, 1, 2, 3, 4, 5, 7, 8]
target = 7
print(find_pivot(nums))
print(search_rotated_array(nums, target))


# https://leetcode.com/explore/learn/card/binary-search/126/template-ii/947/
# find first bad version
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
# your product fails the quality check. Since each version is developed based on the previous version,
# all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the
# following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to
# find the first bad version. You should minimize the number of calls to the API.

def is_bad_version(total_versions, first_bad):
    return [True if i < first_bad else False for i in range(1, total_versions + 1)]


no_of_versions = 10
first_bad_version = 10
versions = is_bad_version(no_of_versions, first_bad_version)
print(versions)

def first_bad_version(list_of_versions):
    start = 0
    end = len(list_of_versions)-1
    while start <= end:
        mid = start + (end - start) // 2
        print(start, mid, end)
        print(f"list_of_versions[{mid}] is {list_of_versions[mid]}")
        if start == mid:
            return end + 1
        if list_of_versions[mid]:
            start = mid
        else:
            end = mid - 1
        print(start, mid, end)
        print("--------------------------------------")
    return end + 1
print("printing the position of first bad version")
print(first_bad_version(versions))
