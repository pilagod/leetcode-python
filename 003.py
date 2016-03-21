__author__ = 'pilagod'

def lengthOfLongestSubstring(s):
    dic = {}
    max_length = 0
    start_index = 0
    index = 0
    while(index < len(s)):
        ch = s[index]
        try:
            if dic[ch] >= 0:
                pre_index = dic[ch]
                if pre_index >= start_index:
                    max_length = max(max_length, index-start_index)
                    start_index = pre_index + 1
                dic[ch] = index
        except:
            dic[ch] = index
        finally:
            index += 1

    max_length = max(max_length, index-start_index)
    return max_length

print(lengthOfLongestSubstring("abcb"))


