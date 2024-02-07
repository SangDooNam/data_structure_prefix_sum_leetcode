class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        
        result = [0] * (len(gain) + 1)
        
        for i in range(1,len(result)):
            result[i] = result[i-1] + gain[i-1]
        
        return max(result)
    


sol = Solution()
gain = [-5,1,5,0,-7]
gain = [-4,-3,-2,-1,4,3,2]
print(sol.largestAltitude(gain))



            