import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

x = np.linspace(-3,3,50)
y = np.exp(-x**2) + 0.1 * np.random.randn(50)

plt.plot(x,y,'ro', ms=5)

spl = UnivariateSpline(x,y)
xs = np.linspace(-3,3,1000)
plt.plot(xs,spl(xs),'g',lw=3)

spl2 = UnivariateSpline(x,y)
spl2.set_smoothing_factor(0.5)
plt.plot(xs,spl2(xs),'b',lw=3)

spl3 = UnivariateSpline(x,y)
spl3.set_smoothing_factor(0.1)
plt.plot(xs,spl3(xs),'y',lw=3)




plt.plot(xs,spl(xs),'g',lw=3)
plt.show()
