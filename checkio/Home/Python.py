def checkio(data):
    off = len(data) // 2
    data.sort()
    med = data[off] + data[-(off + 1)]
    return med / 2
    
a = [1, 2, 3, 4, 5]
print checkio(a)