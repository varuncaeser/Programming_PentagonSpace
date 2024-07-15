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
###to get this as output
# #       5
#       5 4 5
#     5 4 3 4 5
#   5 4 3 2 3 4 5
# 5 4 3 2 1 2 3 4 5
##code follows
# rows=5
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(rows,rows-i,-1):##
#         print(j,end=' ')
#     for j in range(rows+2-i,rows+1,1):##
#         print(j,end=' ')
#     print()
###to get this as output
# #       1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5
#code follows
# rows=5
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(i,0,-1):##start-->relate with i=j-->start=i
#         print(j,end=' ')
#     for j in range(2,i+1,1):##end -->relate with i=j-->end=i+1(i+1 as end consider -1)
#         print(j,end=' ')
#     print()
