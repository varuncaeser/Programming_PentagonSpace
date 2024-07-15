#----------------------------
#Numbers
#----------------------
#output:
#0
#1
#2
#3
#4
#5
#none
#code follows
# def print_num(num):
#     if num==0:
#         print(num)
#         return
#     print_num(num-1)
#     print(num)
# num=5
# res=print_num(num)
# print(res)
#-------------------------
#output:
# 5
# 4
# 3
# 2
# 1
# 0
#None
# #code follows
# def print_num(num):
#     if num==0:
#         print(num)
#         return
#     print(num)
#     print_num(num-1)
#
# num=5
# res=print_num(num)
# print(res)
#-----------------------------
# n=int(input("enter number"))
# for i in range(1,n+1):
#     print(i,end=' ')
#     print()
#--------------------------
#enter number 10
# 1 2
# 3 4
# 5 6
# 7 8
# 9 10
#---------------------------------
n=int(input("enter number"))
for i in range(1,n+1):
    if(i%2!=0):
        print(i ,end=' ')
    else:
        print(i)


