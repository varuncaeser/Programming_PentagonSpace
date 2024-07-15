# a=[1,2,3]
# b=[1,2,3]
# print(a is b)
# print(id(a))
# print((id(b)))#diff address(bcoz it is oin ting to the outer list)
# print(id(a[0]))
# print(id(b[0]))#same address(inner list)
# print(id(id(a[0])))
# print(id(id(id(a[0]))))#same address(inner list)
#
#
# #range
# #syntax--range(<start>,<stop>,<step>)
# #default step value is 1
# for i in range(1,5,1):
#     print(i)
# #range consider from index of 0
# for j in range(5):
#     print(j)#0,1,2,3,4-> 5 values
# for i in range(4,1,-1):
#     print(i)#4,3,2
# for i in range(4,4,-1):
#     print(i)#null
# for i in range(4,2,1):
#     print(i)#null
