def golf(number):
    p=[x for x in range(2,98690) if not any((x%d==0 for d in range(2,int(x**0.5)+1)))]
    return [i for i in filter(lambda j:str(j)==str(j)[::-1] and j>number, p)][0]

if __name__ == "__main__":
    assert golf(2) == 3 , "2"
    assert golf(13) == 101, "13"
    assert golf(101) == 131, "101"