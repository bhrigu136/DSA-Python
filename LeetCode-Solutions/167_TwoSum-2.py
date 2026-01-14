# TWO POINTERS approach
class Solution:
    def twoSum(self, nums, target):
        left, right = 0, len(nums) -1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return [left+1, right+1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
        

t = int(input().strip())
for _ in range(t):
    nums = list(map(int, input().strip().split()))
    target = int(input().strip())
    sol = Solution()
    result = sol.twoSum(nums, target)
    print(result)

""" 
Output:
3
2 7 11 15
9
[1, 2]
-1 0
-1
[1, 2]
1 2 3 4 4 9 56 90
8
[4, 5]
"""
