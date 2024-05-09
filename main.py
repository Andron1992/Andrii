def caching_fibonacci():
    # Створюємо словник для зберігання кешу.
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        # Перевіряємо, чи значення вже є у кеші
        if n in cache:
            return cache[n]

        # Якщо значення не знайдено у кеші, обчислюємо його та зберігаємо у кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    #  визначаємо та повертаємо внутрішню функцію
    return fibonacci

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
fib = caching_fibonacci()
print(fib(12))
print(fib(30))

print("\t")
print("\t")
print("\t")


import re
from typing import Callable

def generator_numbers(text: str):
    # Вираз для пошуку дійсних чисел
    pattern = r'(?<=\s)\d+\.\d+'
    # Знаходимо всі збіги
    for match in re.finditer(pattern, text):
        # Перетворюємо знайдені рядки у числа
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    # Викликаємо функцію яка виділяє числа з тексту
    numbers_generator = func(text)
    # Підрахуємо суму
    total = sum(func(text))
    return total


text = "Загальний дохід працівника складається з декількох частин: 5045.48 як основний дохід, доповнений додатковими надходженнями 64.78 і 278.25 доларів."
total_income = sum_profit(text, generator_numbers)
total_income = round(total_income, 2)
print(f"Загальний дохід: {total_income}")








