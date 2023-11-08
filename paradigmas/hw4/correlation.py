from functools import reduce

# вычисление среднего значения
def mean(data):
    return sum(data) / len(data)

# вычисление ковариации
def covariance(x, y):
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)
    return sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))

# вычисление корреляции пирсона
def pearson_correlation(x, y):
    covar = covariance(x, y)
    var_x = covariance(x, x)
    var_y = covariance(y, y)
    correlation = covar / (var_x ** 0.5 * var_y ** 0.5)
    return correlation

# Пример использования:
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 5]

print(f"Корреляция Пирсона между x и y: {pearson_correlation(x, y)}")
