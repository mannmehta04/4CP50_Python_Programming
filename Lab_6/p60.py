import numpy as np
from pylab import *

x = np.linspace(-3, 3, 50)
y = x**2

fig, ax = subplots(figsize=(8,6))

ax.plot(x, y, 'r-', linewidth=2, label='$y = x^2$')

ax.set_xlabel('$x$', fontsize=14)
ax.set_ylabel('$y$', fontsize=14)
ax.set_title('Parabolic Function', fontsize=16)

ax.legend(loc='upper left', fontsize=12)

show()