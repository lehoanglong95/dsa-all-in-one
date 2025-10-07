from bisect import bisect_left

2,3,3,2,4
removes = [3,3]
stack = [2,2,4]

def findUnsortedSubarray(nums: list[int]) -> int:
    n = len(nums)
    last_oc = dict()
    for i, val in enumerate(nums):
        last_oc[val] = i
    removes = []
    inc_stack = []

    for i in range(n):
        while inc_stack and nums[inc_stack[-1]] > nums[i]:
            removes.append(inc_stack.pop())
        inc_stack.append(i)

    if not removes:
        return 0

    left_idx = min(removes)
    max_removes = max([nums[i] for i in removes])
    inc_stack_value = [nums[i] for i in inc_stack]
    right_idx = last_oc[inc_stack_value[bisect_left(inc_stack_value, max_removes) - 1]]

    return right_idx - left_idx + 1

print(findUnsortedSubarray([2, 3, 3, 2, 4]))