from scipy import stats

x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 5]

correlation, _ = stats.pearsonr(x, y)
print(f"Корреляция Пирсона между x и y: {correlation}")
