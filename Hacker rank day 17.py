# #between two sets
# def totalx(a,b):
#     count=1
#     start=max(a)
#     end=min(b)+1
#     for i in range(start,end):
#             good=True
#             for value in a:
#                 if i %value != 0:
#                     good=False
#             for value in b:
#                 if value % i != 0:
#                     good=False
#             if good == True :
#                 count+=1
#             return count
# a=[2,6]
# b=[24,36]
# res=totalx(a,b)
# print(res)
#breaking the records

def breakingRecords(scores):
    # Write your code here
    min_value = scores[0]
    max_value = scores[0]
    max = 0
    min = 0
    ans = []
    for value in scores:
        if value > max_value:
            max_value = value
            max += 1
        if value < min_value:
            min_value = value
            min += 1
    ans.append(max)
    ans.append(min)
    return ans
scores=[10,5,20,20,4,5,2,25,1]
ans=breakingRecords(scores)
print(ans)