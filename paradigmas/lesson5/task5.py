from pyDatalog import pyDatalog

# Создаем термины
pyDatalog.create_terms('X, number, total_sum')

# Добавляем числа как факты
+ (number[1])
+ (number[2])
+ (number[3])

# Определяем правило для суммирования
total_sum(X) <= sum_(number[X], for_each=X)

# Выводим общую сумму
print(total_sum(X))