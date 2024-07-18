def print_params(a=1, b='строка', c=True):
    print(a, b, c)

'''1.Функция с параметрами по умолчанию:'''
print_params()
print_params(b=40)
print_params(b=25, c=[1, 2, 3])

'''2.Распаковка параметров:'''
values_list = [54.32, 'Строка', True]
values_dict = {'a': 7, 'b': 'Строка', 'c': 3}

print_params(*values_list)
print_params(**values_dict)

'''3.Распаковка + отдельные параметры:'''
values_list_2 = [34, 'Stroka']
print_params(*values_list_2, 42)
