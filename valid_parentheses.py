class Solution: 
    def isValid(self, s: str) -> bool:
        # init empty stack
        stack = [] 
        # hashmap for the parenthesis characters
        # closing to opening bracket
        mapping = {")":"(", "}":"{", "]":"["}
        
        # for the input string
        for char in s:
            # check if its an open bracket 
            #  .values() refers to the  open bracker
            if char in mapping.values():
                # append the current character in s to 
                # the stack
                stack.append(char)
            
            # else if the current char is a closed bracket 
            # keys refer to closed brackets    
            elif char in mapping.keys():
                # if the stack is empty and there is no opening bracket
                # to match or if the top of the stack doesnt
                # match the opening bracket, return false
                if not stack or mapping[char] != stack.pop():
                    return False
        
        
        return not stack
    
# Tests function
def test_isValid():
    solution = Solution()

    # Test cases
    test_cases = {
        "": True,  # Empty string is valid
        "()": True,
        "()[]{}": True,  # All brackets correctly matched
        "(]": False,  # Mismatched brackets
        "([)]": False,  # Wrong order
        "{[]}": True,  # Nested correctly
        "{[()]}" : True,  # Complex but correct
        "{[(])}": False,  # Incorrect nesting
        "[": False,  # Only an opening bracket
        "({[": False,  # Incomplete opening
        "}])": False,  # Closing without opening
    }

    for s, expected in test_cases.items():
        result = solution.isValid(s)
        print(f"Testing '{s}': Expected {expected}, Got {result}")
        assert result == expected, f"Test failed for input '{s}'"

    print("All tests passed!")

# Run tests only when the script is executed directly
if __name__ == "__main__":
    test_isValid()
        
        
        
        
        
        