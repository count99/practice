#coding="utf-8"
n=input()
number_list = input()
number = input()
get_list = [ x for x in number_list if x!=" "]
for i in range(len(get_list)):
    if int(get_list[i]) >= int(number):
        print (i)
        break
else:
    print(len(get_list))