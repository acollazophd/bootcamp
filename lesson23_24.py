import numpy as np
#import scipy.special
import scipy.stats
#import bootcamp_utils

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

data_txt = np.loadtxt('data/collins_switch.csv', delimiter=',', skiprows=2)

iptg = data_txt[:,0]
gfp = data_txt[:,1]
sem = data_txt[:,2]

#Practice exercise 3


#Practice exercise 1
#plot ipgt vs gfp
#plt.plot(iptg, gfp, marker='.', linestyle='none')
# plt.semilogx(iptg, gfp, marker='.', linestyle='none', markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG Titration - Semilog X')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.show()

#Practice exercise 2
# plt.errorbar(iptg, gfp, yerr=sem, marker='.', linestyle='none', markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG Titration - Semilog X')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.xscale('log')
# plt.show()
