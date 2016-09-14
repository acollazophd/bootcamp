import numpy as np
#import scipy.special
import scipy.stats
#import bootcamp_utils
import bootcamp_utils
# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

def ecdf(data):
    """
    Compute x, y values for an empirical distribution function
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y

#Load data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

x_high, y_high = bootcamp_utils.ecdf(xa_high)
x_low, y_low = bootcamp_utils.ecdf(xa_low)



# Make smooth x-values
x = np.linspace(1600, 2500, 400)

# Compute theoretical Normal distribution
cdf_high = scipy.stats.norm.cdf(x, loc=np.mean(xa_high), scale=np.std(xa_high))
cdf_low = scipy.stats.norm.cdf(x, loc=np.mean(xa_low), scale=np.std(xa_low))

plt.plot(x_high, y_high, marker='.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(x_low, y_low, marker='.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(x, cdf_high, color='gray')
plt.plot(x, cdf_low, color='gray')
plt.xlabel('Cross-sectional area (um)')
plt.ylabel('eCDF')
plt.legend(('high food', 'low food'), loc='lower right')
plt.show()
