def num_input():
    while True:
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        if a > 0 or b > 0:
            break
        else:
            print("Please, enter ONLY positive numbers! Try again...")
    return a, b


def mat(x, y):
    boole = True
    if x % y != 0:
        boole = False
    return boole


def main():
    while True:
        try:
            num1, num2 = num_input()
            var = num1 / num2
            break
        except ValueError:
            print("It`s not a right number.  Try again...")
        except ZeroDivisionError:
            print("You can`t divide on 0. Try again...")

    print(str(mat(num1, num2)))


if __name__ == '__main__':
    main()
