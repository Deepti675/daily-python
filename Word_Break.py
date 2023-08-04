# https://leetcode.com/problems/word-break/description/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for w in wordDict:
                if len(w)>i:
                    continue
                if s[i-len(w):i]== w and dp[i-len(w)]:
                    dp[i]=dp[i-len(w)]
                    break
        return dp[len(s)]
      
