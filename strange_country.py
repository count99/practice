#coding="utf-8"
first_numer = input()
second_number = input()
output_number = []
for i in range(len(first_numer)):
    if (int(first_numer[i])==1 and int(second_number[i])==1) or (int(first_numer[i])==0 and int(second_number[i])==0):
        output_number.append(1)
    else:
        output_number.append(0)
result_number=""
for i in output_number:
    result_number += str(i)
print(result_number)