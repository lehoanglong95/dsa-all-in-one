def pref_sum(arr):
    n = len(arr)
    
    # to store the prefix sum
    prefix_sum = [0]

    # Adding present element with previous element
    for i in range(n):
        prefix_sum.append(prefix_sum[-1] + arr[i])
    
    return prefix_sum

def calculate_sum(pref_sum, i, j):
    return pref_sum[j + 1] - pref_sum[i]

if __name__ == "__main__":
    arr = [1, 3, 5, 7]
    prefix_sum = pref_sum(arr)
    assert calculate_sum(prefix_sum, 0, 3) == sum(arr)
    assert calculate_sum(prefix_sum, 2, 3) == 12
    assert calculate_sum(prefix_sum, 1, 2) == 8
    assert calculate_sum(prefix_sum, 0, 2) == 9