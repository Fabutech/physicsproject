import sys
import matplotlib.pyplot as plt
import numpy as np

x = sys.argv[1].split(",")
y = sys.argv[2].split(",")
x = [float(i) for i in x]
y = [int(j) for j in y]

coef = np.polyfit(x,y,deg=1)
poly1d_fn = np.poly1d(coef) 

print(poly1d_fn)

ax2 = plt.subplot(1, 1, 1)

ax2.plot(x, poly1d_fn(x), color="#028A0F", lw=2, label="Line of best fit") 

ax2.set_title("Change in temperature compared to change in pressure", y=1.035)
ax2.set_xlabel("Temperature (T / °C)")
ax2.set_ylabel("Pressure (p / mm Hg)")

plt.legend()

plt.savefig("public/Assets/chart2.png")