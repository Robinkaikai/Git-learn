#匿名函数
# L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
#
# print(L)
#=========================================================
# #Decorator
# import time, functools
#
# def metric(fn):
#     @functools.wraps(fn)
#     def wraps(*args, **kw):
#         print('%s executed in %s ms' % (fn.__name__, 10.24))
#         return fn(*args, **kw)
#     return wraps
#
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;
#
# f = fast(11, 22)
# s = slow(11, 22, 33)