def check_io(data):
    copy_data = tuple(data)
    for i in copy_data:
        if data.count(i) == 1:
            data.remove(i)
    return data

a = [1, 2, 3, 4, 5]
print check_io(a)