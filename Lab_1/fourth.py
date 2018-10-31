my_list = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]


def merger(massive):
    new_list = []
    for elt in massive:
        t = type(elt)
        print("\n" + str(type(elt)))
        if t is tuple or t is list:
            for i in merger(elt):
                new_list.append(i)
        else:
            new_list.append(elt)
    return new_list


print(merger(my_list))
