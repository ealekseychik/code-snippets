# Binary search implementation in Python

def binarySearch(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1
