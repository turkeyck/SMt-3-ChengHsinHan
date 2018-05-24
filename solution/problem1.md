### Problem1

#### 1.
_Write a program to compute and plot V as a function of P at constant T for the van der Waals gas._
##### _<Solution\>_
source code: [vdW_versus_ideal.py](https://github.com/NTHU-Phys-Qubit/SMt-3-ChengHsinHan/blob/master/solution/vdW_versus_ideal.py)  

The equation I write in this code file for the van der Waals gas is based on equation 17.12, which we almost reach in HW 5, problem 17-1, in textbook written by Robert H.Swendsen. It is valid because ![P_tilde](https://latex.codecogs.com/png.latex?%5Cbg_white%20%5Ctilde%7BP%7D), ![V_tilde](https://latex.codecogs.com/png.latex?%5Cbg_white%20%5Ctilde%7BV%7D) and ![T_tilde](https://latex.codecogs.com/png.latex?%5Cbg_white%20%5Ctilde%7BT%7D) are simply a rescale of the unit (to critical quantities of each).

#### 2.
_Modify your program to include a comparison curve for the ideal gas law at the same temperature._
##### _<Solution\>_
source code:
[vdW_versus_ideal.py](https://github.com/NTHU-Phys-Qubit/SMt-3-ChengHsinHan/blob/master/solution/vdW_versus_ideal.py)

#### 3.
_Make plots for values of T that are at, above, and below Tc._
##### _<Solution\>_
source code:
[vdW_versus_ideal.py](https://github.com/NTHU-Phys-Qubit/SMt-3-ChengHsinHan/blob/master/solution/vdW_versus_ideal.py)
![T=0.9T_c](https://latex.codecogs.com/png.latex?%5Cbg_white%20T%3D0.9T_c):  
![plot1](https://github.com/NTHU-Phys-Qubit/SMt-3-ChengHsinHan/blob/master/solution/vdW_versus_ideal_at_0.9Tc.png)

![T=T_c](https://latex.codecogs.com/png.latex?%5Cbg_white%20T%3DT_c):  
![plot2](https://github.com/NTHU-Phys-Qubit/SMt-3-ChengHsinHan/blob/master/solution/vdW_versus_ideal_at_1.0Tc.png)

![T=1.1T_c](https://latex.codecogs.com/png.latex?%5Cbg_white%20T%3D1.1T_c)  
![plot3](https://github.com/NTHU-Phys-Qubit/SMt-3-ChengHsinHan/blob/master/solution/vdW_versus_ideal_at_1.1Tc.png)

#### 4.
_For some values of temperature, the plots will have a peculiar feature. What is it?_
##### _<Solution\>_
From the solution of last question, we can see that **when the temperature is at the critical temperature**, there is a nearly horizontal line in the P-V curve of van der Waals gas, which is quite peculiar.

#### 5.
_Make a plot of the chemical potential *μ* as a function of *P*. You might want to include a plot of *V* vs. *P* for comparison. <p> What does the plot of *μ* vs. *P* look like at, above, and below *Tc*? <p> The data you need to do a numerical integration of the Gibbs-Duhem relation is the same as you’ve already calculated for the first plot in this assignment. You just have to multiply the volume times the change in P and add it to the running sum to calculate μ vs. P._
##### _<Solution\>_
source code: [muP_and_VP_plots.py](https://github.com/NTHU-Phys-Qubit/SMt-3-ChengHsinHan/blob/master/solution/muP_and_VP_plots.py)  

The equation of the chemical potential in this source file is based on equation 17.17 in textbook written by Robert H.Swendsen, with N being set to 1.  

![T=0.9T_c](https://latex.codecogs.com/png.latex?%5Cbg_white%20T%3D0.9T_c):  
![plot4](https://github.com/NTHU-Phys-Qubit/SMt-3-ChengHsinHan/blob/master/solution/mu-P_V-P_at_0.9T_c.png)

![T=T_c](https://latex.codecogs.com/png.latex?%5Cbg_white%20T%3DT_c):  
![plot5](https://github.com/NTHU-Phys-Qubit/SMt-3-ChengHsinHan/blob/master/solution/mu-P_V-P_at_1.0T_c.png)

![T=1.1T_c](https://latex.codecogs.com/png.latex?%5Cbg_white%20T%3D1.1T_c)  
![plot6](https://github.com/NTHU-Phys-Qubit/SMt-3-ChengHsinHan/blob/master/solution/mu-P_V-P_at_1.1T_c.png)

As we can see, when the temperature is _below_ critical temperature, because volume is not a function of pressure - for a specific pressure, there may be multiple value of volume - chemical potential would also _not_ behave as a function of pressure. There are even crosses in the plot.
  
When the temperature is _at_ critical temperature, volume is a function of pressure **except** when the pressure is at critical prssure. As a result, there is a discontinuity of the slope of the tangent line at that point in the chemical potential plot, as shown.

When the temperature is _above_ critical temperature, volume is a function of preesure. So the chemical potential plot wouldn't behave strange.
