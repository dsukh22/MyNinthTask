import random


def Print_Menu() -> str:
    choice = input("1. Создание массивов\n"
                   "2. Выполнение алгоритма\n"
                   "3. Вывод результата\n"
                   "4. Завершение работы программы\n")
    return choice


def Creating_Arrays_Dialogue():
    mode: str = input("Выберите режим создания массивов:\n"
                      "1. Автоматический\n"
                      "2. Ручной\n"
                      "Ваш выбор: ")
    match mode:
        case "1":
            my_arrays = Auto_Generating_Arrays()
            return my_arrays
        case "2":
            my_self_arrays = Self_Creating_Arrays()
            return my_self_arrays
        case _:
            input("Такого случая не предусмотрено.\n"
                  "Нажмите любую клавишу, чтобы продолжить")
            return


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


def Checking_Digits(arrays: list):
    results = []

    for i in range(len(arrays[0])):
        sum_ab = arrays[0][i] + arrays[1][i]

        if sum_ab == arrays[2][i]:
            min_value = min(arrays[0][i], arrays[1][i], arrays[2][i])
            result = (arrays[0][i] + arrays[1][i] + arrays[2][i]) ** min_value
            results.append(result)

    return results


if __name__ == "__main__":
    array1 = [1, 2, 3]
    array2 = [2, 4, 7]
    array3 = [3, 5, 10]
    arrays1 = [array1, array2, array3]
    print(Checking_Digits(arrays1))  # [6, 8000]
