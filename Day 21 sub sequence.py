def sub_sequence(str, res):
    if len(str)==0:
        print(res)
        return
    sub_sequence(str[1:], res + str[0])
    sub_sequence(str[1:], res)
str='abc'
res=''
sub_sequence(str, res)