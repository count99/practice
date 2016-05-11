#coding="utf-8"
#http://www.jisuanke.com/course
#problem's solve in python 2.7
matrix = raw_input()
i = 0
full_matrix = []
while i < int(matrix[0]): 
    N = raw_input()
    N = N.split(" ")
    i += 1
    full_matrix.append(N)

if int(matrix[4])==1:
    n=[]
    for i in range((len(full_matrix)-1), -1, -1):
        n.append(full_matrix[i])
elif int(matrix[4])==0:
    n=[]
    for i in range(len(full_matrix)):
        temp_n = []
        for j in range(len(full_matrix[i])-1, -1, -1):
            temp_n.append(full_matrix[i][j])
        n.append(temp_n)
            
for i in range(len(n)):
    a=" ".join(n[i])
    print("{} ".format(a))