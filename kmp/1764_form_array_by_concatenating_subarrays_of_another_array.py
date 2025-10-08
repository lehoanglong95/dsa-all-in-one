# Link: https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/description/

import bisect

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        idxs = [self.kmp(group, nums) for group in groups]
        if len(idxs[0]) == 0:
            return False

        pre_idx = idxs[0][0]
        for i in range(1, len(idxs)):
            next_idx = bisect.bisect_left(idxs[i], pre_idx)
            if next_idx == len(idxs[i]) or pre_idx + len(groups[i-1]) > idxs[i][next_idx]:
                return False
            pre_idx = idxs[i][next_idx]

        
        return True
        

    def kmp(self, pattern, num):
        num = pattern + ["#"] + num
        m = len(pattern)
        n = len(num)
        kmp = [0] * n
        ans = []

        for i in range(1, n):
            j = kmp[i-1]
            while j > 0 and num[i] != num[j]:
                j = kmp[j-1]
            if num[i] == num[j]:
                j += 1
            kmp[i] = j
            if j == m:
                ans.append(i - 2 * m)

        return ans