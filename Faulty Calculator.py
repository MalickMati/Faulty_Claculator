#Except these calculations, every calculation is done properly
#  45 * 3 = 555 , 56 + 9 = 77 , 56 / 6= 4

print("Enter your choice: * , / , - , + ")
operator = input()
print("Enter First value: ")
val1 = int(input())
print("Enter Second value: ")
val2 = int(input())

if val1 == 45 and val2 == 3 and operator == "*" :
    print("555")
elif val1 == 56 and val2 == 9 and operator == "+" :
    print("77")
elif val1 == 56 and val2 == 6 and operator == "/" :
    print("4")
elif operator == "*":
    ans = val1 * val2
    print(ans)
elif operator == "/":
    ans = val1 / val2
    print(ans)
elif operator == "+":
    ans = val1 + val2
    print(ans)
elif operator == "-":
    ans = val1 - val2
    print(ans)
else:
    print("Check your answer")