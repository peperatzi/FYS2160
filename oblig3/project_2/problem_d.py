# 
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 
d_data = (np.loadtxt("problem_d_lammps.dat",skiprows=1).T)
dT = d_data[3]
dQ = d_data[2]

# 
slope, intercept, r_value, p_value, std_err = stats.linregress(dT,dQ)

dT_cont = np.linspace(np.min(dT),np.max(dT),1000)

# Plot
plt.plot(dT,dQ,".")
plt.plot(dT_cont,slope*dT_cont + intercept,label="Linear Fit")
plt.title("dT vs dQ and the linear fit for finding $C_V$")
plt.xlabel(r"dT $[\epsilon/k]$")
plt.ylabel(r"dQ $[\epsilon]$")
plt.legend()
plt.show()

print("C_V = {} +/- {}".format(slope,std_err))


