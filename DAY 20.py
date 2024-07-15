# write a pgm wheather the given two strings are anagram or not
#METHOD 1 using inbuilt methods#
# def are_anagrams(str1, str2):
#     # Remove spaces and convert to lower case
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
#
#     # Check if sorted strings are equal
#     return sorted(str1) == sorted(str2)
#
#
# # Test the function
# str1 = "L isten"
# str2 = "S ilent"
# print(are_anagrams(str1, str2))  # Output: True
#--------------------METHOD 2
# def anagram(str1,str2):
#     dict1={}
#     dict2={}
#     for char in str1:
#         if char in dict1:
#             dict1[char] += 1
#         else:
#             dict1[char] = 1
#     for char in str2:
#         if char in dict2:
#             dict2[char] += 1
#         else:
#             dict2[char] = 1
#     return dict1,dict2
# str1=input()
# str2=input()
# dict1,dict2=anagram(str1,str2)
# if dict1==dict2:
#     print("ANAGRAM")
# else:
#     print("NOT")
#-------------------------------------------
#sort function-METHOD 3
# def check(s,s2):
#     if(sorted(s)==sorted(s2)):
#         print("anangram")
#     else:
#         print("not")
# s="silent"
# s2="listen"
# check(s,s2)
#--------------------------
#string to list -METHOD 4
# def check_Anagram(s1,s2):
#     arr1= []
#     arr2 =[]
#     for char in s1:
#         arr1.append(char)
#     for char in s2:
#         arr2.append(char)
#     arr1.sort()
#     arr2.sort()
#     if arr1==arr2:
#         print("Anagram")
#     else:
#         print("NOT")
# s1=input()
# s2=input()
# check_Anagram(s1,s2)
#Write a pgm to print all the substrings of a given string
# def sub_string(s):
#     for i in range(len(s)):
#         for j in range(i,len(s)):
#             print(s[i:j+1])
# s=input()
# sub_string(s)
#Sub-string---> Contigeous sequence of char within a given string and mainting the order of the main string
#Sub-sequence--> Sequence derived by deleting or not deleting elements and mainting the order of the main string
#write a pgm to print the substrings only if the sub string is pallindrome

# def reverse(s):
#     res=""
#     for char in s:
#         res=char+res
#     return res
# def sub_string(s):
#     for i in range(len(s)):
#         for j in range(i,len(s)):
#             ans=(s[i:j+1])
#             if reverse(ans)==ans:
#                 print(ans)
# s=input()
# sub_string(s)
#write a pgm to print longest pallindrome sub-string
# def reverse(s):
#     res = ""
#     for char in s:
#         res = char + res
#     return res


# def sub_string(s):
#     longest = 0
#     longest_str = ''
#     for i in range(len(s)):
#         for j in range(i, len(s)):
#             ans = (s[i:j + 1])
#             if (reverse(ans) == ans and len(ans) > longest):
#                 longest_str = ans
#                 longest = len(longest_str)
#     print(longest_str)
#
#
# s = input()
# sub_string(s)


#----------------------------------

str=input("Enter the string").lower()
words=str.split()
search=input("Enter the input to search")
dict={ }
for i in words:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for i in dict:
    if search == i:
        print(f" occurence of {search} word is {dict[i]}")
    break

