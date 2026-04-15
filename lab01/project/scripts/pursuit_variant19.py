import math
import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("plots", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Вариант 19
k = 10.0
n = 3.4

# Углы движения лодки для двух иллюстраций
phi1 = math.pi / 4
phi2 = 3 * math.pi / 4

# Начальные радиусы для двух случаев
x1 = k / (n + 1)
x2 = k / (n - 1)

a = math.sqrt(n**2 - 1)

def r_case1(theta):
    return x1 * np.exp(theta / a)

def r_case2(theta):
    return x2 * np.exp((theta + math.pi) / a)

# Полярная -> декартова
def pol2cart(r, theta):
    return r * np.cos(theta), r * np.sin(theta)

# Лодка идет по прямой из начала координат
def boat_line(t, phi):
    return t * np.cos(phi), t * np.sin(phi)

# Ищем точку пересечения графически/численно
def intersection_case1(phi):
    theta_vals = np.linspace(0, 4 * math.pi, 5000)
    r_vals = r_case1(theta_vals)

    # Для прямой лодки в полярных координатах пересечение при theta = phi
    r_boat = r_case1(phi)
    xb, yb = pol2cart(r_boat, phi)
    return phi, r_boat, xb, yb, theta_vals, r_vals

def intersection_case2(phi):
    # Для второго случая пересечение берем при угле phi
    theta_vals = np.linspace(-math.pi, 3 * math.pi, 5000)
    r_vals = r_case2(theta_vals)

    r_boat = r_case2(phi)
    xb, yb = pol2cart(r_boat, phi)
    return phi, r_boat, xb, yb, theta_vals, r_vals

# --- Случай 1 ---
theta_i1, r_i1, xi1, yi1, theta_vals1, r_vals1 = intersection_case1(phi1)
xc1, yc1 = pol2cart(r_vals1, theta_vals1)

t1 = np.linspace(0, r_i1 * 1.2, 400)
xb1, yb1 = boat_line(t1, phi1)

plt.figure(figsize=(8, 8))
plt.plot(xc1, yc1, label="Катер, случай 1")
plt.plot(xb1, yb1, label="Лодка", linestyle="--")
plt.scatter([xi1], [yi1], color="red", label="Точка пересечения")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Траектории катера и лодки — случай 1")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.savefig("plots/case1.png", dpi=150)
plt.close()

# --- Случай 2 ---
theta_i2, r_i2, xi2, yi2, theta_vals2, r_vals2 = intersection_case2(phi2)
xc2, yc2 = pol2cart(r_vals2, theta_vals2)

t2 = np.linspace(0, r_i2 * 1.2, 400)
xb2, yb2 = boat_line(t2, phi2)

plt.figure(figsize=(8, 8))
plt.plot(xc2, yc2, label="Катер, случай 2")
plt.plot(xb2, yb2, label="Лодка", linestyle="--")
plt.scatter([xi2], [yi2], color="red", label="Точка пересечения")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Траектории катера и лодки — случай 2")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.savefig("plots/case2.png", dpi=150)
plt.close()

# Общий график
plt.figure(figsize=(9, 9))
plt.plot(xc1, yc1, label="Катер, случай 1")
plt.plot(xb1, yb1, "--", label="Лодка, случай 1")
plt.plot(xc2, yc2, label="Катер, случай 2")
plt.plot(xb2, yb2, "--", label="Лодка, случай 2")
plt.scatter([xi1, xi2], [yi1, yi2], color="red", label="Точки пересечения")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Задача о погоне, вариант 19")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.savefig("plots/all_cases.png", dpi=150)
plt.close()

with open("data/results.txt", "w", encoding="utf-8") as f:
    f.write("Вариант 19\n")
    f.write(f"k = {k}\n")
    f.write(f"n = {n}\n")
    f.write(f"x1 = {x1:.6f}\n")
    f.write(f"x2 = {x2:.6f}\n")
    f.write(f"sqrt(n^2 - 1) = {a:.6f}\n\n")

    f.write("Случай 1:\n")
    f.write(f"theta_intersection = {theta_i1:.6f}\n")
    f.write(f"r_intersection = {r_i1:.6f}\n")
    f.write(f"point = ({xi1:.6f}, {yi1:.6f})\n\n")

    f.write("Случай 2:\n")
    f.write(f"theta_intersection = {theta_i2:.6f}\n")
    f.write(f"r_intersection = {r_i2:.6f}\n")
    f.write(f"point = ({xi2:.6f}, {yi2:.6f})\n")

print("Готово.")
print(f"x1 = {x1:.6f}")
print(f"x2 = {x2:.6f}")
print(f"Случай 1: ({xi1:.4f}, {yi1:.4f})")
print(f"Случай 2: ({xi2:.4f}, {yi2:.4f})")
print("Файлы:")
print(" - plots/case1.png")
print(" - plots/case2.png")
print(" - plots/all_cases.png")
print(" - data/results.txt")
