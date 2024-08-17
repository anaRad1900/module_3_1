# Глобальная переменная для подсчета вызовов
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()  # Считаем вызов
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()  # Считаем вызов
    # Приводим к нижнему регистру для сравнения
    string_lower = string.lower()
    return string_lower in [item.lower() for item in list_to_search]

# Примеры вызовов функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))     

# Выводим количество вызовов
print(calls)