import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("plots", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Вариант 19
x0 = 25000.0
y0 = 45000.0

t0 = 0.0
tmax = 1.0
dt = 0.001

t = np.arange(t0, tmax + dt, dt)

# ---------------------------
# МОДЕЛЬ 1: регулярные войска
# dx/dt = -0.22 x - 0.71 y + 2 sin(3t)
# dy/dt = -0.79 x - 0.32 y + 2 cos(4t)
# ---------------------------

def f1(time, x, y):
    dx = -0.22 * x - 0.71 * y + 2 * np.sin(3 * time)
    dy = -0.79 * x - 0.32 * y + 2 * np.cos(4 * time)
    return dx, dy

# ---------------------------
# МОДЕЛЬ 2: регулярные + партизаны
# dx/dt = -0.23 x - 0.84 y + 2 sin(2t)
# dy/dt = -0.91 x y - 0.32 y + 2 cos(t)
# ---------------------------

def f2(time, x, y):
    dx = -0.23 * x - 0.84 * y + 2 * np.sin(2 * time)
    dy = -0.91 * x * y - 0.32 * y + 2 * np.cos(time)
    return dx, dy

def euler_system(func, x0, y0, t):
    x = np.zeros_like(t)
    y = np.zeros_like(t)
    x[0] = x0
    y[0] = y0

    for i in range(len(t) - 1):
        dx, dy = func(t[i], x[i], y[i])
        x[i + 1] = max(0.0, x[i] + dt * dx)
        y[i + 1] = max(0.0, y[i] + dt * dy)
    return x, y

# Решение
x1, y1 = euler_system(f1, x0, y0, t)
x2, y2 = euler_system(f2, x0, y0, t)

# Победитель
def winner(x, y):
    if x[-1] > y[-1]:
        return "Побеждает армия X"
    elif y[-1] > x[-1]:
        return "Побеждает армия Y"
    return "Ничья"

w1 = winner(x1, y1)
w2 = winner(x2, y2)

# График 1
plt.figure(figsize=(10, 6))
plt.plot(t, x1, label="Армия X")
plt.plot(t, y1, label="Армия Y")
plt.xlabel("t")
plt.ylabel("Численность")
plt.title("Модель 1: регулярные войска")
plt.grid(True)
plt.legend()
plt.savefig("plots/model1.png", dpi=150)
plt.close()

# График 2
plt.figure(figsize=(10, 6))
plt.plot(t, x2, label="Армия X")
plt.plot(t, y2, label="Армия Y")
plt.xlabel("t")
plt.ylabel("Численность")
plt.title("Модель 2: регулярные войска и партизаны")
plt.grid(True)
plt.legend()
plt.savefig("plots/model2.png", dpi=150)
plt.close()

# Общий график
plt.figure(figsize=(10, 6))
plt.plot(t, x1, label="X, модель 1")
plt.plot(t, y1, label="Y, модель 1")
plt.plot(t, x2, "--", label="X, модель 2")
plt.plot(t, y2, "--", label="Y, модель 2")
plt.xlabel("t")
plt.ylabel("Численность")
plt.title("Сравнение моделей")
plt.grid(True)
plt.legend()
plt.savefig("plots/all_models.png", dpi=150)
plt.close()

# Результаты
with open("data/results.txt", "w", encoding="utf-8") as f:
    f.write("Лабораторная работа №2, вариант 19\n\n")
    f.write(f"Начальные условия: x0={x0}, y0={y0}\n\n")

    f.write("Модель 1: регулярные войска\n")
    f.write("dx/dt = -0.22x - 0.71y + 2sin(3t)\n")
    f.write("dy/dt = -0.79x - 0.32y + 2cos(4t)\n")
    f.write(f"Финальные значения: x={x1[-1]:.3f}, y={y1[-1]:.3f}\n")
    f.write(f"{w1}\n\n")

    f.write("Модель 2: регулярные войска и партизаны\n")
    f.write("dx/dt = -0.23x - 0.84y + 2sin(2t)\n")
    f.write("dy/dt = -0.91xy - 0.32y + 2cos(t)\n")
    f.write(f"Финальные значения: x={x2[-1]:.3f}, y={y2[-1]:.3f}\n")
    f.write(f"{w2}\n\n")

    f.write("Условия победы:\n")
    f.write("- В модели 1 побеждает сторона, чья численность медленнее убывает и остается больше к концу интервала.\n")
    f.write("- В модели 2 большое влияние оказывает нелинейный член -0.91*x*y, который резко ускоряет потери армии Y.\n")

print("Готово.")
print("Модель 1:", w1, f"(x={x1[-1]:.2f}, y={y1[-1]:.2f})")
print("Модель 2:", w2, f"(x={x2[-1]:.2f}, y={y2[-1]:.2f})")
print("Файлы:")
print(" - plots/model1.png")
print(" - plots/model2.png")
print(" - plots/all_models.png")
print(" - data/results.txt")
