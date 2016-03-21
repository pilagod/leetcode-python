__author__ = 'pilagod'
def maxArea(self, height):
    left = 0
    right = len(height)-1
    result = 0
    while left < right:
        result = max(result, (right-left)*min(height[left], height[right]))
        if height[left] < height[right]:
            left+=1
            while height[left] <= height[left-1] and left < right:
                left+=1
        else:
            right-=1
            while height[right] <= height[right+1] and left < right:
                right-=1

        return result