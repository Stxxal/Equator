import numpy as np
import sympy as sp 

(f,m,a,c,e)=sp.symbols("f m a c e") #Defining symbols
symbols=(f,m,a,c,e)
initial_eq=np.array([sp.Eq(f,m*a),sp.Eq(e,m*c**2)]) #Example list of equations

#print(initial_eq)

final_symbols=np.array([]) #array() is list-like iterable from numpy module
final_equations=np.array([])
checking_symbol=np.array([])
for i in range(len(initial_eq)):
    for j in symbols:
        if sp.solve(initial_eq[i],j): #for removing blank arrays
            checking_symbol=np.append(j,checking_symbol)
            specific_symbol=sp.solve(initial_eq[i],j)[0] #this represents the equation in terms of every variable
            final_symbols=np.append(specific_symbol,final_symbols)
            
#print(final_symbols)

for i in range(len(final_symbols)):
    for j in symbols:
        for k in initial_eq:
            if j==checking_symbol[i]: #checking if the symbol being substituted is same
                final_equations=np.append(k.subs(j,final_symbols[i]),final_equations)
print(final_equations)
