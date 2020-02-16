number = int(input("Enter the Year"))


def leapYear(x):
    if 1900 <= x <= 100000:
        if x % 4 == 0:
            if x % 100 == 0:
                if x % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        print("Invalid Year")


print(leapYear(number))
