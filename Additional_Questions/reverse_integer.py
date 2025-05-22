integer = int(input("Enter an integer: "))
reversed_int = 0
number = abs(integer)
while number > 0:
    modulu = number % 10
    number = number // 10
    reversed_int= reversed_int * 10+modulu
# print("Reversed integer:", reversed_int)123
if integer < 0:
    reversed_int = -reversed_int
print("Reversed integer:", reversed_int)