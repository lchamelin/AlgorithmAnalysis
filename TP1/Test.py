import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [3,5,7,110] # 10, not 9, so the fit isn't perfect

fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit)
# fit_fn is no function which takes in x and returns an estimate for y

plt.plot(x,y, 'yo', x, fit_fn(x), '--k')


plt.show()