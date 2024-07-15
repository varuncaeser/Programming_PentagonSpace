# to find the happy number
# def find_sqr(num):
#     sum=0
#     while(num!=0):
#         rem=num%10
#         sum=sum+(rem*rem)
#         num=num//10
#     return sum
# num=7
# res=num
# while(res!=1 and res!=4):
#     res=find_sqr(res)
#
# if(res==1):
#     print("its happy number")
# else:
#     print("not")
# #----------------------------------------------------------------
#
# #try to print 1-10000 happy numbers
# def find_sqr(num):
#     sum = 0
#     while num != 0:
#         rem = num % 10
#         sum += rem * rem
#         num //= 10
#     return sum
# for k in range(1, 10000):
#     slow = k
#     fast = find_sqr(k)
#
#     while fast != 1 and slow != fast:
#         slow = find_sqr(slow)
#         fast = find_sqr(find_sqr(fast))
#
#     if fast == 1:
#         print(k, end=' ')

# #----------------------------------------------------------------
# #to print HCF of given to two numbers
# #factors of 10=1,2,5,10
# #factors of 13=1,13
# commom factors is 1 and it is the Highest common factor
a = 13
b = 10
if (a < b):
    small = a
else:
    small = b
for i in range(1, small + 1):####range should be considered as the factors from 1 to the  smallest number in between given two numbers
    if (a % i == 0 and b % i == 0): #to get the factors ,is i perfectly divide a and b then it is a common factor
        cf = i
print(cf)
# #---------------------------------------------------------------------------------------------------------------------------------------
# #LCM of given two numbers
# #multiples of 5=5,10,15,20,25,30,35,.........
# #multiples of 7=7,14,21,28,35,............
#common multiple is 35 and least common multiple is always the first common multiple i.e; 35 is LCF For 5 and 7
a = 5
b = 7
c=a*b
if (a > b):
    great = a
else:
    great= b
for i in range(great,c+1):#range should considered as from the great number as start and end is the multiplication of two given numbers
    if (i % a == 0 and i % b == 0):####35%5==0 this is true and 35%7==0 true ,and the condition goes to true and cm is the value of i
        cm = i
        break
print(cm)

# #write a pgm to find factorial of a given number
#
# # def fact(num):
# #     res=1
# #     for i in range(1,num+1):
# #         res=res*i
# #     return res
# # num=5
# # num=fact(num)
# # print(num)
# #####RECURSIVE APPROACH
# #always start the recursive approach using termination condition as end condition
# #when we are calling a method or function recursively we need to change the parameters to the second iteration parameter
#to get the reverse of a number
# def reverse(num, res):
#     if (num == 0):
#         return res
#     return reverse(num // 10, (res * 10) + (num % 10))  ####(num=num//10,res=res*10+remainder[i.e,num%10=remainder])
#
#
# num = 2898
# res = reverse(num, 0)
# print(res)
