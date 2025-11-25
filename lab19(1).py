from sympy import symbols, ztrans, inverse_ztransform, Heaviside

n, z = symbols('n z')

u = Heaviside(n)

U_z = ztrans(u, n, z)
print("Z-transform of unit step function u[n] is:", U_z)

print("\nStability Analysis:")
print("For u[n], Z-transform = 1 / (1 - z^(-1)) with ROC: |z| > 1")
print("Since ROC does NOT include the unit circle (|z|=1), the system is UNSTABLE.")
