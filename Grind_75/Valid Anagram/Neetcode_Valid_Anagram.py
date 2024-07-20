# Solution 1
from typing import Counter
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    # Cheating one line
    return Counter(s) == Counter(t)

# Solution 1 (explicit)
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:

    if len(s) == len(t):
      return False

    countS, countT = {}, {}
    for i in range(len(s)):
      countS[s[i]] = 1 + countS.get(s[i], 0)
      countT[t[i]] = 1 + countS.get(t[i], 0)

    for c in countS:
      if countS[c] != countT.get(c, 0):
        return False

    return True

#Solution 2 - Sorting
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

"""
For Time Complexity
Worst case - O(N^2)
Avg case - O(Nlog N)

For Space Complexity
O(N) or O(1). Most interviewers assume O(1).
"""