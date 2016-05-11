def checkio(game_result):
    horizon = game_result
    vertic = [''.join(h[i] for h in horizon) for i in range(3)]
    NW = ''.join([game_result[i][i] for i in range(3)])
    NE = ''.join([game_result[i][2-i] for i in range(3)])
    all = [horizon, vertic, NW, NE]
    for i in all:
        if "XXX" in i:
            return "X"
            break
        elif "OOO" in i:
            return "O"
            break
    else:
        return "D" 
