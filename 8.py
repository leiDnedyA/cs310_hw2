def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def _quicksort(arr, l, r):
    if l < r:
        pivot = partition(arr, l, r)
        _quicksort(arr, l, pivot - 1)
        _quicksort(arr, pivot + 1, r)

def quicksort(arr):
    _quicksort(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
    quicksort(arr)
    print(arr)
