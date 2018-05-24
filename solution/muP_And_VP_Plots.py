"""************************************************************
Written by Cheng-Hsin Han (gsjh80317cla@gmail.com)
************************************************************"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# The values of volume V, temperature T, and pressure P are all being rescaled
# in the units of critical volume V_c, critical temperature T_c and critical
# pressure P_c in this program. Thus are all dimensionless.

# the value of the range and number of bins for the volume
Vmin = 0.4
Vmax = 3.0
n_bin = 1000

# I plus one in n_bin here for I need when calculating chemical potential
V = np.linspace(Vmin, Vmax, n_bin + 1)

# this list would contain the vertical position of interest
vertical_line = [0.65, 1]

# make plots for T = 0.9T_c, 1.0 T_c, and 1.1 T_c
for step in range(3):
    T = 0.9 + 0.1 * step
    P_vdW = 8 * T / (3 * V - 1) - 3 / V**2

    mu = []   # would store the chemical potential
    u = 0     # initial value of chemical potential

    # this index would store the index of chemical potential whose value
    # would give the plots better performance
    chosen_index = 0
    max_x = 3
    for j in range(len(V[:-1])): # minus 1 here to ensure the index doesn't surpass the length
        u += V[j] * (P_vdW[j + 1] - P_vdW[j])
        mu.append(u)
        if P_vdW[j] > max_x:
            chosen_index = j - 1

    fig, ax = plt.subplots()

    plt.subplot(2, 1, 1)
    plt.plot(P_vdW[:-1], mu, "-,")
    plt.title("$mu-P$ curve and $V-P$ curve of van der Waals gas at $T = {T}T_c$".format(T = T))
    plt.ylabel("$mu (P_c V_c$)")
    plt.xlim([0, max_x])
    plt.ylim([min(mu), mu[chosen_index]])
    if step != 2:
        plt.vlines(x = vertical_line[step], ymin = min(mu), ymax = mu[chosen_index], linestyle = "dashed")

    plt.subplot(2, 1, 2)
    plt.plot(P_vdW[:-1], V[:-1], "-,")
    plt.xlabel("$P (P_c$)")
    plt.ylabel("$V (V_c$)")
    plt.xlim([0, max_x])
    if step != 2:
        plt.vlines(x = vertical_line[step], ymin = Vmin, ymax = Vmax, linestyle = "dashed")

    fig.savefig("mu-P_V-P_at_{T}T_c.png".format(T = T))
    plt.show()
