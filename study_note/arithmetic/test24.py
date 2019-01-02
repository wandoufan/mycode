#输入三条边长，判断三角型的类型
#注意：先判断能否组成三角形
def f(a,b,c):
    list1=[a,b,c]
    list1.sort()
    max=int(list1[2])
    middle=int(list1[1])
    min=int(list1[0])

    if min+middle<=max or max-min>=middle:
        print('不能组成三角形')
    else:
        if max**2==min**2+middle**2:
            print('直角三角形')
        elif max**2>min**2+middle**2:
            print('钝角三角形')
        else:
            print('锐角三角形')

    print('')
        
#f(1,4,6)