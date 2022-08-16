def binaryConvert(n):
    return bin(n).replace("0b","")
def decimalConvert(d):
    return int(d,2)
def octalConverter(o):
    return oct(o)
def hexConverter(h):
    return hex(h)

dec=int(input("Enter the decimal you want to convert into binary: "))
print(binaryConvert(dec))

Bin=input("Enter the decimal number you want to convert into decimal: ")
print(decimalConvert(Bin))

Oct=int(input("Enter the decimal numnuber you want to convert into octal: "))
print(octalConverter(Oct))

Hex=int(input("Enter the decimal number yoy want to convert into hexadecimal: "))
print(hexConverter(Hex))

    