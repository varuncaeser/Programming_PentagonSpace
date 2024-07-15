#write a pgm to find the max sum of sub array whose size is K?

# def sub_array_sum(array, key):
#     sum_of_elements = 0
#     for i in range(0, key):
#         sum_of_elements += array[i]
#     max_sum = sum_of_elements
#     for i in range(1, len(array) - key + 1):
#         sum_of_elements = 0
#         for j in range(i, key + i):
#             sum_of_elements += array[j]
#         if sum_of_elements > max_sum:
#             max_sum = sum_of_elements
#     return max_sum
#
#
# arr = [8, -6, 3, 4, -1, 6, 3, -4]
# k = 3
# res = sub_array_sum(arr, k)
# print(res)
#write a pgm to remove duplicate values from the list
# def unique(arr):
#     ans=[]
#     for i in arr:
#         if i not in ans:
#             ans.append(i)
#     return ans
# arr=[10,20,20,3,40,40]
# print(unique(arr))
# write the pgm to print the count of occurence,unique and duplicate of a num in array
def occurrence(arr):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    for i in dict:
        print(i, "->", dict[i], end=' ')
        print()
        # if dict[i]>=1:##to print duplicate numbers
        #     print(i)
        #if dict[i]==1:###to print the unique numbers
        #print(i)


arr = [12, 23, 12, 24, 90, 60, 30, 12, 60, 18]
occurrence(arr)

