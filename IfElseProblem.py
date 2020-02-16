n = int(input("Please Enter a Number :: \n"))

if 1 <= n <= 100:
    if (n % 2) == 0:
        if 2 <= n <= 5:
            print("n is between 2 and 5 : Not Weird")

        elif 6 <= n <= 20:
            print("n is between 6 and 20 : Weird")

        elif n > 20:
            print(" n is greater than 20 : Not Weird")

    else:
        print("n id Odd : So Weird")

else:
    print("Incorrect number try again")
