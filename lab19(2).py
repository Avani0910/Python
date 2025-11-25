import sympy as sp

# Define variable
z = sp.symbols('z')

# Define H(z)
H = 0.5 * (z - 0.7) * (z - 0.9) / ((z - 0.6) * (z - 0.4))

# Find poles and zeros
zeros = sp.solve(sp.simplify((z - 0.7)*(z - 0.9)), z)
poles = sp.solve(sp.simplify((z - 0.6)*(z - 0.4)), z)

print("Zeros:", zeros)
print("Poles:", poles)

# Stability Check
stable = all(abs(p) < 1 for p in poles)

if stable:
    print("\nThe system is STABLE (All poles lie inside the unit circle).")
else:
    print("\nThe system is UNSTABLE (One or more poles lie outside the unit circle).")
