# Вычисление суммы чисел: 
# Напишите программу для вычисления суммы чисел от 1 до N.

# императивный
n = 5
sum_of_n = 0
for i in range(1, n +1):
    sum_of_n += i
print("the sum is", sum_of_n)

# декларативный
n = range(1,6)
print("the sum is", sum(n))