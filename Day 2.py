# #to print this as output
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
###code follows
# k=1
# rows=5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#     print()
#----------------------------------------------------
#to print this as output
#A
# B C
# D E F
# G H I J
# K L M N O
###code follows

# k=1
# rows=5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(chr(k+64),end=" ")
#         k=k+1
#     print()
#----------------------------------------------
##to print this as output
#1
# 0 1
# 0 1 0
# 1 0 1 0
# 1 0 1 0 1
#code follows
# k=1
# rows=5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(k%2,end=" ")
#         k=k+1
#     print()
#--------------------------------------------
###to print this as output
#1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
#code follows
#we can use +1 or -1 for (i+j+1) or (i+j-1)
# rows=5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print((i+j+1)%2,end=" ")
#     print()
#---------------------------------------------------------
###to print this as output
# 1
# 3 2
# 6 5 4
# 10 9 8 7
# 15 14 13 12 11
#code follows
# sum=0
# rows=5
# for i in range(1,rows+1):
#     sum = sum + i
#     temp=sum
#     for j in range(1,i+1):
#         print(temp,end=" ")
#         temp=temp-1
#     print()
#----------------------------------------
####to print this as output
# A
# C B
# F E D
# J I H G
# O N M L K
# #code follows
#sum=0
# rows=5
# for i in range(1,rows+1):
#     sum = sum + i
#     temp=sum
#     for j in range(1,i+1):
#         print(chr(temp+64),end=" ")
#         temp=temp-1
#     print()
#----------------------------------------------------------
####to print this as output
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#code follows
# rows=5
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     print()
#-------------------------------
#####to print this as output
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#code follows
# rows=5
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     for j in range(i-1):
#         print('*',end=' ')
#     print()
#-----------------------------------------
##to get this as output
#         1
#       1 2 *
#     1 2 3 * *
#   1 2 3 4 * * *
# 1 2 3 4 5 * * * *
#code follows
# rows=5
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):###change range to (1,i+1)
#         print(j,end=' ')
#     for j in range(i-1):
#         print('*',end=' ')
#     print()
#----------------------------------
##to get this as output
# #       1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
#code follows
# rows=5
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):###change range to (1,i+1)
#         print(j,end=' ')
#     for j in range(i-1,0,-1):###change range to(i-1,0,-1)
#         print(j,end=' ')
#     print()
#-------------------------------------------------------------
