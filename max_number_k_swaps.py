import copy
import sys 

class Solution:
    
    def setAns(self, ans, s):
        for i in range(len(s)):
            if int(ans[i]) > int(s[i]):
                return
            
            #if num[i] is greater, we update res as num or store
            #the larger value in res.
            if int(ans[i]) < int(s[i]):
                
                for i in range(len(s)):
                    ans[i] = s[i]
                return
    
    def maxNumber(self, s, k, ans, idx, n):
        if k == 0 or idx==n-1:
            # print(f" k is 0")
            self.setAns(ans, s)
            return
        
        maxNum = 0
        for i in range(idx+1, n):
            maxNum = max(int(s[i]), maxNum)

        if str(maxNum) == s[idx]:
            self.maxNumber(s, k, ans, idx+1, n)
            return
        
        for j in range(n-1, idx, -1):
            if s[j] == str(maxNum):
                s[idx],s[j]=s[j],s[idx]
                self.maxNumber(s, k-1, ans, idx+1, n)
                s[idx],s[j]=s[j],s[idx]
        

             
    #Function to find the largest number after k swaps.
    def findMaximumNum(self,s,k):
        num = [x for x in s]
        ans = [x for x in s]
        self.maxNumber(num, k, ans, 0, len(s))
        print(ans)




Solution().findMaximumNum("129814999", 4)