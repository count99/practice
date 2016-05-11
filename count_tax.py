def count_tax(number):
    """count china personal income tax"""
    tax_standard = number-3500
    if tax_standard < 0:
        tax = 0
    else:
        if tax_standard >= 0 and tax_standard < 1500:
            tax = tax_standard*0.03
        elif  tax_standard >= 1500 and tax_standard < 4500:
            tax = (tax_standard-1500)*0.1+1500*0.03
        elif tax_standard >= 4500 and tax_standard < 9000:
            tax = (tax_standard-4500)*0.2+(4500-1500)*0.1+1500*0.03
        elif tax_standard >= 9000 and tax_standard < 35000:
            tax = (tax_standard-9000)*0.25+(9000-4500)*0.2+(4500-1500)*0.1+1500*0.03
        elif tax_standard >= 35000 and tax_standard < 55000:
            tax = (tax_standard-35000)*0.3+(35000-9000)*0.25+(9000-4500)*0.2+(4500-1500)*0.1+1500*0.03
        elif tax_standard >= 55000 and tax_standard < 80000: 
            tax = (tax_standard-55000)*0.35+(55000-35000)*0.3+(35000-9000)*0.25+(9000-4500)*0.2+(4500-1500)*0.1+1500*0.03    
        elif tax_standard >= 80000:
            tax= (tax_standard-80000)*0.45+(80000-55000)*0.35+(55000-35000)*0.3+(35000-9000)*0.25+(9000-4500)*0.2+(4500-1500)*0.1+1500*0.03
        return tax
    
if __name__=="__main__":
    number = int(input("請輸入所得金額? "))
    tax = count_tax(number)
    print("所需繳納所得稅{}".format(tax))