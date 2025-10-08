# Link: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=daily-question&envId=2025-10-08

import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        ans = []

        for spell in spells:
            if success % spell == 0:
                remain = (success // spell)
            else:
                remain = (success // spell) + 1
            ans.append(m - bisect.bisect_left(potions, remain))

        return ans