
import numpy as np
import matplotlib.pyplot as plt

# Setup lists
T_values = [77.0,100.0, 110.0, 115.0, 120.0, 125.0] # [K]

T_c = 126.0
P_c = 36.6  # [atm]
V_c = 0.089 # [l/mol]

V = np.linspace(0.4*V_c, 6.0*V_c, 1000)

# Calculate pressure for a given T: 
for T in T_values:
    p = (P_c)*((8*T/T_c)/(3*(V/V_c) - 1) - 3/((V/V_c)**2))
    plt.plot(V, p)


# Plot:
plt.legend(['$\hat{T} = 77.0$','$\hat{T} = 100.0$', '$\hat{T}=110.0$','$\hat{T} = 115.0$', '$\hat{T} = 120.0$', '$\hat{T} = 125.0$'])
plt.xlabel('Volume V')
plt.ylabel('Pressure P')
plt.show()

