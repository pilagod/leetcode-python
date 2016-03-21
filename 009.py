__author__ = 'pilagod'
from math import *

def isPalindrome(x):
    if x < 0:
        return False
    elif x == 0:
        return True
    left = pow(10, floor(log10(x)))
    right = 1
    while right < left:
        print(floor(x / left))
        if (floor(x / left) - floor(x / right)) % 10 != 0:
            return False
        left = left / 10
        right = right * 10

    if right == left:
        return True
    else:
        return False

# def isPalindrome(self, x):
#         if x == 0:
#             return True
#         elif x < 0 or x % 10 == 0:
#             return False
#
#         reverse = 0
#
#         while reverse < x:
#             digit_one = x % 10
#             reverse = reverse*10 + digit_one
#             if reverse == x or reverse == x / 10:
#                 return True
#             x = x / 10
#
#         return False


print(isPalindrome(123421))