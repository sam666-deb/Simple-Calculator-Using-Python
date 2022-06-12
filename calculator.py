def addition(num1, num2):
    return num1+num2


def subtrection(num1, num2):
    return num1-num2


def Multiplication(num1, num2):
    return num1*num2


def Divition(num1, num2):
    return num1//num2


def Moduls(num1, num2):
    return num1 % num2


def Takeinput():
    num1 = int(input("Enter First number: "))
    num2 = int(input("Enter Second number: "))

    return num1, num2


def main():
    while True:
        print("************ Simple Calculator ****************")
        print("1. Add\n2. SubTract\n3. Multiply\n4. Divide\n5. Moduls\n6 Exit.")
        print()
        option = int(input("Select What you want to DO: "))

        if(option == 1):
            num1, num2 = Takeinput()
            print(f'{num1}+{num2}={addition(num1,num2)}')
        elif option == 2:
            num1, num2 = Takeinput()
            print(f'{num1}-{num2}={subtrection(num1,num2)}')
        elif option == 3:
            num1, num2 = Takeinput()
            print(f'{num1}x{num2}={Multiplication(num1,num2)}')
        elif option == 4:
            num1, num2 = Takeinput()
            print(f'{num1}÷{num2}={Divition(num1,num2)}')
        elif option == 5:
            num1, num2 = Takeinput()
            print(f'{num1}%{num2}={Moduls(num1,num2)}')
        elif option == 6:
            print(f'************ Thank You For Using Our Product!!! *************')
            break
        else:
            print("Invalid Input Try again!!!")


if __name__ == '__main__':
    main()
