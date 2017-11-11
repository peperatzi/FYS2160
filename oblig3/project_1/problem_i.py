
import numpy as np
import matplotlib.pyplot as plt

# Setup lists
T_values = [100.0, 110.0, 115.0, 120.0, 125.0] # [K]
col = ['r','g','b','y','m']
P_values = [12.0, 20.0, 25.0, 30.0, 35.5] # [K]

# 
T_c = 126.0
P_c = 36.6  # [atm]
V_c = 0.089 # [l/mol]

V = np.linspace(0.4*V_c, 6.0*V_c, 1000)

# Calculate pressure for a given T:
i = 0
for T in T_values:
    p = (P_c)*((8.0*T/T_c)/(3.0*(V/V_c) - 1) - 3/((V/V_c)**2))
    plt.plot(V, p, col[i])
    i += 1

# Plot:
plt.legend(['$\hat{T} = 77.0$','$\hat{T} = 100.0$', '$\hat{T}=110.0$','$\hat{T} = 115.0$', '$\hat{T} = 120.0$', '$\hat{T} = 125.0$'])
plt.xlabel('Volume V')
plt.ylabel('Pressure P')
plt.ylim(-20,40)

# Add lines to sepereate the plot into "two sections"
for i in range(len(col)):
    plt.plot([0.0,0.6],[P_values[i],P_values[i]], '%s--'%(col[i]), lw='1', label="_not in legend")

plt.show()

