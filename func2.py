import numpy as np
import matplotlib.pyplot as plt

def binomial_tree_one_path(S0, T, n_steps, mu, sigma):
    """
    Генерирует один сценарий движения цены по биномиальному дереву.

    Параметры:
    S0 (float): Начальная цена.
    T (float): Горизонт прогноза в годах.
    n_steps (int): Количество шагов в дереве.
    mu (float): Ожидаемая доходность (годовая).
    sigma (float): Волатильность (годовая).

    Возвращает:
    np.array: Массив цен по шагам.
    """
    dt = T / n_steps # Длина одного шага в годах
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(mu * dt) - d) / (u - d) # Вероятность роста

    price_path = np.zeros(n_steps + 1)
    price_path[0] = S0

    for t in range(1, n_steps + 1):
        # Подбрасываем "монетку" для каждого шага
        if np.random.rand() < p:
            price_path[t] = price_path[t-1] * u
        else:
            price_path[t] = price_path[t-1] * d

    return price_path
