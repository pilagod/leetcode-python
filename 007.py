__author__ = 'pilagod'
def reverse(x):
    if x < 0:
        result = int(str(x)[0] + str(x)[:0:-1])
        return result if result > -4294967296 else 0
    else:
        result = int(str(x)[::-1])
        return result if result < 4294967296 else 0

print(reverse(-10))