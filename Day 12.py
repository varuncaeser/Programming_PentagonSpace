#recursive approach to find number of digits in number
# def no_of_digits(num, count):
#     if num == 0:
#         return count
#     return no_of_digits(num // 10, count + 1)
# num=153
# digit=no_of_digits(num,0)
# print(digit)
#recursive approach to find number is armstrong or not
# def no_of_digits(num, count):
#     if num == 0:
#         return count
#     return no_of_digits(num // 10, count + 1)
#till here it is the recusive approch for no of digits in num


# def check_armstrong(num, res, digit):
#     if (num == 0):
#         return res
#     return check_armstrong(num // 10, ((num % 10) ** digit) + res, digit)
#
#
# num = 1634
# digit = no_of_digits(num, 0)
# res = check_armstrong(num, 0, digit)
# if res == num:
#     print("ITS ARMSTRONG")
# else:
#     print("ITS NOT")
#----------------------
#factorial using recursive
# def fact(num):
#      if num<=1:
#          return 1
#      return num*fact(num-1)
# num=5
# num=fact(num)
# print(num)
#-------------------------------
#count-digit
def count(num):
    if num==0:
        return 0
    return count(num//10)+1
num=12345
res=count(num)
print(res)

