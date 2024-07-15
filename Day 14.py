#Linear Search
#to get the index of the element & element
# def linear_search(list: object, key):
#     for i in range(0, len(list)):
#         if list[i] == key:
#             return i, True, list[i]
#     return -1
#
#
# list = [1, 2, 3, 4, 54, -1]
# key = -1
# ind = linear_search(list, key)
# print(ind)
#Binary Search
#to get the index of the element & element
from typing import Any, List


# def binary_search(l,key):
#     low=0
#     high=len(l)-1
#     while low<=high:
#         mid=(low+high)//2
#         if l[mid]==key:
#             return mid
#         elif key>l[mid]:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1
# l=[10,1,2,3,4,5,6]
# key=10
# ind=binary_search(l,key)
# print("index and ele are",ind)
