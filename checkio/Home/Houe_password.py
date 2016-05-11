def checkio(data):
    import re
    if len(data) < 10:
        return False
    elif re.search("[a-z]+", data) is None:
        return False
    elif re.search("[A-Z]+", data) is None:
        return False
    elif re.search("[0-9]+", data) is None:
        return False
    else:
        return True
    