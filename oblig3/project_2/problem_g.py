import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def find_CV(name):
    d_data = (np.loadtxt(name,skiprows=1).T)
    dT = d_data[3]
    dQ = d_data[2]

    slope, intercept, r_value, p_value, std_err = stats.linregress(dT,dQ)
    return slope, std_err

d_data = (np.loadtxt("problem_d_lammps.dat",skiprows=1).T)
dT = d_data[3]
dQ = d_data[2]

slope, intercept, r_value, p_value, std_err = stats.linregress(dT,dQ)

dT_cont = np.linspace(np.min(dT),np.max(dT),1000)

rhos = [0.01,0.2,0.4,0.6,0.8]
rho_names = ["001","02","04","06","08"]
C_Vs = []
uncertainties = []

for r,name in zip(rhos,rho_names):
    slope,std_err = find_CV("problem_d_lammbs_rho_%s.dat" %name)
    C_Vs.append(slope)
    uncertainties.append(std_err)

plt.errorbar(rhos,C_Vs,uncertainties,fmt=".-.")
plt.title(r"Heat Capacity as $\rho$ increases. (T=2)")
plt.xlabel(r"$\rho$")
plt.ylabel(r"$C_V$")
plt.show()
