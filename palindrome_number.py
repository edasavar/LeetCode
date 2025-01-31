# Given an integer x, return true if x is a 
# palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert input to string,
        # check if the reverse of the string
        # is equal to input 
        return str(x) == str(x)[::-1]



def test_isPalindrome():

    solution = Solution()
    
    test_cases = [
        (121, True),
        (-121, False),
        (10,False),
        (0, True),
        (1238321, True)
        ]
    
    for num, expected in test_cases:
        result = solution.isPalindrome(num)
        print(f"Testing num = {num}: Expected {expected}, result {result}")
        assert result == expected, f"Test failed for the number {num}, expected result was {expected}"
    
    print("all test cases passed")
    
test_isPalindrome()


