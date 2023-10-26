class Solution:
    def equalPartition(self, n, arr):
        TotalSum = sum(arr)
        if TotalSum % 2 != 0:
            return 0  
        
        t = [[False for _ in range(TotalSum//2 + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            t[i][0] = True  
        
        for j in range(1, TotalSum//2 + 1):
            t[0][j] = False  

        for i in range(1, n + 1):
            for j in range(1, TotalSum//2 + 1):
                if arr[i - 1] <= j:
                    t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
                else:
                    t[i][j] = t[i - 1][j]

        if t[n][TotalSum//2] == True:
            return 1  
        else:
            return 0
