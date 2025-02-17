'''
time complexity: O(n^2)
space complexity: O(n^2)
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
    
        for i in range(0,numRows):
            temp = [None for j in range(i+1)]

            if(len(ans)==0):
                temp[0]=1
                ans.append(temp)
                continue


            #1   1,1
            temp[0] = 1
            temp[-1] = 1
            for k in range(1,len(temp)-1):
                temp[k] = ans[i-1][k-1] + ans[i-1][k]

            ans.append(temp)
        return ans
