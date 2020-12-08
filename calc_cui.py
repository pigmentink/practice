a = int(input("a >>"))
b = int(input("b >>"))
print("select mode 1...+(Addition) 2...-(Subtraction) 3...*(Multiply) 4.../(division)")
mode = int(input("mode:")) # 1,+ 2,- 3,* 4,/
# modeに沿って計算する
if mode is 1:
    print("a + b = " + str(a + b))
elif mode is 2:
    print("a - b = " + str(a - b))
elif mode is 3:
    print("a * b = " + str(a * b))
elif mode is 4:
    print("a / b = " + str(a / b))
else:
    print("Error: illegal mode number")