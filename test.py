# Параметры эксперимента
sample_sizes = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
estimates = []
errors = []

for n in sample_sizes:
    pi_est, err = estimate_pi(n)
    estimates.append(pi_est)
    errors.append(err)
    print(f"N = {n:7d}: π ≈ {pi_est:.5f} ± {err:.5f}")

plt.figure(figsize=(16, 7))


plt.subplot(1, 2, 1)
plt.errorbar(sample_sizes, estimates, yerr=errors, fmt='-o', capsize=5, label='Оценка Монте-Карло')
plt.axhline(y=np.pi, color='r', linestyle='--', label='Истинное значение π')
plt.xscale('log') # Логарифмическая шкала для наглядности
plt.xlabel('Число случайных точек (N)')
plt.ylabel('Оценка π')
plt.title('Сходимость оценки π')
plt.grid(True, alpha=0.3)
plt.legend()

plt.subplot(1, 2, 2)

n_show = 50000 # Using the largest sample_size for visualization

x_show = np.random.uniform(-1, 1, n_show)
y_show = np.random.uniform(-1, 1, n_show)
inside_show = (x_show**2 + y_show**2) <= 1**2

pi_est_final, _ = estimate_pi(n_show) # Estimate pi for this visualization to match the title

plt.scatter(x_show[inside_show], y_show[inside_show], color='blue', s=1, alpha=0.6, label='Внутри круга')
plt.scatter(x_show[~inside_show], y_show[~inside_show], color='red', s=1, alpha=0.6, label='Снаружи круга')

theta = np.linspace(0, 2*np.pi, 100)
plt.plot(np.cos(theta), np.sin(theta), color='black', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Точки (N={n_show}), π ≈ {pi_est_final:.4f}')
plt.axis('equal')
plt.legend(markerscale=5)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
