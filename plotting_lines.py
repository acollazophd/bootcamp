import numpy as np
import scipy.special

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# The following is specific Jupyter notebooks
#%matplotlib inline
#%config InlineBackend.figure_formats = {'png', 'retina'}

# The x-values we want
x = np.linspace(-15, 15, 400)

# The normalized intensity
norm_I = 4 * (scipy.special.j1(x) / x)**2

#plat our application
plt.close()
plt.plot(x, norm_I, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('$x$')
plt.ylabel('$I(x)/I_0$')

#Processing spike data

# Load in data set
data = np.loadtxt('data/retina_spikes.csv', skiprows=2, delimiter=',')

# Slice out time and voltage
t = data[:,0]
V = data[:,1]

plt.close()
plt.plot(t, V)
plt.xlabel('t (ms)')
plt.ylabel('V (µV)')
plt.xlim(1395, 1400)
