import numpy as np

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# We will use Seaborn styling to make plots look nicer Commented out
# here for demonstration later in this lesson
import seaborn as sns

rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.titlesize' : 18}
sns.set(rc=rc)

xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

low_min = np.min(xa_low)
low_max = np.max(xa_low)
high_min = np.min(xa_high)
high_max = np.max(xa_high)
global_min = np.max

# Reset bins, since xa_low has smaller values
#bins = np.arange(1600, 2501, 50)

# Generate the histogram for the low-density fed mother
#_ = plt.hist((xa_low, xa_high), bins=bins)

# Add axis labels
#plt.xlabel('Cross-sectional area (µm$^2$)')
#plt.ylabel('count')

# Add a legend
#plt.legend(('low', 'high'), loc='upper right')

# You need this is you didn't use %matplotlib in IPython shell
#plt.show()

# Reset bins, since xa_low has smaller values
bins = np.arange(1600, 2501, 50)

# Generate the histogram for the low-density fed mother
_ = plt.hist(xa_low, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
_ = plt.hist(xa_high, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)

# Add axis labels
plt.xlabel('Cross-sectional area (µm$^2$)')
plt.ylabel('count')

# Add a legend
plt.legend(('low', 'high'), loc='upper right')

#save the figure
plt.savefig('egg_area_histograms.svg', bbox_inches='tight')

# You need this is you didn't use %matplotlib in IPython shell
plt.show()
