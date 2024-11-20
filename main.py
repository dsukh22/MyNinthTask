import random


def Print_Menu() -> str:
    choice = input("1. Создание массивов\n"
                   "2. Выполнение алгоритма\n"
                   "3. Вывод результата\n"
                   "4. Завершение работы программы\n")
    return choice


def Auto_Generating_Arrays() -> list:
    size = random.randint(2, 10)

    array1 = list(map(lambda _: random.randint(1, 100), range(size)))
    array2 = list(map(lambda _: random.randint(1, 100), range(size)))
    array3 = list(map(lambda _: random.randint(1, 100), range(size)))

    return [array1, array2, array3]


def Self_Creating_Arrays():
    arrays = [[], [], []]
    try:
        arrays_size: int = int(input("Введите размер массивов: "))
    except:
        input("Размер массивов введён некорректно!\n"
              "Нажмите любую клавишу, чтобы продолжить")
        return
    for index, array in enumerate(arrays):
        for _ in range(arrays_size):
            try:
                array += [int(input(f"Введите число ({index + 1} массив): "))]
            except:
                input("Необходимо вводить именно числа, в противном случае создать массив не получится.\n"
                      "Нажмите любую клавишу, чтобы продолжить")
                return
    return arrays


if __name__ == "__main__":
    test_arrays = Self_Creating_Arrays()
    print(test_arrays)
