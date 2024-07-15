#To get this as the output
#         1
#       2 6
#     3 7 10
#   4 8 11 13
# 5 9 12 14 15
#code follows-code 1
# rows=5
# start=1
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(' ',end=' ')
#     temp=start
#     for j in range(1,i+1):
#         print(start,end=' ')
#         start+=rows-j
#     start=temp+1
#     print()
#----------------------------------
#code 2 follows
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(rows - i):
#         print(' ', end=' ')
#     #k: int
#     for k in range(1, i + 1):
#         print(i, end=' ')
#         i = i + rows - k
#     print()
#code 3 follows
# rows=5
# for i in range(1,rows+1):
#     k=i
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(0,i):
#         print(k,end=' ')
#         k=k+rows-1-j
#     print()
#code 4 follows
# rows=5
# for i in range(1,rows+1):
#     k=i
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print(k,end=' ')
#         k=k+rows-j
#     print()
#----------------------------------------------
#to get this pattern as output
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * *
#     * * *
#       * *
#         *
#code follows
# rows=5
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print("*",end=' ')
#     for j in range(i-1):
#         print("*",end=' ')
#     print()
#top half-output
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# for i in range(1,rows):
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(rows-i):
#         print("*",end=' ')
#     for j in range(rows - i - 1):
#         print("*", end=' ')
#     print()
#bottom half-output
# * * * *
# * * *
# * *
# *
#to get this pattern as output
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
#code follows
# rows=5
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print("*",end=' ')
#     for j in range(i-1):
#         print("*",end=' ')
#     print()
# for i in range(1,rows):
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(rows-i):
#         print("*",end=' ')
#     for j  in range(rows-i-1):
#         print("*",end=' ')
#     print()
#to get this as output
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
#code follows
# rows=5
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print("*",end=' ')
#     for j in range(i-1):
#         print("*",end=' ')
#     print()
# for i in range(1,rows):
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(rows-i):
#         print("*",end=' ')
#     for j  in range(rows-i-1):
#         print("*",end=' ')
#     print()
# rows=5
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print("*",end=' ')
#     for j in range(i-1):
#         print("*",end=' ')
#     print()
# for i in range(1,rows):
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(rows-i):
#         print("*",end=' ')
#     for j  in range(rows-i-1):
#         print("*",end=' ')
#     print()
#--------------------------------------
#to get this as ouput
#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
#   1 2 3 4 3 2 1
#     1 2 3 2 1
#       1 2 1
#         1
#code follows
# rows=5
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print(j,end=' ')
#     for j in range(i-1,0,-1):
#         print(j,end=' ')
#     print()
# for i in range(1,rows):
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(1,rows-i+1):
#         print(j,end=' ')
#     for j  in range(rows-i-1,0,-1):
#         print(j,end=' ')
#     print()
#-------------------------------------------
#to get this as output
#         5
#       5 4 5
#     5 4 3 4 5
#   5 4 3 2 3 4 5
# 5 4 3 2 1 2 3 4 5
#   5 4 3 2 3 4 5
#     5 4 3 4 5
#       5 4 5
#         5
#code follows
# rows=5
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print(6-j,end=' ')#we can use rows+1-j also
#     for j in range(i-1,0,-1):
#         print(6-j,end=' ')#we can use rows+1-j also
#     print()
# for i in range(1,rows):
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(1,rows-i+1):
#         print(6-j,end=' ')#we can use rows+1-j also
#     for j  in range(rows-i-1,0,-1):
#         print(6-j,end=' ')#we can use rows+1-j also
#     print()
#----------------------------------------------------------
#code with changing the range
# rows=5
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(' ',end=' ')
#     for j in range(rows,rows-i,-1):##
#         print(j,end=' ')
#     for j in range(rows+2-i,rows+1,1):##
#         print(j,end=' ')
#     print()
# for i in range(1,rows):
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(rows,i,-1):
#         print(j,end=' ')
#     for j in range(rows+i-3,rows+1,1):
#         print(j,end=' ')
#     print()

