def binary_search(arr: list[int], target: int) -> int:
    # arr must be sorted
    n = len(arr)
    l, r = 0, n - 1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid - 1 # find left
        else:
            l = mid + 1 # find right
    return -1