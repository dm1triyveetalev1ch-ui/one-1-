def simulate_stock_price(S0=100, T=1.0, n_steps=252, mu=0.05, sigma=0.2, n_simulations=10000):
        
    dt = T / n_steps
    time_grid = np.linspace(0, T, n_steps + 1)

    all_paths = np.zeros((n_simulations, n_steps + 1))

    for i in range(n_simulations):
        all_paths[i] = binomial_tree_one_path(S0, T, n_steps, mu, sigma)

    mean_path = np.mean(all_paths, axis=0)
    percentile_5 = np.percentile(all_paths, 5, axis=0)
    percentile_95 = np.percentile(all_paths, 95, axis=0)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
     
    for i in range(min(50, n_simulations)): # Визуализируем до 50 случайных путей для наглядности
        plt.plot(time_grid, all_paths[i], alpha=0.1, color='gray')
    plt.plot(time_grid, mean_path, color='blue', linewidth=3, label='Средний путь')
    plt.fill_between(time_grid, percentile_5, percentile_95, color='blue', alpha=0.2, label='90% дов. интервал')
    plt.xlabel('Время (годы)')
    plt.ylabel('Цена акции')
    plt.title(f'Моделирование цены акции (n={n_simulations})')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.subplot(1, 2, 2)
       
    final_prices = all_paths[:, -1]
    plt.hist(final_prices, bins=50, edgecolor='black', alpha=0.7)
    plt.axvline(np.mean(final_prices), color='red', linestyle='--', linewidth=2, label=f'Среднее: {np.mean(final_prices):.2f}')
    plt.axvline(S0 * np.exp(mu * T), color='green', linestyle='--', linewidth=2, label=f'Теория: {S0 * np.exp(mu * T):.2f}')
    plt.xlabel('Цена в момент T')
    plt.ylabel('Частота')
    plt.title('Распределение конечных цен')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    return all_paths, mean_path, (percentile_5, percentile_95)
  paths, mean_path, percentiles = simulate_stock_price(S0=100, T=1.0, n_steps=252, mu=0.05, sigma=0.2, n_simulations=5000)
