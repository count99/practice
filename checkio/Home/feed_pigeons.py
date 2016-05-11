#coding="uft-8"
def checkio(number):
    """If We have number portions of bird feed, how many 
    pigeons will be fed with at lastone portion of wheat?"""
    
    food = number
    birds = 0
    for i in range(1, number+1):
        birds += i
        food -= birds
        if food == 0:
            break
        elif food < 0:
            if (birds + food) > (birds - i):
                birds = birds + food 
                break
            else:
                birds -= i
    return birds

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
    assert checkio(3) == 2, "5th example"