# comparison algorithm
# also known as sinking sort, exchange sort


# Time Complexity
# Best Case O(n)
# Worst Case O(n^2)
#     n + n-1 + n-2 + n-3 + .....

# Bubble Sort is stable Sorting Algorithm

unsorted_array = [5,4,3,2,1]
print(f"Before Sorting: {unsorted_array}")
for i in range(len(unsorted_array)-1):
    is_sorted = True
    for j in range(len(unsorted_array)-1-i):
        if unsorted_array[j]>unsorted_array[j+1]:
            unsorted_array[j], unsorted_array[j+1] = unsorted_array[j+1], unsorted_array[j]
            is_sorted = False
    if is_sorted:
        break
print(f"After Sorting: {unsorted_array}")