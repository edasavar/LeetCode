# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        i = 0

        while i < len(nums):

            a = nums[i]
            j = 0

            while j < len(nums):

                b = nums[j]
                c = a + b

                # if element is is equal to target
                # and is a unique indice, return
                # list of indices
                if c == target and i != j:
                    return [i, j]

                j += 1
            i += 1
            
            
    # Tests function        
def test_twoSum():
        
        solution = Solution()
        
        test_cases = [
            ([2,7,11,15], 9, [0,1]),  
            ([3,2,4], 6, [1,2]), 
            ([3,3], 6, [0,1]) # case with duplicate values in input
        ]
        
        for nums, target, expected in test_cases:
            result = solution.twoSum(nums, target)
            print(f"Testing nums = {nums}, target = {target}: Expected {expected}, Got {result}")
            assert result == expected, f"Test failed for nums = {nums}, target = {target}"
        print("All tests passed!")
        
test_twoSum()
        
        
        