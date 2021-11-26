# non stable sorting algorithm
# best time is O(n^2)
# worst time is O(n^2)

def selection_sort(array):
    for i in range(len(array)):
        max_pos = find_max(array, 0, len(array) - i - 1)
        print(max_pos)
        array[max_pos], array[len(array) - i - 1] = array[len(array) - i - 1], array[max_pos]
        print(array)


def find_max(array, start_pos, end_pos):
    max_pos = start_pos
    for i in range(start_pos, end_pos):
        if array[i] < array[i + 1]:
            max_pos = i + 1
    return max_pos


array = [1,2,3,4,0]
print(array)
selection_sort(array)
print(array)
