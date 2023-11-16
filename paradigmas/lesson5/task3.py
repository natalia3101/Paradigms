from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, can_marry')

+ can_marry('Иван', 'Мария')
+ can_marry('Анна', 'Петр')

# Правило: X может жениться на Y, если Y может выйти замуж за X
can_marry(X, Y) <= can_marry(Y, X)

# Запрос: с кем может жениться Петр?
print(can_marry('Петр', X))