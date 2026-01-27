#闭包
# def createCounter():
#     x = 0  外层变量
#     def counter():
#         nonlocal x  !!!!内层仍能使用
#         x = x + 1
#         return x
#     return counter   返回函数