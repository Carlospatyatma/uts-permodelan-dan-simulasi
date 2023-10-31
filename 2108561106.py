from scipy.optimize import linprog

# Koefisien fungsi tujuan (minimalkan biaya)
c = [10, 8]  # Harga per kg A dan B

# Matriks koefisien batasan pertama (protein)
A = [
    [-3, -2],  # Koefisien protein A dan B dalam pakan
]

# Batasan pertama (protein minimal)
b = [-18]  # Minimal 18 unit protein

# Matriks koefisien batasan kedua (energi)
A_eq = [
    [-2, -4],  # Koefisien energi A dan B dalam pakan
]

# Batasan kedua (energi minimal)
b_eq = [-24]  # Minimal 24 unit energi

# Batasan non-negatif
x_bounds = (0, None)  # x (kg A) >= 0
y_bounds = (0, None)  # y (kg B) >= 0

result = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=[x_bounds, y_bounds], method='highs')
# method 'highs' digunakan karena masalah ini memiliki lebih banyak batasan daripada variabel

print("Solusi optimal:")
print("Jumlah kg bahan pakan A yang harus digunakan:", result.x[0], "kg")
print("Jumlah kg bahan pakan B yang harus digunakan:", result.x[1], "kg")
print("Biaya minimal:", result.fun, "ribu rupiah")
