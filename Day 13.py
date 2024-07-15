####-----lISTS-----####
#List insertion
# #In list insertion we need to specify the len of list and while creating we do not need .
# n=int(input("Enter the value of n"))
# L=[]
# for i in range(n):
#     data=int(input("Enter the value"))
#     L.append(data)
# print(L)
#------------------------------------------
#to print the even elements in a list
# L=[12,23,45,67,98,100]
# for i in range(0,len(L)):
#     data=L[i]
#     if data%2==0:
#         print(data)
#-------------------------------------

#to print the elements at even indeces
# L=[12,23,45,67,98,100]
# for i in range(0,len(L)):
#     data=L[i]
#     if i%2==0:
#         print(L[i])##print(data)
#-----------------------------------
#to print the sum & avg of given num in a list
# l=[1,2,3,4,98,45,23]
# sum=0
# for i in range(0,len(l)):
#     data=l[i]
#     sum=data+sum
# print(sum)
# avg=sum/len(l)
# print(avg)
# #----------to print max element in list
# L=[1,2,3,5,45]
# max=0
# for i in range(len(L)):
#     max=L[i]
# print(max)
# #-----------to print min element in list
# L=[1,2,3,5,45]
# min=L[0]
# for i in range(len(L)):
#     max=L[i]
# print
#---------method 2 -max
# L=[1,2,3,4]
# max=0
# for i in range(len(L)):
#     data: int = L[i]
#     if data > max:
#         max = data
# print(max)
#----------- if the list has -ve elements we take max as L[0] or any element index from list
# L=[-1,-2,-3,-4]
# max=L[0]
# for i in range(len(L)):
#     data: int = L[i]
#     if data > max:
#         max = data
# print(max)
#to find the second max element in list
##----WORST CASE----####
# l = [1,3,4,7,9]
# max = l[0]
# for i in range(len(l)):
#     data: int = l[i]
#     if data > max:
#         max = data
# print(max)
# max1=max
# n=float(input("enter n"))
# l.append(n)
# print(l)
# print(max)
# for i in range(len(l)):
#     data: int = l[i]
#     if data > max:
#         max = data
# print(max1)
# print(l)
# # max1 = l[0]
# # for i in range(len(l)):
# #     data: int = l[i]
# #     if data > max1:
# #         max1 = data
# print(max1)
#------------------------
#method by me
# l = [12, 45, 7, 23, 56, 89, 34]
# first_max = l[0]
# second_max = l[0]
#
# i: int
# for i in l:
#     if i > first_max:
#         second_max = first_max
#         first_max = i
#     elif first_max > i > second_max:
#         second_max = i
# print(second_max)
# print(id(second_max))
#method 2
l = [-12, 23, 5, 12, 344, 344]
if l[0] > l[1]:
    max1 = l[0]
    max2 = l[1]
else:
    max1 = l[1]
    max2 = l[0]
for i in range(2, len(l)):
    if l[i] > max1:
        max2 = max1
        max1 = l[i]
    elif l[i] > max2:
        max2 = l[i]
print(id(max2))
print(id(max1))
print(max1)
print(max2)
