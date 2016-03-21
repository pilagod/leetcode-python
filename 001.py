__author__ = 'pilagod'
# @return a tuple, (index1, index2)
def twoSum(num, target):
    dic_value = {}
    for i in range(0, len(num)):
        try:
            dic_value[num[i]].append(i)
        except:
            dic_value[num[i]] = []
            dic_value[num[i]].append(i)

    for value in dic_value:
        try:
            if dic_value[target-value]:
                index1 = dic_value[value][0]+1
                if len(dic_value[target-value]) == 1:
                    index2 = dic_value[target-value][0]+1
                elif len(dic_value[target-value]) > 1:
                    index2 = dic_value[value][1]+1

                return (index1, index2) if index1 < index2 else (index2, index1)
        except:
            continue

print(twoSum([0, 4, 3, 0], ))

