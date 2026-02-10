import numpy as np
import matplotlib.pyplot as plt
# Для воспроизводимости результатов
np.random.seed(42)

def estimate_pi(num_samples, radius=1.0):
    """
    Оценивает число pi методом Монте-Карло.

    Параметры:
    num_samples (int): Количество случайных точек.
    radius (float): Радиус круга.

    Возвращает:
    float: Оценка числа pi.
    float: Стандартная ошибка оценки.
    """
    # Генерация случайных точек в квадрате [-radius, radius] x [-radius, radius]
    x = np.random.uniform(-radius, radius, num_samples)
    y = np.random.uniform(-radius, radius, num_samples)

    # Определение, какие точки лежат внутри круга (x^2 + y^2 <= r^2)
    inside_circle = (x**2 + y**2) <= radius**2
    num_inside = np.sum(inside_circle)

    # Оценка площади квадрата и доли, занятой кругом
    square_area = (2 * radius) ** 2
    # pi_estimate = (num_inside / num_samples) * 4  # Альтернативный расчет
    estimated_area_ratio = num_inside / num_samples
    pi_estimate = estimated_area_ratio * 4

    # Оценка стандартной ошибки (упрощенно)
    # Дисперсия бернуллиевской величины: p*(1-p), где p = num_inside/num_samples
    p = num_inside / num_samples
    std_error = np.sqrt(p * (1 - p) / num_samples)

    return pi_estimate, std_error
