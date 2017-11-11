
import numpy as np
import matplotlib.pyplot as plt

# Setup lists
T_values = [0.8, 0.9, 0.95, 1.0]
rho = np.linspace(0.0, 2.0, 100)

# Calculate pressure for a given T: 
for T in T_values:
    p = (8*rho*T)/(3 - rho) - 3*rho**2
    plt.plot(rho, p)


# Plot:
plt.legend(['$\hat{T} = 0.8$', '$\hat{T}=0.9$','$\hat{T} = 0.95$', '$\hat{T} = 1.0$'])
plt.xlabel('Density $\\rho$')
plt.ylabel('Pressure P')
plt.show()

