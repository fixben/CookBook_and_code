#pow() 与幂指数运算差不多，计算一个数的几次方 有两个参数，第一个是底数，第二个是指数
import math
print(math.pow(4,3))
#幂运算 函数返回浮点型，幂运算返回整形
print(4**3)

#fabs() 对一个数值获取他的绝对值
print(math.fabs(-1))
print(math.fabs(3))
print(math.fabs(0))

# abs() 获取绝对值操作 不是数学模块当中的，是Python内置函数,返回值由本身类型而定
print(abs(-1))
print(abs(-2.5))

#fsum() 求和
print(math.fsum([1,4,5,7]))
#sum() python内置求和
print(sum([1,4,5,7]))

#