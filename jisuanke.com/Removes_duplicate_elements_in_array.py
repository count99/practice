#coding="utf-8"
n = input()
n_array = input().split(" ")
print(n_array)
count = 1
for i in range(len(n_array)-1):
    if n_array[i] == n_array[i+1]:
        continue
    else:
        count += 1
print (count)