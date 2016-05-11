def checkio(number):
    ones_table = {
                    "1":"one", "2":"two", "3":"three", "4":"four", "5":"five",
                    "6":"six", "7":"seven", "8":"eight", "9":"nine", "10":"ten",
                    "11":"eleven", "12":"twelve", "13":"thirteen", "14":"fourteen",
                    "15":"fifteen", "16":"sixteen", "17":"seventeen", "18":"eighteen",
                    "19":"nineteen", "0":""
                    }
    tens_table={    
                    "2":"twenty", "3":"thirty", "4":"forty",
                    "5":"fifty", "6":"sixty", "7":"seventy", "8":"eighty",
                    "9":"ninety"
                    }
    if number < 20:
        return ones_table[str(number)]
    elif number < 100 and number > 19:
        tens = number // 10
        ones = number % 10
        if ones == 0:
            return " ".join([tens_table[str(tens)]])
        else:
            return " ".join([tens_table[str(tens)], ones_table[str(ones)]])
    else:
        if number % 100 == 0:
            return " ".join([ones_table[str(number//100)], "hundred"])
        else:
            return " ".join([ones_table[str(number//100)], "hundred", checkio(number%100)])
    
print checkio(4)
print checkio(143)
print checkio(12)
print checkio(101)
print checkio(212)
print checkio(40)