#coding=utf-8
import random

def MontyHall(change):
    selects_list = [1,0,0]
    random.shuffle(selects_list)
    choices = random.randint(0,2)
    if selects_list[choices]==1 and change==0:
        hit=1
    elif selects_list[choices]==0 and change==1:
        hit=1
    else:
        hit=0
    return hit

def choice_change(rechange, times):
    win=0
    if rechange == 2:
        for i in range(times):
            change=random.randint(0,1)
            if MontyHall(change):
                win += 1
    else:    
        for i in range(times):
            if MontyHall(rechange):
                win += 1
    return float(win/times*100)

if __name__=="__main__":
    print("确定改变选择的中奖概率=%f" % choice_change(1, 10000))
    print("确定不改变选择的中奖概率=%f" % choice_change(0, 10000))
    print("不确定是否改变选择的中奖概率=%f" % choice_change(2, 10000))
    