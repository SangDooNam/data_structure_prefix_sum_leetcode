class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0 
        for i, num in enumerate(nums):
            if left_sum == (total - left_sum - num):
                return i
            left_sum += num
        
        return -1
    
sol = Solution()

nums = [1,7,3,6,5,6]
nums = [2,1,-1]
nums = [1,2,3]
nums = [-1,-1,-1,-1,-1,0]
print(sol.pivotIndex(nums))