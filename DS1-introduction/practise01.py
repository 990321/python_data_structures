'''
问题一描述：使用函数，求前n个函数的和
'''
import time
def sumOFN(n):
    start_time = time.time()
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    end_time = time.time()
    return sum,end_time-start_time

print('计算的结果是%d 时间是%f'%sumOFN(10000))

# 高斯函数
# def sumOFN2(n):
#     return (n*(n+1))/2
# start_time = time.time()
# print(sumOFN2(10000))
# end_time = time.time()
# print(end_time-start_time)


# def foo(lala):
#     a = 0
#     for b in range(1,lala+1):
#         c = b
#         a = a + c
#     return a
# print(foo(10))

















