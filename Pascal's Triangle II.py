# https://leetcode.com/problems/pascals-triangle-ii/description/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        temp = []
        temp.append([1])
        for i in range(rowIndex):
            add_row=[1]
            for j in range(i):
                add_row.append(temp[i][j]+temp[i][j+1])
            add_row.append(1)
            temp.append(add_row)
        return temp[rowIndex]

            

