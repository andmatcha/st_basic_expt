import sympy as sp

# 定数の定義
k = 5.623 * 10**11

# 変数の定義
x = sp.symbols("x")

# 方程式の定義
equation = x - k * (0.0079 - x) * (3.0 - 4 * x) ** 4

# 方程式を解く
solution = sp.solve(equation, x)
print(solution)
