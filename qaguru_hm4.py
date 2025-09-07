def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Alisha"
    age = 29
    # TODO Сформируйте нужную строку
    output = f"Hello, {name}! You're {age} years old."

    # Проверяем результат
    assert output == "Hello, Alisha! You're 29 years old."
    print(output)

def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 20
    b = 30
    # TODO сосчитайте периметр
    perimeter = 2 * (a + b)

    assert perimeter == 100

    # TODO сосчитайте площадь
    area = a * b

    assert area == 600


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23

    # TODO сосчитайте площадь
    area = (r ** 2) * math.pi

    assert area == 1661.9025137490005

    print(f'Площадь круга, S = {area}')


    # TODO сосчитайте длину окружности
    length = (2 * math.pi) * r
    print(f'Длинна круга, l = {length}')

    assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 (включая обе границы) и отсортируйте его по возрастанию.
    """
    # TODO создайте список
    l = [3, 1, 5, 10, 99, 77, 33, 9, 46, 100]
    l.sort()

    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    l = list(set(l))
    # TODO удалите повторяющиеся элементы

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first, second))

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second