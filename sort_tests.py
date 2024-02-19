import copy
import random
import matplotlib.pyplot as plt
from timeit import default_timer as timer

# my implementation of merge sort
def insertion_sort(array):
    n = len(array)

    if n <= 1:
        return

    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key


# merge sort implemented from https://www.scaler.com/topics/merge-sort-in-python/
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0

        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1

            else:
                array[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

mergetimes = []
insertiontimes = []

for i in range(100):

    randomlist = random.sample(range(1, 10000), i)
    randomlist2 = copy.deepcopy(randomlist)

    startinsert = timer()
    insertion_sort(randomlist)
    endinsert = timer()
    insertiontimes.append(endinsert - startinsert)

    startmerge = timer()
    merge_sort(randomlist2)
    endmerge = timer()
    mergetimes.append(endmerge - startmerge)

plt.plot(mergetimes, 'g', insertiontimes, 'r')
plt.show()

print("merge times: ", mergetimes[60:99])
print("insertion times: ", insertiontimes[60:99])

# randomlist = random.sample(range(1, 10000), 80)
# randomlist2 = copy.deepcopy(randomlist)
# randomlist3 = copy.deepcopy(randomlist2)
#
# completion_time_insert = 0
# for i in range(1000):
#     startinsert = timer()
#     insertion_sort(randomlist)
#     endinsert = timer()
#     completion_time_insert += (endinsert - startinsert)
#
#     randomlist = randomlist2
#
# print("completion time for insertion sort, size 80 (*1000): ", completion_time_insert)
#
# completion_time_merge = 0
# for i in range(1000):
#     startmerge = timer()
#     merge_sort(randomlist2)
#     endmerge = timer()
#     completion_time_merge += (endmerge - startmerge)
#
#     randomlist2 = randomlist3
#
# print("completion time for merge sort, size 80 (*1000): ", completion_time_merge)