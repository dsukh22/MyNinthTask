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


if __name__ == "__main__":
    first_test = Auto_Generating_Arrays()
    for array in first_test:
        print(array, len(array))

    print("=========================")

    second_test = Auto_Generating_Arrays()
    for array in second_test:
        print(array, len(array))

    print("=========================")

    third_test = Auto_Generating_Arrays()
    for array in third_test:
        print(array, len(array))
        