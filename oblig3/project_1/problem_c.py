
import numpy as np
import matplotlib.pyplot as plt

# Setup lists
T_values = [1.0, 0.95, 0.9, 0.8]
V = np.linspace(0.4, 6.0, 100)

# Calculate pressure for a given T: 
for T in T_values:
    p = 8*T/(3*V - 1) - 3/(V**2)
    plt.plot(V, p)


# Plot:
plt.legend(['$\hat{T} = 1.0$', '$\hat{T}=0.95$','$\hat{T} = 0.9$', '$\hat{T} = 0.8$'])
plt.xlabel('Volume V')
plt.ylabel('Pressure P')
plt.show()

