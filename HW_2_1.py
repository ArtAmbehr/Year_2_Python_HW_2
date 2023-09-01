# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки (не для решения!) своего результата.

def main():
    decToHex(int(input("Введите целое число: ")))

def decToHex(dec_value):
    while dec_value > 0:
        hex_value=dec_value%16
        dec_value=dec_value//16
        print(getHexChar(hex_value),end="")

def getHexChar(dec_digit):
    if dec_digit < 10:
        return dec_digit
    if dec_digit == 10:
        return "A"
    if dec_digit == 11:
        return "B"
    if dec_digit == 12:
        return "C"
    if dec_digit == 13:
        return "D"
    if dec_digit == 14:
        return "E"
    if dec_digit == 15:
        return "F"

main() 
print('\n')

num = int(input("Проверка результата при помощи hex - введите то же число: "))
hex_num = hex(num)

print("Шестнадцатеричное представление числа:", hex_num)