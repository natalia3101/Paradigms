# Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    pass
    return sorted_numbers

numbers = [64, 4, 25, 1, 22, 11, 90]
print("sorted list", sort_list_declarative(numbers))
