# Link: https://leetcode.com/problems/avoid-flood-in-the-city/description/

from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        lakes = defaultdict(int)
        dry_days = SortedList()
        times = defaultdict(int)
        ans = [1] * n

        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.add(i)
            else:
                ans[i] = -1
                lakes[lake] += 1
                if lakes[lake] > 1:
                    last_time = times[lake]
                    idx = dry_days.bisect(last_time)
                    if idx == len(dry_days):
                        return []
                    ans[dry_days[idx]] = lake
                    dry_days.discard(dry_days[idx])
                times[lake] = i
        return ans