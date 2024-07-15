#other way to check a num if it is prime
# def check_prime(num):
#     if(num<=1):   ##edge condition
#         return False
#     for i in range(2,num):
#         if(num%i==0):
#             return False
#     return True
# num=0
# result=check_prime(num)
# if(result==True):
#     print("Prime")
# else:
#     print("Not ")
#output--Prime
#-----------------------------
# def check_prime(num):
#     if(num<=1):   ##edge condition
#         return False
#     for i in range(2,num//2):##reduced time complexity ny num//2
#         if(num%i==0):
#             return False
#     return True
# num=13
# result=check_prime(num)
# if(result==True):
#     print("Prime")
# else:
#     print("Not ")
# #------------------------
# import math
# def check_prime(num):
#     if(num<=1):   ##edge condition
#         return False
#     for i in range(2,int(math.sqrt(num))): ### reduced time complexity by sqrt(num)
#         if(num%i==0):
#             return False
#     return True
# num=13
# result=check_prime(num)
# if(result==True):
#     print("Prime")
# else:
#     print("Not ")
#---------------------------------
# #----------Perfect number------##
# def perfect_num (num):
#     sum=0
#     for i in range(1,num):
#         if(num%i==0):
#             sum=i+sum   ###adding the factors expect the number [1+2+3]=6//perfect number
#     return sum
# num=6
# res=perfect_num(num)
# if(res==num):
#     print("Perfect")
# else:
#     print("Not")
# #-------------------------
#perfect numbers between 1-10000
#6
# 28
# 496
# 8128
#----code----
# def perfect_num (num):
#     sum=0
#     for i in range(1,num):
#         if(num%i==0):
#             sum=sum+i
#     return sum
# for k in range(1,10000):
#     num = k
#     res = perfect_num(num)
#     if(res==num):
#         print(num)
#-------------REVERSE NUMBER--------------#
# num=181
# res=0
# while(num!=0):
#     rem=num%10
#     res=(res*10)+rem
#     num=num//10
# print(res)
#-----------------------
######PALINDROME NUMBER#####
# def reverse(num):
#     res=0
#     while(num!=0):
#         rem=num%10
#         res=res*10+rem   ###USING THE REVERSE NUMBER CONDITION
#         num=num//10
#     return res
# num=99
# res=reverse(num)
# if(res==num):
#     print("PALINDROME")
# else:
#     print("NOT")
#---------------------
#to print the palindrome from 1-10000
def reverse(num):
    res=0
    while(num!=0):
        rem=num%10
        res=res*10+rem
        num=num//10
    return res
for k in range(1,10000):
    num = k
    res = reverse(num)
    if(res==num):
        print(num)

