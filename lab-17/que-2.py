import sympy as s
omega,n,z = s.symbols('n,z,omega')
u_n = 1
x_n = s.cos(omega*n)
X_z = s.summation(x_n*u_n*z**(-n),(n,0,s.oo))
print("Z-Transform of x[n] = cos(wn)u[n] : ")
s.pprint(X_z,use_unicode = True)