#
# 快速排序 : 选一个基准 小的放左边 大的放右边 然后递归
#

# 普通版本
def quickSort(xs):
    if len(xs) < 2:
        return xs
    less = []
    more = []
    for x in xs:
        if x < xs[-1]:
            less.append(x)
        elif x > xs[-1]:
            more.append(x)
    return quickSort(less) + [xs[-1]] + quickSort(more)

# 一行代码
# 这里的技巧是 and 表达式 在左右都为真时 值为右边的子表达式,or表达式 左式为真的时候 右式将不被计算
qs = lambda xs : ((len(xs) <= 1 and [xs]) or [ qs([x for x in xs[1:] if x < xs[0]]) + [xs[0]] + qs([x for x in xs[1:] if x > xs[0]])])[0]

# 下面是错误的示范  列表为空的时候  len(xs) <= 1 and xs 这个表达式值为false 而不是我们想要的 元素一个或零个的列表
# zs = lambda xs : (len(xs) <= 1 and xs) or zs([x for x in xs if x < xs[0]]) + [xs[0]] + zs([x for x in xs if x > xs[0]])
# test = [6,1,9,8,3,5,4,2,7]
# print(qs(test))


###################################################################################################################################################

#
# 归并排序 假设两个已经排好的数组 将这两个数组合并就比较简单了，只需要依次拉出它们的排头兵 比较一下
# 小的放入新数组，重复此操作 直到两个数组一个为空，最后把剩下的元素全都放入新数组就可以了
#

# 普通版
def mergeSort(Q):
    if len(Q) <= 1:
        return Q
    middle = (0 + len(Q) ) >> 1
    left   = mergeSort(Q[0:middle])
    right  = mergeSort(Q[middle:])
    newQ   = []
    while left and right:
        newQ.append( (left[0] < right[0] and left.pop(0)) or (left[0] > right[0] and right.pop(0)) )
    newQ.extend(left)
    newQ.extend(right)
    return newQ

test = [6,1,9,8,3,5,4,2,7]
print(mergeSort(test))

# 将其中的关键部分 抽出来
def merge(l,r):
    newQ = []
    while l and r:
        newQ.append( l.pop(0) if l[0] < r[0] else r.pop(0) )
    newQ.extend(l)
    newQ.extend(r)
    return newQ
l = [1,3,5,7,9]
r = [2,4,6]
print(merge(l,r))

r_l = [1,3,5,7,9]
r_r = [2,4,6]
# 改为递归版本
def recursiveMerge(l,r):
    if l and r:
        if l[0] < r[0]:
            return [l[0]] + recursiveMerge(l[1:],r)
        else:
            return [r[0]] + recursiveMerge(l,r[1:])
    else:
        return l + r
# 将递归版的函数改为 lambda
rm = lambda l,r : ( (l and r) and ( [l[0]] + rm(l[1:],r) if l[0] < r[0] else [r[0]] + rm(l,r[1:]) ) ) or l + r

# 原函数可以改变为如下形式
def mergeSortEx(Q):
    if len(Q) <= 1:
        return Q
    return rm(mergeSortEx(Q[0:(0 + len(Q) ) >> 1]),mergeSortEx(Q[(0 + len(Q) ) >> 1:]))

testQ = [9,3,2,8,4,6,1,5,7]
print(mergeSortEx(testQ))

#进而 归并排序可改为如下形式
ms = lambda Q : ( (len(Q) <= 1 and [Q]) or [rm(ms(Q[0:(0 + len(Q) ) >> 1]),ms(Q[(0 + len(Q) ) >> 1:]) )])[0]
print(ms(testQ))

# 进行到这里 大约可以给出最终版了，还有一个问题需要解决 ，就是当初被我们抽出来的 rm,现在要以什么样的形式给放回去
# 先看下面的代码
testLL = [1,3,5,7,9]
testRR = [2,4,6]
print('匿名lambda')
print( (lambda l,r,func = lambda l,r,func:  ( (l and r) and ( [l[0]] + func(l[1:],r,func) if l[0] < r[0] else [r[0]] + func(l,r[1:],func) ) ) or l + r:func(l,r,func))(testLL,testRR) )
# print 函数中 我们调用了一个真正 匿名 的lambda表达式  不同于 rm(76行定义的lambda)，这次的lambda表达式将彻底是匿名的


# 好了 现在可以完工了
print('打完收工')
ZQue = [3,7,1,9,8,4,6,5,2]
MS = lambda Q : ( (len(Q) <= 1 and [Q]) or [(lambda l,r,func = lambda l,r,func:  ( (l and r) and ( [l[0]] + func(l[1:],r,func) if l[0] < r[0] else [r[0]] + func(l,r[1:],func) ) ) or l + r:func(l,r,func))(MS(Q[0:(0 + len(Q) ) >> 1]),MS(Q[(0 + len(Q) ) >> 1:]) )])[0]
print (MS(ZQue))
