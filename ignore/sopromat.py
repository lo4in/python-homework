import numpy as np
import matplotlib.pyplot as plt


# Данные
tau_allowable = 0.6 * 240  # Допустимые напряжения, МПа
Mx_values = [3.0, 3.0, 6.0]  # Моменты для каждого участка (кН·м)
Mx_values = np.abs(np.array(Mx_values) * 1e3)  # Перевод в Н·м
pi = np.pi
# Данные
L = 1.2  # Общая длина вала, м
M = 3.0  # Крутящий момент, кНм
n = 0.2 * L  # Длина первого участка, м
m = 0.3 * L  # Длина третьего участка, м

# Формула для минимального диаметра
d_values = ((16 * Mx_values) / (pi * tau_allowable * 1e6)) ** (1 / 3)  # Диаметр в метрах
d_values_mm = d_values * 1e3  # Диаметр в миллиметрах

# Рассчёт максимальных касательных напряжений для каждого момента
d = np.max(d_values)  # Выбираем наибольший диаметр для расчёта
r = d / 2
J = (pi * d**4) / 32  # Полярный момент инерции
tau_max = Mx_values * r / J * 1e-6  # В МПа

# Построение графика
x_sections = [0, n, L - m, L]  # Координаты участков
tau_sections = [tau_max[0], tau_max[0], tau_max[1], tau_max[2]]

plt.figure(figsize=(8, 5))
plt.plot(x_sections, tau_sections, drawstyle='steps-post', label=r'$\tau_{max}$ (МПа)', color='red', linewidth=2)
plt.axhline(tau_allowable, color='green', linestyle='--', label=r'$\tau_{доп} = 144$ МПа')
plt.title("Эпюра касательных напряжений $\tau_{max}$", fontsize=14)
plt.xlabel("Длина вала (м)", fontsize=12)
plt.ylabel(r"$\tau_{max}$ (МПа)", fontsize=12)
plt.xticks([0, n, L - m, L], ['0', 'n', 'L-m', 'L'])
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
#plt.show()

d_values_mm  # Вывод диаметра для каждого участка в мм



# Углы закручивания на границах участков
phi_1 = Theta_values[0] * n  # Участок 1
phi_2 = phi_1 + Theta_values[1] * (L - n - m)  # Участок 2
phi_3 = phi_2 + Theta_values[2] * m  # Участок 3

# Координаты для эпюры
phi_sections = [0, phi_1, phi_2, phi_3]

# Построение графика
plt.figure(figsize=(8, 5))
plt.plot(x_sections, phi_sections, drawstyle='steps-post', label=r'$\varphi$ (рад)', color='orange', linewidth=2)
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.title("Эпюра углов закручивания $\varphi$", fontsize=14)
plt.xlabel("Длина вала (м)", fontsize=12)
plt.ylabel(r"$\varphi$ (рад)", fontsize=12)
plt.xticks([0, n, L - m, L], ['0', 'n', 'L-m', 'L'])
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.show()

phi_sections  # Углы закручивания на границах участков (рад)
