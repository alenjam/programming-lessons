# for sorting a series of numbers
# 1-N where all numbers are present once

array = [4,3,2,7,8,2,3,1]

i = 0
print(array)
for i in range(len(array)):
    print(f"--------{i}---------")
    while array[i] != i + 1:
        array[array[i] - 1], array[i] = array[i], array[array[i] - 1]
        print(array)

print(array)