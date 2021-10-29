# Question url: https://leetcode.com/problems/roman-to-integer/

# Difficulty is easy
# Solution 1
class Solution:
  def romanToInt(self, s: str) -> int:
    roman_table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    # Reverse iteration solution 
    
    num = 0
    last = "I"
    
    for numeral in s[::-1]:
      if roman_table[numeral] < roman_table[last]:
        num -= roman_table[numeral]
      else:
        num += roman_table[numeral]
      last = numeral
    return num