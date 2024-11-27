import numpy as np
import matplotlib.pyplot as plt

# Fungsi 1: f(x) = x^3 - 3x
def f(x):
    return x**3 - 3*x

# Interval untuk fungsi 1
x1 = np.linspace(-3/2, 3, 500)
y1 = f(x1)

# Fungsi 2: g(x) = 3x / (x^2 + 1)
def g(x):
    return 3*x / (x**2 + 1)

# Interval untuk fungsi 2
x2 = np.linspace(-3, 3, 500)
y2 = g(x2)

# Plot kedua grafik
fig, axes = plt.subplots(2, 1, figsize=(10, 10))

# Grafik fungsi 1
axes[0].plot(x1, y1, label=r"$f(x) = x^3 - 3x$", color="blue")
axes[0].scatter([-1, 1, -3/2, 3], [f(-1), f(1), f(-3/2), f(3)], color="red", zorder=5)
axes[0].set_title("Grafik Fungsi f(x) = x^3 - 3x")
axes[0].set_xlabel("x")
axes[0].set_ylabel("f(x)")
axes[0].axhline(0, color='black', linewidth=0.8, linestyle='--')
axes[0].axvline(0, color='black', linewidth=0.8, linestyle='--')
axes[0].grid()
axes[0].legend()

# Grafik fungsi 2
axes[1].plot(x2, y2, label=r"$g(x) = \frac{3x}{x^2 + 1}$", color="green")
axes[1].set_title("Grafik Fungsi g(x) = 3x / (x^2 + 1)")
axes[1].set_xlabel("x")
axes[1].set_ylabel("g(x)")
axes[1].axhline(0, color='black', linewidth=0.8, linestyle='--')
axes[1].axvline(0, color='black', linewidth=0.8, linestyle='--')
axes[1].grid()
axes[1].legend()

# Tampilkan grafik
plt.tight_layout()
plt.show()