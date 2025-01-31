# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.


def two_sum( nums: list[int], target: int) -> list[int]:

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

# test cases                
assert two_sum([2,7,11,15], 9) == [0,1]
assert two_sum([3,2,4], 6) == [1,2]        
assert two_sum([3,3], 6) == [0,1]

print("passed testcases!!! :)")
        
        
        