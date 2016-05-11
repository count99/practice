#coding="utf-8"
n = input()
a_array = input()
remove_number = input()
element_list = a_array.split(" ")
while remove_number in element_list:
    element_list.remove(remove_number)
print(len(element_list))