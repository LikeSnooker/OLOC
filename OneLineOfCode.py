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

# 下面是错误的示范  聊表为空的时候  len(xs) <= 1 and xs 这个表达式值为false 而不是我们想要的 元素一个或零个的列表
# zs = lambda xs : (len(xs) <= 1 and xs) or zs([x for x in xs if x < xs[0]]) + [xs[0]] + zs([x for x in xs if x > xs[0]])
# test = [6,1,9,8,3,5,4,2,7]
# print(qs(test))


###################################################################################################################################################
 

