a = int(input("enter x \n"))

if 1 <= a <= 10000000000:
    b = int(input("enter y \n"))
    if 1 <= b <= 10000000000:
        print(a + b)
        print(a - b)
        print(a * b)

    else:
        print("b in not a valid number")

else:
    print("a in not a valid number")
