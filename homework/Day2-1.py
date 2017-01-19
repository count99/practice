# coding = UTF-8
# Homework Buy

def buystuffs():
    suffs = ["apple", "poneapple", "grapes", "banana", "watermelon"]
    price = [100, 120, 150, 70, 200]
    salary = int(input("Please input your salary?  "))
    buyed = []
    flag = 0
    limit_badges = salary
    while flag == 0:
        print("====================")
        for i in suffs:
            print(i)
        else:
            print("Quit")
            print("====================")
        choice_fruit = input("Please input what do you need?\n")
        if choice_fruit in suffs:
            limit_badges = limit_badges - price[suffs.index(choice_fruit)]
            buyed.append(choice_fruit)
            print("Now you left {}".format(limit_badges))
            if limit_badges < 70:
                print("You can't buy any more")
                flag = 1
        elif choice_fruit == "Quit" or choice_fruit =="quit":
            flag = 1
        else:
            print("Please input the right fruit")
    else:
        print("Thanks for using.")
        print("You have bought")
        print("==========")
        for i in buyed:
            print(i)
        print("==========")
        print("You still have {}".format(limit_badges))

if __name__ == "__main__":
    buystuffs()