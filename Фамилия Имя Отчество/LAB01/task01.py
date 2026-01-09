#!/usr/env/python

def get_integer_input(position):
    """
    Запрашивает у пользователя целое число для указанной позиции.
    При ошибке ввода повторяет запрос.
    
    Args:
        position: номер позиции в списке (от 1 до 10)
    
    Returns:
        int: введённое пользователем целое число
    """
    while True:
        try:
            value = int(input(f"Введите целое число #{position}: "))
            return value
        except ValueError:
            print("Ошибка! Введите целое число")


def main():
    """
    Основная функция программы.
    Запрашивает 10 целых чисел у пользователя и выводит статистику.
    """
    print("Программа для ввода 10 целых чисел")
    print("=" * 40)
    
    numbers = []
    
    for i in range(1, 11):
        number = get_integer_input(i)
        numbers.append(number)
    
    print("\n" + "=" * 40)
    print("Все числа успешно введены!")
    print("=" * 40)
    print(f"\nВведённые числа: {numbers}")
    print(f"\nМинимальное число: {min(numbers)}")
    print(f"Максимальное число: {max(numbers)}")
    print(f"Сумма всех чисел: {sum(numbers)}")


if __name__ == '__main__':
    main()
