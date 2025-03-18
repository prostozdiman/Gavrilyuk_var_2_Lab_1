import itertools
import math
import random

def triangle_height(S, a):
    """Обчислює висоту трикутника, якщо його основа більша за висоту на a."""
    h = (-a + math.sqrt(a**2 + 4*S*2)) / 2
    return round(h, 2)

def parallelogram_properties(points):
    """Обчислює площу паралелограма та довжини його діагоналей."""
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = points
    area = abs((x1*y2 + x2*y3 + x3*y4 + x4*y1) - (y1*x2 + y2*x3 + y3*x4 + y4*x1)) / 2
    diag1 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    diag2 = math.sqrt((x2 - x4)**2 + (y2 - y4)**2)
    return round(area, 3), round(diag1, 3), round(diag2, 3)

def pyramid_surface_area(V, h):
    """Обчислює площу бічної поверхні правильної чотирикутної піраміди."""
    base_area = V / (h / 3)
    return round(base_area, 3)

def quadrilateral_area(coords):
    """Обчислює площу чотирикутника за координатами."""
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = coords
    area = abs((x1*y2 + x2*y3 + x3*y4 + x4*y1) - (y1*x2 + y2*x3 + y3*x4 + y4*x1)) / 2
    return round(area, 3)

def truncated_cone_surface_area(R, r, H):
    """Обчислює площу повної поверхні зрізаного конуса."""
    L = math.sqrt(H**2 + (R - r)**2)
    area = math.pi * (R**2 + r**2 + (R + r) * L)
    return round(area, 3)

def is_divisible(n, a, b):
    return "YES" if n % a == 0 and n % b == 0 else "NO"

def check_number(n):
    return "Positive" if n > 0 else "Negative" if n < 0 else "Zero"

def min_max(a, b):
    return min(a, b), max(a, b)

def season(month):
    seasons = {1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring", 6: "Summer", 
               7: "Summer", 8: "Summer", 9: "Autumn", 10: "Autumn", 11: "Autumn", 12: "Winter"}
    return seasons.get(month, "Invalid month")

def triangle_type(a, b, c):
    if a == b == c:
        return 1
    elif a == b or b == c or a == c:
        return 2
    else:
        return 3

# Виконання функцій
n, a, b = 12, 3, 4
print("Чи ділиться число на a і b:", is_divisible(n, a, b))

n = -5
print("Тип числа:", check_number(n))

print("Мінімум і максимум:", min_max(8, 3))

print("Пора року:", season(5))

print("Тип трикутника:", triangle_type(3, 3, 3))
