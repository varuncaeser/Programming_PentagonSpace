#sub array division
# def birthday(s, d, m):
#     count =0
#     for i in range(len(s) - m +1):
#         sum =0
#         for j in range(i, i+m):
#             sum+=s[j]
#         if sum==d:
#             count+=1
#     return count
# s=[1,2,1,3,2]
# res=birthday(s,3,2)
# print(res)
# # divisible sum pairs

# def divisibleSumPairs(n, k, ar):
#     count = 0
#     for i in range(len(ar)):
#         for j in range(i + 1, len(ar)):
#             if ((ar[i] + ar[j]) % k == 0):
#                 count += 1
#     return count
# ar=[1,2,3,4,5,6]
# n=6
# k=5
# res=divisibleSumPairs(n,k,ar)
# print(res)


def migratoryBirds(arr):
    # Write your code here
    dict={}
    for i in arr:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
    print(max(dict))
arr=[1,2,4,4,4]
migratoryBirds(arr)
