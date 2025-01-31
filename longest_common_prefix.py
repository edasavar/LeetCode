# Write a function to find the longest common prefix 
# string amongst an array of strings.

# If there is no common prefix, return an empty string "".
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:

    char_lowest = min(strs, key=len)
    char_length_lowest = len(char_lowest)
    idx_lowest = strs.index(char_lowest)

    i = 0
    prefix = ""

    while i < char_length_lowest:

        cur = strs[idx_lowest][i]

        for word in strs:
            if word[i] != cur:
                return prefix
        
        prefix += cur
        i += 1
    return prefix

assert longestCommonPrefix(["shoe", "shop", "shine"]) == "sh"
assert longestCommonPrefix(["potatoes", "pot noodles", "potholes"]) == "pot"
print("passed testcases!! :)")