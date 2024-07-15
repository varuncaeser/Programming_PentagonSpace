def add_digit(num):
    sum=0
    while(num!=0):
        rem=num%10
        sum=sum+rem
        num=num//10
    return num
num=14
num1=num+1
while(add_digit(num)*2!=add_digit(num1)):
    num1+=1
print(num1)