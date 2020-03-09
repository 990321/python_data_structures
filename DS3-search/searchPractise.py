'''
**练习**：
写一个函数，该函数需要一个列表和我们正在搜索的项作为参数，
并返回一个是否存在的布尔值。found = False
'''
# def sequentialSearch(alist, item):
#     pos = 0   # 下标索引
#     found = False
#     while pos<len(alist) and not found:
#         if alist[pos] == item:
#             found = True
#         else:
#             pos = pos + 1
#     return found


# testlist = [1, 12, 30, 45, 20]
# print(sequentialSearch(testlist, 20))



'''
    升序 [17,20,26,30,44,54,55,65,77,93]
    假设寻找的项在列表中，
    假设寻找的项不在列表中，50
'''
# def orderSequentialSearch(alist,item):
#     pos = 0
#     found = False
#     stop = False
#     while pos<len(alist) and not found and not stop:
#         if alist[pos] == item:
#             found = True
#         else:
#             if alist[pos] > item:
#                 stop = True
#             else:
#                 pos = pos + 1
#     return found

# testlist1 = [17,20,26,30,44,54,55,65,77,93]
# print(orderSequentialSearch(testlist1,30))


'''
    有序列表
    二分查找：每次都从剩余项中的中间元素进行比对
'''
# def binarySearch(alist,item):
#     found = False
#     first = 0
#     last = len(alist) - 1

#     while first<=last and not found:
#         # 中间
#         midpoint = (first+last)//2
#         if alist[midpoint] == item:
#             found = True
#         else:
#             if item < alist[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
    
#     return found

# testlist2 = [0,1,2,8,13,17,19,32,42]
# print(binarySearch(testlist2,3))

#  递归实现二分查找
def binarySearch(alist,item):
    if len(alist) == 0:
        return False
    midpoint = len(alist)//2 # 分成两半，下标
    if alist[midpoint] == item:
        return True
    else:
        if alist[midpoint] > item:
            return binarySearch(alist[:midpoint],item)
        else:
            return binarySearch(alist[midpoint+1:],item)

testlist3 = [0,1,2,8,13,17,19,32,42]
print(binarySearch(testlist3,8))







