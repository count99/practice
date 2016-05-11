def checkio(data):
    data_len = len(data)
    data.sort()
    if (data_len % 2) == 0:
        mid = int(data_len/2)
        answer = (data[(mid-1)]+data[mid])/2.0
        return answer
    else:
        return data[int(data_len/2)]
    
