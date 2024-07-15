# #MERGE SORT
# # #DIVIDE & CONQUER METHOD#
# def divide(list):
#     if len(list) == 1:
#         return list
#     mid = len(list) // 2
#     left = list[:mid]
#     right = list[mid:]
#     left = divide(left)
#     right = divide(right)
#     return merge_todolist(left, right)
#
#
# def merge_todolist(l1, l2):
#     res = []
#     i = 0
#     j = 0
#     while i < len(l1) and j < len(l2):
#         if (l1[i] < l2[j]):
#             res.append(l1[i])
#             i += 1
#         else:
#             res.append(l2[j])
#             j += 1
#     while i < len(l1):
#         res.append(l1[i])
#         i += 1
#     while j < len(l2):
#         res.append(l2[j])
#         j += 1
#     return res
# #
#
# list = [90, 60, 120, 6106, 18, 69]
# res = divide(list)
# print(res)
# #--------------------------------------
# #METHOD ONE MORE[RECURSIVE]
# def merge_sort(L):
#     if len(L)==1:
#         return L
#     return merge_todolist(merge_sort(L[:len(L)//2]),merge_sort(L[len(L)//2:]))
# def merge_todolist(l1, l2):
#     res = []
#     i = 0
#     j = 0
#     while i < len(l1) and j < len(l2):
#         if (l1[i] < l2[j]):
#             res.append(l1[i])
#             i += 1
#         else:
#             res.append(l2[j])
#             j += 1
#     while i < len(l1):
#         res.append(l1[i])
#         i += 1
#     while j < len(l2):
#         res.append(l2[j])
#         j += 1
#     return res
# L = [90, 60, 120, 6106, 18, 69]
# res = merge_sort(L)
# print(res)
#
#
