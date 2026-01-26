#map&reduce
# def normalize(name):
#     name = name.lower()
#     name = name[0].upper() + name[1:] //str是不可变类型
#     return name
#//仅首字母大写，等于name.capitalize()
# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
#--------------------------------------------------------
# from functools import reduce
# def plus(x,y):
#     return x*y
#
# def prod(L):
#     return reduce(plus,L)
#--------------------------------------------------------
# from functools import reduce
# digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# def str1num(ch):
#     return digits[ch]
#
# def str2float(s):
#     int_parts,float_parts = s.split('.')
#     integer = reduce(lambda x,y : x*10+y,map(str1num,int_parts))
#     floater = reduce(lambda x, y: x * 10 + y, map(str1num, float_parts))
#     return integer + floater / (10**len(float_parts))
#===========================================================================
#filter
# def is_palindrome(n):
#     n = str(n)
#     return n==n[::-1] !!!!!!
#===================================
#sorted
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
# def by_name(t):
#     return t[0]
#
# L2 = sorted(L, key=by_name)
# print(L2)
#---------------------------------------------
# def by_score(t):
#     return t[1]
#
# L2 = sorted(L, key=by_score,reverse=True)
# print(L2)
# lst = [0,1,2,3,4]
# print(list(reversed(lst)))