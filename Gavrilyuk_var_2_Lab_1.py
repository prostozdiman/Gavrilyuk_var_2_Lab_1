import math

def parallelogram_properties():
    """Рівень 1: Обчислення площі паралелограма та довжин його діагоналей."""
    print("Введіть координати чотирьох вершин паралелограма у форматі x y через пробіл:")
    x1, y1 = map(float, input("Перша вершина: ").split())
    x2, y2 = map(float, input("Друга вершина: ").split())
    x3, y3 = map(float, input("Третя вершина: ").split())
    x4, y4 = map(float, input("Четверта вершина: ").split())
    
    # Обчислення площі паралелограма за формулою площі чотирикутника
    area = 0.5 * abs((x1*y2 + x2*y3 + x3*y4 + x4*y1) - (y1*x2 + y2*x3 + y3*x4 + y4*x1))
    
    # Обчислення довжин діагоналей
    d1 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    d2 = math.sqrt((x2 - x4)**2 + (y2 - y4)**2)
    
    print(f"Площа паралелограма: {round(area, 3)}")
    print(f"Довжина першої діагоналі: {round(d1, 3)}")
    print(f"Довжина другої діагоналі: {round(d2, 3)}")

def check_number_sign():
    """Рівень 2: Перевірка, чи число додатне, від'ємне або нуль."""
    n = int(input("Введіть число: "))
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

def list_divisors():
    """Рівень 3: Виведення всіх дільників числа."""
    m = int(input("Введіть число: "))
    divisors = [i for i in range(1, m + 1) if m % i == 0]
    print("Дільники числа:", divisors)

def main():
    while True:
        print("\nОберіть завдання:")
        print("1 - Рівень 1: Паралелограм (площа та діагоналі)")
        print("2 - Рівень 2: Перевірка числа")
        print("3 - Рівень 3: Вивід дільників")
        print("0 - Вийти")
        choice = input("Ваш вибір: ")
        
        if choice == "1":
            parallelogram_properties()
        elif choice == "2":
            check_number_sign()
        elif choice == "3":
            list_divisors()
        elif choice == "0":
            print("Вихід...")
            break
        else:
            print("Некоректний вибір, спробуйте ще раз!")

if __name__ == "__main__":
    main()
