# s=input("enter the string")
# print(s)
# str="varun"
#write a pgm to reverse a string
# def reverse(S):
#     res = ""
#     for char in S:
#         res = char+res
#     return res
#
#
# S = "MALAYALAM"
# rev = reverse(S)
# print(rev)
# if S != rev:
#     print("NOT")
# else:
#     print("Palindrome")
#------------------------------------------
# write a pgm to count number of vowels present in a string
# def count(s):
#     count=0
#     for i in s:
#         if i in "aeiouAEIOU":
#             count+=1
#     return (count)
# s="helloHELLO"
# no_of_vowels=count(s)
# print(no_of_vowels)
# ----------------------------------
# #write a pgm to print no of vowels,consonents,white spaces [assuming string has white spaces and no special char and uppercase]
# def count(s):
#     count_vowels=0
#     count_consonants=0
#     count_whitespace=0
#     for i in s:
#         if i in "aeiou":
#             count_vowels+=1
#         elif i in " ":
#             count_whitespace+=1
#         else:
#             count_consonants+=1
#     return  count_consonants,count_vowels,count_whitespace
#     # print("count_vowels:",count_vowels)
#     # print("count_consonants:", count_consonants)
#     # print("count_whitespace:",count_whitespace)
# s=" v a r un "
# v_count,c_count,w_count=count(s)
# print(v_count,c_count,w_count)
#------------------------------------------------
#to get GFECB as output
# def assci(s):
#     rev = ""
#     for i in s:
#         rev = chr(ord(i)+1)+rev
#     return rev
# s="ABDEF"
# rev=assci(s)
# print(rev)
#----------------------------------------
s = "Virat is running"
#running is Virat
# words = s.split()  # Split the string into words
# reversed_words = words[::-1]  # Reverse the order of the words
# output = " ".join(reversed_words) # Join the words back into a string
# print(output)

# tariV si gninnur
# words = s.split()  # Split the string into words
# reversed_words = words[::-1]  # Reverse the order of the words
# output = " ".join(reversed_words) # Join the words back into a string
# print(output)
# rev = ""
# for i in output:
#     rev = i + rev
# print(rev)

#Virat Is Running
# words = s.split()  # Split the string into words
# capitalized_words = [word.capitalize() for word in words]  # Capitalize each word
# output = " ".join(capitalized_words)  # Join the capitalized words

# print(output)

# ## gninnur si tariV
#
# def reverse(s):
#     rev = ""
#     for i in s:
#         rev = i + rev
#     return rev
#
#
# res1 = reverse(s)
# print(res1)


