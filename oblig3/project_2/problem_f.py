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


##############
# Oppgave f) #
##############

Ts = [1,0.694,2,6,10,13]
T_names = ["0694","2","6","10","13"]
C_Vs = [slope]
uncertainties = [std_err]

for t,name in zip(Ts[1:],T_names):

    slope,std_err = find_CV("problem_d_lammps%s.dat" %name)
    
    C_Vs.append(slope)
    uncertainties.append(std_err)

plt.errorbar(Ts,C_Vs,uncertainties,fmt=".-.")
plt.title(r"Heat Capacity $C_V$ as Temperature increases. For $\rho = 0.01$")
plt.xlabel("T")
plt.ylabel(r"$C_V$")
plt.show()

