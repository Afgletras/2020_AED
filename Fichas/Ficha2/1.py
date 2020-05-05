def findmin_n(lista):
    min_n = lista[0]
    for i in lista:
        if i < min_n:
            min_n = i
    return min_n

def findmin_n2(alist):
    for i in alist:
        i_is_min = True
        for j in alist:
            if j < i:
                i_is_min = False
            j = j + 1
        if i_is_min:
            return i

    return min


def main():
    my_list = [20, 40, 10, 30, 25, 50, 85, 15]
    print("O(n):", findmin_n(my_list))
    print("O(n^2):", findmin_n2(my_list))


if __name__ == '__main__':
    main()
