import sys
import matplotlib.pyplot as plt
import numpy as np
import json

# os.remove("/public/chart.png")

x = sys.argv[1].split(",")
y = sys.argv[2].split(",")
x = [float(i) for i in x]
y = [int(j) for j in y]

def extended(ax, x, y, **args):

    xlim = [-300, max(x)+10]
    ylim = [-50, max(y)]

    x_ext = np.linspace(xlim[0], xlim[1], 100)
    p = np.polyfit(x, y , deg=1)
    y_ext = np.poly1d(p)(x_ext)
    ax.plot(x_ext, y_ext, **args)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    return ax

def get_x(y, coef):
    xx = (y - coef[1])/coef[0]
    return xx

coef = np.polyfit(x,y,deg=1)
poly1d_fn = np.poly1d(coef) 

ax2 = plt.subplot(1, 1, 1)

ax2 = extended(ax2, x, y,  color="#0981D1", lw=2, label="extended")
ax2.scatter([get_x(0, coef)], [0], color="red")

ax2.text(get_x(0, coef)+13, -12, round(get_x(0, coef), 1), size=12)

print(round(get_x(0, coef), 4))

ax2.plot(x, poly1d_fn(x), color="#028A0F", lw=2, label="original") 

ax2.set_title("Extended to p = 0 mm Hg", y=1.035)
ax2.set_xlabel("Temperature (T / °C)")
ax2.set_ylabel("Pressure (p / mm Hg)")

plt.legend()

plt.savefig("public/Assets/chart1.png")