#coding="utf-8"

def safe_pawns(pawns):     
    pawns_index = [tuple([ord(i[0])-96,int(i[1])]) for i in pawns]
    safe = 0
    for i in pawns_index:
        test_minus = (i[0]-1, i[1]-1)
        test_add = (i[0]+1, i[1]-1)
        if (test_add in pawns_index) or (test_minus in pawns_index):
            safe +=1
    return safe

assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1