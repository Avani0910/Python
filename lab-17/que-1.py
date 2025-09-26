import sympy as s 
a,z,n = s.symbols('a,z,n')
u_n = 1
x_n = 3**n
X_z = s.summation(x_n*u_n*z**(-n),(n,0,s.oo))
print("Z-Transform of 3^n u[n] : ")
s.pprint(X_z,use_unicode = True)
