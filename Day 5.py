#to print Heart pattern
#  * *     * *
# *     *     *
# *           *
#   *       *
#     *   *
#       *
# rows=6
# cols=7
#
# for i in range(rows):
#     for j in range(cols):
#         if(i==1 and j%3==0)or (i==0 and j%3!=0)or (i-j==2)or(i+j==8):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()
#--------------------------------------------------------------------
#TO get the name inside the pattern
#   * *   * *
# *     *     *
# * V I R A T *
#   *       *
#     *   *
#       *
#code follows
# rows=6
# cols=7
#
# for i in range(rows):
#     for j in range(cols):
#         if(i==1 and j%3==0)or (i==0 and j%3!=0)or (i-j==2)or(i+j==8):
#             print("*",end=' ')
#         elif(i==2 and j==1):
#             print("V",end=' ')
#         elif(i==2 and j==2):
#             print("I",end=' ')
#         elif(i==2 and j==3):
#             print("R",end=' ')
#         elif(i==2 and j==4):
#             print("A",end=' ')
#         elif(i==2 and j==5):
#             print("T",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
#---------------------------------------------
#to print the reverse heart
#       *
#     *   *
#   *       *
# *           *
# *     *     *
#   * *   * *
#code follows
# rows=6
# cols=7
#
# for i in range(rows):
#     for j in range(cols):
#         if((i+j==3)or(j-i==3)or(j%3==0 and i==4)or(j%3!=0 and i==5)):
#             print("*",end=' ')

#         else:
#             print(" ",end=' ')
#     print()
#-----------------------------------------------------
#to print name inside the reverse heart
#       *
#     *   *
#   *       *
# * V I R A T *
# *     *     *
#   * *   * *
#code follows
# rows=6
# cols=7
#
# for i in range(rows):
#     for j in range(cols):
#         if((i+j==3)or(j-i==3)or(j%3==0 and i==4)or(j%3!=0 and i==5)):
#             print("*",end=' ')
#         elif(i==3 and j==1):
#             print("V",end=' ')
#         elif(i==3 and j==2):
#             print("I",end=' ')
#         elif(i==3 and j==3):
#             print("R",end=' ')
#         elif(i==3 and j==4):
#             print("A",end=' ')
#         elif(i==3 and j==5):
#             print("T",end=' ')
#         else:
#             print(" ",end=' ')
#     print()
#----------------------------------------
#to print a square
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
#code follows
# rows = 5
# for i in range(rows):
#     for j in range(rows):
#         if (i == 0 or j == 0 or j == rows - 1 or i == rows - 1):
#             print("*", end=' ')
#         else:
#             print(' ', end=' ')
#     print()
#----------------------------------
#to print a right-angled triangle
# *
# * *
# *   *
# *     *
# * * * * *
#code follows
# rows = 5
# for i in range(rows):
#     for j in range(rows):
#         if (i == rows - 1 or j == 0 or i == j):
#             print("*", end=' ')
#         else:
#             print(' ', end=' ')
#     print()
#-----------------------------------------
#to print this as output
#   * *   * *
# *     *     *
# * V I R A T *
#   *       *
#     *   *
#       *
#       *
#     *   *
#   *       *
# * V I R A T *
# *     *     *
#   * *   * *
#code follows
# rows=6
# cols=7
# for i in range(rows):
#     for j in range(cols):
#         if(i==1 and j%3==0)or (i==0 and j%3!=0)or (i-j==2)or(i+j==8):
#             print("*",end=' ')
#         elif(i==2 and j==1):
#             print("V",end=' ')
#         elif(i==2 and j==2):
#             print("I",end=' ')
#         elif(i==2 and j==3):
#             print("R",end=' ')
#         elif(i==2 and j==4):
#             print("A",end=' ')
#         elif(i==2 and j==5):
#             print("T",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# for i in range(rows):
#     for j in range(cols):
#         if((i+j==3)or(j-i==3)or(j%3==0 and i==4)or(j%3!=0 and i==5)):
#             print("*",end=' ')
#         elif(i==3 and j==1):
#             print("V",end=' ')
#         elif(i==3 and j==2):
#             print("I",end=' ')
#         elif(i==3 and j==3):
#             print("R",end=' ')
#         elif(i==3 and j==4):
#             print("A",end=' ')
#         elif(i==3 and j==5):
#             print("T",end=' ')
#         else:
#             print(" ",end=' ')
#     print()
#-------------------------------------------------------------------
# #to print this
# * * * * * * *
# * *   *   * *
# *   * * *   *
# * * * * * * *
# *   * * *   *
# * *   *   * *
# * * * * * * *
#code follows
# rows = 7
# for i in range(rows):
#     for j in range(rows):
#         if((i==(rows)//2) or (j==(rows)//2) or (i==j) or (i+j==rows-1)or i==0 or j==0 or i==rows-1 or j==rows-1):
#             print("*", end=' ')
#         else:
#             print(' ', end=' ')
#     print()
#---------------------------------------
# *           *
#   *       *
#     *   *
#       *
#     *   *
#   *       *
# *           *
#code follows
# rows = 7
# for i in range(rows):
#     for j in range(rows):
#         if(i==j or i+j==rows-1):
#             print("*", end=' ')
#         else:
#             print(' ', end=' ')
#     print()
