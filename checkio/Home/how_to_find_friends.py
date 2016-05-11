def check_connection(network, first, second):
    networks=[]
    for i in network:
        networks.append(i.split("-"))
    flag=1
    while flag > 0:
        for i in networks:
            temp = i
            networks.remove(i)
            set_temp = set(temp)
            for j in range(len(temp)):
                for k in networks:
                    set_k = set(k)
                    if (temp[j] in k) and not(set_temp <= set_k):
                        networks.remove(k)
                        a=(set_temp|set_k)
                        a = list(a)
                        networks.append(a)
                        flag +=1
        else:
            if flag > 1:
                flag = 1
            elif flag ==1:
                networks.append(temp)
                flag = 0
    check_list={first, second}
    return_flag = False
    for i in networks:
        if check_list <= set(i):
            return_flag = True
    return return_flag


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
