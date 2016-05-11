#codeing="utf-8"
count = 0
kid_dict={}
while True:
    n = input()
    if int(n) is -1:
        break
    else:
        kid_data = []
        for i in range(int(n)):
            data = input()
            data = data.split(" ")
            kid_data.append(data)
        kid_dict[count]=kid_data
        count += 1
for i in range(count):
    sum_cube_list = []
    sum_name_list = []
    for j in kid_dict[i]:
        sum_cube = 1 
        for k in range(0, 3):
            sum_cube *= int(j[k])
        sum_cube_list.append(sum_cube)
        sum_name_list.append(j[3])
    else:
        sum_cube_max_index=sum_cube_list.index(max(sum_cube_list))
        sum_cube_min_index=sum_cube_list.index(min(sum_cube_list))
        print("{} took clay from {}.".format(sum_name_list[sum_cube_max_index], sum_name_list[sum_cube_min_index]))
    