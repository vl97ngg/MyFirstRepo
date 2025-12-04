"""
Простой Python скрипт для демонстрации работы с GitHub
Автор: Студент ЛЭТИ
Дата: 18.12.2024
"""

def hello_github():
    """Функция приветствия"""
    print("=" * 50)
    print("Привет из репозитория GitHub!")
    print("Этот скрипт демонстрирует работу с файлами в Git")
    print("=" * 50)

def calculate_statistics(numbers):
    """Рассчитывает статистику по списку чисел"""
    if not numbers:
        return "Список пуст"
    
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return {
        "sum": total,
        "average": average,
        "max": maximum,
        "min": minimum,
        "count": len(numbers)
    }

def main():
    """Основная функция"""
    hello_github()
    
    # Пример работы со списком чисел
    sample_data = [10, 20, 30, 40, 50]
    print(f"\nИсходные данные: {sample_data}")
    
    stats = calculate_statistics(sample_data)
    print("\nРезультаты расчета:")
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    # Простые математические операции
    print("\nПростые операции:")
    a = 15
    b = 3
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b:.2f}")
    
    print("\nСкрипт успешно выполнен!")

if __name__ == "__main__":
    main()