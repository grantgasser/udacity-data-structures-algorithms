## Grant Gasser
## Iterative Binary Search

import time, random

#REMEMBER: binary search assumes sorted array
def binary_search(arr, e):
    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = (first + last) // 2

        if arr[mid] == e:
            return mid
        elif arr[mid] < e:
            first = mid + 1
        else:
            last = mid - 1

    return -1

def main():
    arr = [random.randint(0, 5000000) for x in range(1, 10000000)]
    arr = sorted(arr)

    e = arr[67000]

    # time the binary search
    start = time.time()
    print 'binary: ', binary_search(arr, e) #=> close to 67000 (may have duplicates)
    end = time.time()
    print 'Binary Search:', end - start, 'seconds.\n'

    # time the linear search
    start = time.time()
    i = 0

    while i < len(arr):
        if arr[i] == e:
            print 'Linear: ', i
            break
        i += 1

    end = time.time()
    print 'Linear Search:', end - start, 'seconds.\n'

main()
