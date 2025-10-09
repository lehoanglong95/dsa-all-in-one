# Link: https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/description/

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        prefix_sum = [0]
        start_time = 0
        for sk in skill:
            prefix_sum.append(prefix_sum[-1] + sk) # O(n)
        ans = [0] * n

        for idx, man in enumerate(mana): # O(m)
            if idx == 0:
                ans = [man * e + start_time for e in prefix_sum[1:]] # O(n)
            else:
                start_time = ans[0]
                for idx in range(1, n):
                    start_time = max(start_time, ans[idx] - man * prefix_sum[idx])
                ans = [man * e + start_time for e in prefix_sum[1:]]

        return ans[-1]