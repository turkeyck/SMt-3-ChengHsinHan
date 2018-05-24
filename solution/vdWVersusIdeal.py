"""************************************************************
Written by Cheng-Hsin Han (gsjh80317cla@gmail.com)
************************************************************"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# The values of volume V, temperature T, and pressure P are all being rescaled
# in the units of critical volume V_c, critical temperature T_c and critical
# pressure P_c in this program. Thus are all dimensionless. I also assume the
# number of particles, N, is 1

# the value of the range and number of bins for the volume
Vmin = 0.4
Vmax = 3.0
n_bin = 1000

V = np.linspace(Vmin, Vmax, n_bin)

# make plots for T = 0.9T_c, 1.0 T_c, and 1.1 T_c
for step in range(3):
    T = 0.9 + 0.1 * step

    P_ideal = T / V
    P_vdW = 8 * T / (3 * V - 1) - 3 / V**2

    fig, ax = plt.subplots()

    ax.plot(V, P_ideal, "-,r", label = "ideal gas")
    ax.plot(V, P_vdW, "--b", label = "van der Waals gas")

    ax.set(xlabel = "$V (V_c$)", ylabel = "$P (P_c$)", title = "$T = {T}T_c$".format(T = T))

    ax.legend()
    ax.grid()

    plt.ylim([0, 3])

    fig.savefig("vdWVersusIdeal at {T}Tc.png".format(T = T))
    plt.show()
