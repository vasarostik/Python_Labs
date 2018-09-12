from second import mat


def input_numbers():
    while True:
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        if a > 0 or b > 0:
            break
        else:
            print("Please, enter ONLY positive numbers! Try again...")
    return a, b


num1, num2 = input_numbers()


def simple(x, y):
    new_list = []
    k = 0

    for i in range(x, y + 1):
        for j in range(2, i + 1):
            if __name__ == '__main__':
                var = mat(i, j)
            if var is True: k += 1
            if k > 1: break
        if k == 1:
            new_list.append(i)
            k = 0
        else:
            k = 0
    if not new_list:
        print("NoSimpleDigits")
    else:
        print(new_list)


simple(num1, num2)
