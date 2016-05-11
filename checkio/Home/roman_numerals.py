#coding="utf-8"
def checkio(data):
    """Converting the digital into a Roman numeral"""
    temp_data_number = []
    roman_numerals_dict = {1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
    while data > 0:
        data, remainder = divmod(data, 10)
        temp_data_number.append(remainder)
    number_digits = [10**x for x in range(len(temp_data_number))]
    number_digits.reverse()
    temp_data_number.reverse()
    roman_numerals_list=[]
    for j in range(len(temp_data_number)):
        if temp_data_number[j]*number_digits[j] in roman_numerals_dict.keys():
            roman_numerals_list.append(roman_numerals_dict[temp_data_number[j]*number_digits[j]])
        else:
            get_character=""
            if temp_data_number[j]>=1 and temp_data_number[j]<4:
                for x in range(temp_data_number[j]):
                    get_character += roman_numerals_dict[number_digits[j]]
            elif temp_data_number[j]>=6 and temp_data_number[j]<9:
                get_character=roman_numerals_dict[5*number_digits[j]]
                for x in range(temp_data_number[j]-5):
                    get_character += roman_numerals_dict[number_digits[j]]
            roman_numerals_list.append(get_character)
    return "".join(roman_numerals_list)      
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
