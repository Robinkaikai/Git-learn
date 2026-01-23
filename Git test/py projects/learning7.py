#Slice
# def trim(s):
#     l = len(s)
#     #正数空格
#     a = 0
#     for n in range(l):
#         if s[n] == " ":
#             a = n + 1
#         else:
#             break
#     #倒数空格
#     b = -1
#     i = -1
#     while i >= -l:
#         if s[i] == " ":
#             b = i - 1
#         else:
#             break
#         i = i - 1
#     #索引
#     c = l + b + 1
#     s = s[a:c]
#
#     return s
#=======================================
#Iteration
# def findMinAndMax(L):
#     if not L:
#         return (None, None)
#     else:
#         minimum = L[0]
#         maximum = L[0]
#
#         for i in L:
#             if i > maximum:
#                 maximum = i
#
#             if i < minimum:
#                 minimum = i
#         return (minimum, maximum)
#=====================================================
#List Comprehensions
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if isinstance(s,str)]
#======================================================
#generator杨辉三角
# def triangles():
#     L = [1]
#
#     while True:
#         yield L
#         L = [1] + [L[i]+L[i+1] for i in range(len(L)-1)] + [1]
#
# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
#
# for t in results:
#     print(t)
#===========================================

