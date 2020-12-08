a = 10
b = 30
print("a : " + str(a))
print("b : " + str(b))
mode = 1 # 1,+ 2,- 3,* 4,/
if mode == 1:
    print("a + b = " + str(a + b))
elif mode == 2:
    print("a - b = " + str(a - b))
elif mode == 3:
    print("a * b = " + str(a * b))
elif mode == 4:
    print("a / b = " + str(a / b))
else:
    print("Error: illegal mode number")