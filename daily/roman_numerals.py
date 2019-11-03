'''
Problem: Convert Roman Numerals to Decimal
From: Daily Interview Pro 04/11/2019

Given a Roman numeral, find the corresponding decimal value.
Inputs will be between 1 and 3999. 

Example: 
Input: IX
Output: 9

Input: VII
Output: 7

Input: MCMIV
Output: 1904
Roman numerals are based on the following symbols:

I     1
IV    4
V     5
IX    9 
X     10
XL    40
L     50
XC    90
C     100
CD    400
D     500
CM    900
M     1000

Numbers are strings of these symbols in descending order.
In some cases, subtractive notation is used to avoid repeated characters.
The rules are as follows:
1.) I placed before V or X is one less,
so 4 = IV (one less than 5), and 9 is IX (one less than 10)

2.) X placed before L or C indicates ten less,
so 40 is XL (10 less than 50) and 90 is XC (10 less than 100).

3.) C placed before D or M indicates 100 less,
so 400 is CD (100 less than 500), and 900 is CM (100 less than 1000).
'''
def roman_to_decimal(roman):
  if len(roman) == 0:
    return 0
  translation = {
    'I' : 1,
    'IV': 4,
    'V' : 5,
    'IX': 9,
    'X' : 10,
    'XL': 40,
    'L' : 50,
    'XC': 90,
    'C' : 100,
    'CD': 400,
    'D' : 500,
    'CM': 900,
    'M' : 1000
  }
  if len(roman) == 1:
    return translation[roman[0]]

  total = 0
  curr = ''
  for i in range(len(roman)):
    tentative = curr + roman[i]
    tentative_val = translation.get(tentative, -1)
    if tentative_val < 0:
      total += translation[curr]
      curr = roman[i]
    else: 
      curr = tentative

  if len(curr) > 0:
    total += translation[curr]

  return total


print(roman_to_decimal('V'))
print(roman_to_decimal('VI'))
print(roman_to_decimal('IV'))
print(roman_to_decimal('LVIII'))
print(roman_to_decimal('VIII'))
print(roman_to_decimal('XIII'))
print(roman_to_decimal('MCMXCIV'))
print(roman_to_decimal('MMMCMXCXX'))