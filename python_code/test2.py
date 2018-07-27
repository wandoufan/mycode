import math

def entropyOfList(ls):
    """
    Given a list of some items, compute entropy of the list
    The entropy is sum of -p[i]*log(p[i]) for every unique element i in the list, and p[i] is its frequency
    """
    elements = {}
    for e in ls:
        elements[e] = elements.get(e, 0) + 1
    length = float(len(ls))
    print(elements)
    print(list(elements.values()))
    # for v in elements.values():
    #     print(v)
    return sum([-v / length * math.log(v / length) for v in list(elements.values())])

string1 = '华语年2月，金曲古金曲届全球金曲歌曲排行榜古届全金曲'
list1 = [] 
for i in string1:
    list1.append(i)
print(entropyOfList(list1))
# 3.183672971483787
# 2.5149845709853262
# 2.5753561499441857