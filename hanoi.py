def hanoi(n, sourse, helper, target):
    if n is 1:
        print("將{}移動到{}".format(sourse, target))
    else:
        hanoi(n-1, sourse, target, helper)         
        print("將{}移動到{}".format(sourse, target))
        hanoi(n-1, helper, sourse , target)

if __name__ == "__main__":
    n=int(input("請輸入層數? "))
    hanoi(n, "A", "B", "C")