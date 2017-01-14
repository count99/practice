id = input("請輸入ID=? ")
for i in range(3):
    password = str(input("請輸入密碼＝？"))
    flag = 0
    if password == "good":
        print("密碼正確，登入中")
        flag = 1
        break
    print("密碼錯誤，請重新輸入")
if flag == False:
    print("帳號已鎖定")

