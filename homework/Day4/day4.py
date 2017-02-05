# coding = “utf-8”
# 看完老男孩寫的模擬人生

class Person(object):
    """"人物類"""
    def __init__(self, **na):
        self.name = na["name"]
        self.sexuality = na["sexuality"]
        self.job = na["job"]
        self.incomes = na["incomes"]
        self.specialty = na["specialty"]

    def change_income(self, amount):
        self.incomes += amount

    def change_job(self, new_job):
        self.job = new_job

    def change_specialty(self, new_specialty):
        if new_specialty not in self.specialty:
            self.specialty.append(new_specialty)

user_name = str(input("請輸入姓名 ?\t"))
user_info = {"name":user_name, "sexuality":"Male", "job":"學生", "incomes":0, "specialty":[]}
player = Person(**user_info)