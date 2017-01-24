def test1(fun):
    def wrapper(aa):
        print("fuck off")
        me = fun(aa)
        print("測試啊")
        return me
    return wrapper

@test1
def good(aa):
    print("Orign",aa)
    return "返回啊"

i = good("gan")
print(i)