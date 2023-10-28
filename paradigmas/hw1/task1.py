# Дан список целых чисел numbers. Необходимо написать в императивном стиле 
# процедуру для сортировки числа в списке в порядке убывания. 
# Можно использовать любой алгоритм сортировки.


def sort_list_imperative(numbers):
    # пузырьковая мортировка
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                # Меняем местами элементы, если текущий больше следующего
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    pass
    return numbers

numbers = [64, 4, 25, 1, 22, 11, 90]
print("sorted list", sort_list_imperative(numbers))

