# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/?envType=daily-question&envId=2023-09-11
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        grups = {}
        res = []
        for i, s in enumerate(groupSizes):
            if s not in grups:
                grups[s]=[]
            grups[s].append(i)

            if len(grups[s]) == s:
                res.append(grups[s])
                grups[s]=[]

        return res
        
