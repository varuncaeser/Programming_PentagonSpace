#---------------------------------
#to merge two sorted arrays
#using sort
# l1 = [1, 2, 3,65]
# l2 = [4, 5, 6]
#
# i = l1[0]
# j = l2[0]
# for i in range(len(l1)):
#     if i < j:
#         l2.append(l1[i])
# l3 = sorted(l2)
# print(l3)
#------------------------------------
#functional approach without sort
# def merge_sort(l1,l2):
#     i=0
#     j=0
#     res=[]
#     while j<len(l2) and i<len(l1):
#         if l1[i]<l2[j]:
#             res.append(l1[i])
#             i+=1
#         else:
#             res.append(l2[j])
#             j=j+1
#     while i < len(l1):
#         res.append(l1[i])
#         i+=1
#     while j < len(l2):
#         res.append(l2[j])
#         j+=1
#     return res
# l1=[2,3,4,5]
# l2=[12]
# result = merge_sort(l1,l2)
# print(result)
#----------------------------------------
#merging two descending arrays into one ascending array
#using sort method
# def merge_sort(l1,l2):
#     i=0
#     j=0
#     res=[]
#     while j<len(l2) and i<len(l1):
#         if l1[i]<l2[j]:
#             res.append(l1[i])
#             i+=1
#         else:
#             res.append(l2[j])
#             j=j+1
#     while i < len(l1):
#         res.append(l1[i])
#         i+=1
#     while j < len(l2):
#         res.append(l2[j])
#         j+=1
#     return res
# l1=[90,80,70,60]
# l2=[95,65,5,4,3,2,1]
# result = merge_sort(l1,l2)
# res=sorted(result)
# print(res)
#------------------------------
# def merge_sort(l1, l2):
#     i = len(l1) - 1
#     j = len(l2) - 1
#     res = []
#     while j >= 0 and i >= 0:
#         if l1[i] < l2[j]:
#             res.append(l1[i])
#             i -= 1
#         else:
#             res.append(l2[j])
#             j = j - 1
#     while i >= 0:
#         res.append(l1[i])
#         i -= 1
#     while j >= 0:
#         res.append(l2[j])
#         j -= 1
#     return res
#
#
# list1= [90, 80, 70, 60]
# list2 = [95, 65, 5, 4, 3, 2, 1]
# result = merge_sort(list1, list2)
# print(result)
#--------------------
##----BUBBLE SORT----##
# def bubble_sort(l1):
#     for k in range(len(l1) - 1):
#         for i in range(len(l1) - 1):
#             if l1[i] > l1[i + 1]:
#                 l1[i],l1[i + 1]=l1[i + 1],l1[i]
#     return l1
# list1=[8,143,420,6106,90,69,120,18]
# list1=bubble_sort(list1)
# print(list1)
#--------------------------------
#descending order bubble sort
# def bubble_sort(l1):
#     for k in range(len(l1) - 1):
#         for i in range(len(l1) - 1):
#             if l1[i] < l1[i + 1]:
#                 l1[i], l1[i + 1] = l1[i + 1], l1[i]
#     return l1
#
#
# list1 = [8, 143, 420, 6106, 90, 69, 120, 18]
# list1 = bubble_sort(list1)
# print(list1)
#--------------------------------
from array import array
#----------------------------
#merge sort
# def merge(l1, l2):
#     merged_list = l1 + l2
#     return merged_list
#
# def bubble_sort(lst: list) -> list:
#     for k in range(len(lst) - 1):
#         for i in range(len(lst) - 1):
#             if lst[i] > lst[i + 1]:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#     return lst
#
# list1 = [8, 143, 420, 6106]
# list2 = [90, 60, 18]
# merged_list = merge(list1, list2)
# sorted_list = bubble_sort(merged_list)
#
# print(sorted_list)



#merge sort -2---------------DOUBT
# def merge(l1: object, l2: object) -> object:
#     for k, l in range(len(l1) - 1, len(l2) - 1):
#         for i, j in range(len(l1, l2)):
#             if l1[i] > l1[i + 1] and l2[j] > l2[j + 1]:
#                 l1[i], l1[i + 1], l2[j], l2[j + 1] = l1[i + 1], l1[i], l2[j + 1], l2[j]
#
#     return l1, l2
#
#
# def bubble_sort(list):
#     for k in range(len(list) - 1):
#         for i in range(len(list) - 1):
#             if list[i] < list[i + 1]:
#                 list[i], list[i + 1] = list[i + 1], list[i]
#     return list
#
#
#
# list1 = [8, 143, 420, 6106]
# list2 = [90, 60, 18]
# list: object = merge(list1, list2)
# print(list)
