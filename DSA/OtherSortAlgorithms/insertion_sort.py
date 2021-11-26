# stable sort algorithm
# worst case - O(n^2)
# best case - O(n)
# better than bubble sort, lesser number of swaps if the sub - array is sorted
# used for smaller values of N
# best when array is partially sorted
# takes part in hybrid sorting algorithms


array = [5,4,3,2,1]


# below program is doing insert at a position and delete... Completely inefficient.
# Insertion sort mentioned at the end is the correct one
def insertion_sort_max_element(array):
    for i in range(1, len(array)):
        final_element = array[len(array)-1]
        for j in range(i):
            if array[j]>final_element:
                array.insert(j, final_element)
                array.pop(len(array)-1)



def insertion_sort_reverse_sorted_bestcase(array):
    for i in range(1, len(array)):
        pivot_element = array[i]
        print(i, pivot_element)
        for j in range(i):
            if array[j] > pivot_element:
                array.insert(j, pivot_element)
                array.pop(i + 1)
                break
            print(array)

print(array)
insertion_sort_reverse_sorted_bestcase(array)
print(array)


array = [5,4,3,2,1]
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in reversed(range(i)):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            else:
                break
        print(array)

print(array)
insertion_sort(array)
print(array)


