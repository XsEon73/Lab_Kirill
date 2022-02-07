import random as rd


def arr_input():
    """
    Ввод данных
    :return:
    """
    print("Введите тип ввода - auto/class:")
    x = input()
    if x == "auto":
        print("Введите кол-во элементов:")
        n = input()
        arr = [rd.randint(1, 10) for i in range(int(n))]
        return arr
    elif x == "class":
        arr = [int(n) for n in input().split()]
        return arr
    else:
        print("Ошибка ввода")


def resh(x):
    """
    Из списка удаляем цепочки из четных элементов, состоящие менее чем из трех элементов
    :param x: Список
    :return:
    """
    k = 0
    i = 0
    m = len(x)
    while i < m:
        if x[i] % 2 == 1:
            k += 1
        if x[i] % 2 == 0 or i == m-1:
            if k > 0 and k < 3:
                if i-1 == 0:
                    del x[i-1]
                    i -= 1
                    m -= 1
                elif i == m - 1:
                    del x[i]
                else:
                    del x[i-k:i]
                    i -= k
                    m -= k
                k = 0
            else:
                k = 0
        i += 1


x = arr_input()
print(x)
resh(x)
print(x)

