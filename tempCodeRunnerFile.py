def romanToInt(s: str) -> int:
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                result -= roman_to_int[s[i]]
            else:
                result += roman_to_int[s[i]]
        return result
s ='MMMCXL'
print(romanToInt(s))


def intToRoman(num: int) -> str:
        # Define the mappings from integer values to Roman numerals
    integer_to_roman = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
        
        # Initialize an empty string to store the Roman numeral representation
    roman = ''
        
        # Iterate through the integer-to-Roman mappings
    for value, numeral in integer_to_roman.items():
            # Repeat the current Roman numeral while the value fits into the remaining number
        while num >= value:
            roman += numeral
            num -= value
        
    return roman

num=3140
print(intToRoman(num))