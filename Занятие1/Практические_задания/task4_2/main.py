from itertools import count

def task():
    iterator_numbers = count(1, 1)
    numbers = map(lambda x: x**2, filter(lambda x: x% 2 == 0, iterator_numbers))
    # numbers = [i ** 2 for i in iterator_numbers if i % 2 == 0]  # TODO заменить на map и filter

    for _ in range(10):  # TODO напечатать первые 10 чисел
        print(next(numbers))  # TODO с помощью next получать следующий элемент от итератора


if __name__ == "__main__":
    task()
