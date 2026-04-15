import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("plots", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Параметры задачи
t0 = 0.0
tmax = 47.0
dt = 0.05
t = np.arange(t0, tmax + dt, dt)

x0 = 0.1
y0 = 0.1

# -----------------------------
# Метод Рунге-Кутты 4-го порядка
# -----------------------------
def rk4_system(func, x0, y0, t):
    x = np.zeros_like(t)
    y = np.zeros_like(t)
    x[0] = x0
    y[0] = y0

    for i in range(len(t) - 1):
        h = t[i + 1] - t[i]

        k1x, k1y = func(t[i], x[i], y[i])
        k2x, k2y = func(t[i] + h / 2, x[i] + h * k1x / 2, y[i] + h * k1y / 2)
        k3x, k3y = func(t[i] + h / 2, x[i] + h * k2x / 2, y[i] + h * k2y / 2)
        k4x, k4y = func(t[i] + h, x[i] + h * k3x, y[i] + h * k3y)

        x[i + 1] = x[i] + h * (k1x + 2 * k2x + 2 * k3x + k4x) / 6
        y[i + 1] = y[i] + h * (k1y + 2 * k2y + 2 * k3y + k4y) / 6

    return x, y

# -----------------------------------------
# 1. Без затухания и без внешней силы
# x'' + 4.5x = 0
# -----------------------------------------
def system1(time, x, y):
    dx = y
    dy = -4.5 * x
    return dx, dy

# -----------------------------------------
# 2. С затуханием, без внешней силы
# x'' + 0.9x' + 0.3x = 0
# -----------------------------------------
def system2(time, x, y):
    dx = y
    dy = -0.9 * y - 0.3 * x
    return dx, dy

# -----------------------------------------
# 3. С затуханием и внешней силой
# x'' + 3x' + 0.5x = 0.5 sin(2t)
# -----------------------------------------
def system3(time, x, y):
    dx = y
    dy = -3.0 * y - 0.5 * x + 0.5 * np.sin(2 * time)
    return dx, dy

# Решения
x1, y1 = rk4_system(system1, x0, y0, t)
x2, y2 = rk4_system(system2, x0, y0, t)
x3, y3 = rk4_system(system3, x0, y0, t)

# График решения 1
plt.figure(figsize=(10, 6))
plt.plot(t, x1, label="x(t)")
plt.plot(t, y1, label="y(t)=x'(t)")
plt.xlabel("t")
plt.ylabel("Значение")
plt.title("Случай 1: без затухания и без внешней силы")
plt.grid(True)
plt.legend()
plt.savefig("plots/solution_case1.png", dpi=150)
plt.close()

# Фазовый портрет 1
plt.figure(figsize=(7, 7))
plt.plot(x1, y1)
plt.xlabel("x")
plt.ylabel("y=x'")
plt.title("Фазовый портрет, случай 1")
plt.grid(True)
plt.savefig("plots/phase_case1.png", dpi=150)
plt.close()

# График решения 2
plt.figure(figsize=(10, 6))
plt.plot(t, x2, label="x(t)")
plt.plot(t, y2, label="y(t)=x'(t)")
plt.xlabel("t")
plt.ylabel("Значение")
plt.title("Случай 2: с затуханием, без внешней силы")
plt.grid(True)
plt.legend()
plt.savefig("plots/solution_case2.png", dpi=150)
plt.close()

# Фазовый портрет 2
plt.figure(figsize=(7, 7))
plt.plot(x2, y2)
plt.xlabel("x")
plt.ylabel("y=x'")
plt.title("Фазовый портрет, случай 2")
plt.grid(True)
plt.savefig("plots/phase_case2.png", dpi=150)
plt.close()

# График решения 3
plt.figure(figsize=(10, 6))
plt.plot(t, x3, label="x(t)")
plt.plot(t, y3, label="y(t)=x'(t)")
plt.xlabel("t")
plt.ylabel("Значение")
plt.title("Случай 3: с затуханием и внешней силой")
plt.grid(True)
plt.legend()
plt.savefig("plots/solution_case3.png", dpi=150)
plt.close()

# Фазовый портрет 3
plt.figure(figsize=(7, 7))
plt.plot(x3, y3)
plt.xlabel("x")
plt.ylabel("y=x'")
plt.title("Фазовый портрет, случай 3")
plt.grid(True)
plt.savefig("plots/phase_case3.png", dpi=150)
plt.close()

# Общий график решений
plt.figure(figsize=(10, 6))
plt.plot(t, x1, label="x(t), случай 1")
plt.plot(t, x2, label="x(t), случай 2")
plt.plot(t, x3, label="x(t), случай 3")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Сравнение решений")
plt.grid(True)
plt.legend()
plt.savefig("plots/all_solutions.png", dpi=150)
plt.close()

# Сохраняем результаты
with open("data/results.txt", "w", encoding="utf-8") as f:
    f.write("Лабораторная работа №3, вариант 19\n\n")
    f.write(f"Интервал: [{t0}, {tmax}], шаг {dt}\n")
    f.write(f"Начальные условия: x0={x0}, y0={y0}\n\n")

    f.write("Случай 1:\n")
    f.write("x'' + 4.5x = 0\n")
    f.write(f"Финальные значения: x={x1[-1]:.6f}, y={y1[-1]:.6f}\n\n")

    f.write("Случай 2:\n")
    f.write("x'' + 0.9x' + 0.3x = 0\n")
    f.write(f"Финальные значения: x={x2[-1]:.6f}, y={y2[-1]:.6f}\n\n")

    f.write("Случай 3:\n")
    f.write("x'' + 3x' + 0.5x = 0.5sin(2t)\n")
    f.write(f"Финальные значения: x={x3[-1]:.6f}, y={y3[-1]:.6f}\n\n")

    f.write("Построены графики решений и фазовые портреты для всех трёх случаев.\n")

print("Готово.")
print("Файлы:")
print(" - plots/solution_case1.png")
print(" - plots/phase_case1.png")
print(" - plots/solution_case2.png")
print(" - plots/phase_case2.png")
print(" - plots/solution_case3.png")
print(" - plots/phase_case3.png")
print(" - plots/all_solutions.png")
print(" - data/results.txt")
