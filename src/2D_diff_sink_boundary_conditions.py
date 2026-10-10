import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
 

#parameters 

Lx=1 
Ly=0.5
k=1000
T_inf=300
b=0.01
h=7000
Nx=10
Ny=12

#grid spacing 
delta_x=Lx/(Nx-1)
delta_y=Ly/(Ny-1)

V=delta_x * delta_y *b 

S_u=h*T_inf
S_p=-h

ae_val=(k*delta_y*b)/delta_x
aw_val=(k* delta_y*b)/delta_x
an_val=(k*delta_x*b)/delta_y
as_val=(k*delta_x*b)/delta_y
bp_val=S_u * delta_x * delta_y * b
cp_val=S_p * delta_x * delta_y * b

#iteration number
iteration=0
#initialize temperature 
T=np.zeros((Ny,Nx))
#left and right side boundary conditions 
T[:,0]=100
T[:,Nx-1]=500
#print (T)

#initialise iterated temperature 
T_new=T.copy()

#error variables:
epsilon = 1.E-8
numerical_error=1

#Iterative process , error verfication 
while numerical_error > epsilon :
    for i in range(0,Ny):
        for j in range(1,Nx-1):
            if i == 0 :
                ap= ae_val/2 + aw_val/2 + as_val - cp_val/2 
                T_new[i,j] = ((ae_val/2)*T[i,j+1] + (aw_val/2)*T[i,j-1] + as_val*T[i+1,j] + bp_val/2)/ap
            elif i == Ny - 1 :
                ap= ae_val/2 + aw_val/2 + an_val - cp_val/2 
                T_new[i,j] = ((ae_val/2)*T[i,j+1] + (aw_val/2)*T[i,j-1] + an_val*T[i-1,j] + bp_val/2)/ap
            else :
                ap= ae_val + aw_val + an_val + as_val - cp_val
                T_new[i,j] = (ae_val*T[i,j+1] + aw_val*T[i,j-1] + an_val*T[i-1,j] + as_val*T[i+1,j] + bp_val)/ap
                
                
    #resetting the numerical error and recalculate
    numerical_error=0
    for i in range(0,Ny):
         for j in range(1,Nx-1):
             numerical_error=numerical_error+abs(T[i,j]-T_new[i,j])  
    iteration =iteration + 1
    T=T_new.copy()
print(f'Temperature distribution obtained after {iteration} iterations and sink strength h is {h}')       
# --- Grid Generation ---
x_dom = np.linspace(0, Lx, Nx)
y_dom = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x_dom, y_dom)
# --- Plot temperature field ---

plt.figure(figsize=(8, 4))

contour = plt.contourf(X, Y, T, levels=200)
plt.colorbar(contour, label="Temperature")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Temperature distribution 2D_diff+sink+boundary_conditions")
plt.show()     
            
#table 
x=np.arange(Nx)*delta_x
table=pd.DataFrame({
    "Node": np.arange(1,Nx+1),
    "Distance" :x,
    "Numerical solution" :T[0,:],
    })
table_display=table.round(6)
print(table_display.to_string(index=False))
table_display.to_csv("Temperature distribution 2D_diff+sink+boundary_conditions", index=False)

    
