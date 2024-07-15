# # pattern printing
# for k in range(5):
#     print("$",end=" ")
#
# for v in range(5):
#     for i in range(5):
#         print("#",end="  ")
#     print()
# for i in range(5):
#     for j in range(5):
#         print(i,end='')
#     print()
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=' ')
#     print()
# for i in range(5):
#     for j in range(0,5):
#         print(j,end=" ")
#     print()
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=' ')
#     print()
# # user defined input
# rows=int(input('Enter the no of rows'))
# for i in range(5):
#     for j in range(i):
#         print("%",end=' ')
#     print()
rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
#
