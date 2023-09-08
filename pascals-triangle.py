# https://leetcode.com/problems/pascals-triangle/description/?envType=daily-question&envId=2023-09-08

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        temp = []
        temp.append([1])
        for i in range(numRows-1):
            add_row = [1]
            for j in range(i):
                add_row.append(temp[i][j]+temp[i][j+1])
            
            add_row.append(1)
            temp.append(add_row)
        
        return temp
        
