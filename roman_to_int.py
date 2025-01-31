# Given a roman numeral, convert it to an integer.

def roman_to_int(s: str) -> int:
    
    i = 0
    converted_int = 0
    
    d = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
        }

    
    while i < len(s):
        current_roman = s[i]
        combined = ""

        if i + 1 < len(s):
            next_roman = s[i+1]
            combined = current_roman + next_roman

        if combined in d:
            converted_int = converted_int + d[combined]
            i += 2
            
        else:
            converted_int = converted_int + d[current_roman]
            i += 1
            
    return converted_int

# test cases

test_cases = {
    "III":3,
    "IV":4,
    "LVIII": 58,
    "XCV":95,
    "MCMXCIV": 1994,
    "MCV": 1105
    }

for numeral, expected in test_cases.items():
    result = roman_to_int(numeral)
assert result == expected, f"Test failed for input '{numeral}', expected '{expected}'"
print("passed all test cases!")



        