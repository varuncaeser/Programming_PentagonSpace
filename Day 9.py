# 1
# 2 3
# 4 5 6
# 7 8 9 11
# 22 33 44 55 66
# 77 88 99 101 111 121
#to print these palindrome numbers till 121 in pattern
# def reverse(num):
#     res = 0
#     while (num != 0):
#         rem = num % 10
#         res = res * 10 + rem
#         num = num // 10
#     return res
#
#
# rows = 6  ###rows are dynamic here
# k = 1
# for i in range(1, rows + 1):
#     for j in range(i):
#         while (True):  ####infinite condition
#             if reverse(k) == k:  ####if k is not palindrome ,it goes to else and increment k
#                 print(k, end=' ')
#                 k = k + 1
#                 break  ####here to break the infinity loop of while true
#             else:
#                 k = k + 1
#     print()
#to print the number of digits in a given number
# def no_of_digits(num):
#     count=0
#     while(num!=0):
#         num=num//10
#         count+=1
#     return count
# num=1634
# count=no_of_digits(num)
# print(count)
#output --- 4
#----------------ARMSTRONG NUMBER---------
def no_of_digits(num):
    count = 0
    sum = 0
    original_num = num

    # Count the number of digits
    while num > 0:
        num //= 10
        count += 1

    num = original_num  # Reset num to the original number

    # Calculate the sum of the digits raised to the power of count
    while num > 0:
        rem = num % 10
        sum += rem ** count
        num //= 10

    return sum


num = 153
sum_of_digits = no_of_digits(num)

if sum_of_digits == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


