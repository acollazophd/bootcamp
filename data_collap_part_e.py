import numpy as np
#import scipy.special
import scipy.stats

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#Load data
wt_lac = np.loadtxt('data/wt_lac.csv', comments='#', delimiter=',', skiprows=3)
q18m_lac = np.loadtxt('data/q18m_lac.csv', comments='#', delimiter=',', skiprows=3)
q18a_lac = np.loadtxt('data/q18a_lac.csv', comments='#', delimiter=',', skiprows=3)

#function for computer fold change
def fold_change_bohr(bohr):
    fc = 1 / (1 + np.e**(-bohr))
    return(fc)

#Define the variables
iptg_wt = wt_lac[:,0]
fold_wt = wt_lac[:,1]

iptg_q18m = q18m_lac[:,0]
fold_q18m = q18m_lac[:,1]

iptg_q18a = q18a_lac[:,0]
fold_q18a = q18a_lac[:,1]

# cwt = fold_change(iptg_wt, 141.5)
# cq18m = fold_change(iptg_q18m, 16.56)
# cq18a = fold_change(iptg_q18a, 1328)


# Make smooth x-values
# c = np.logspace(-6, 2, 400)

b = np.linspace(-6, 6, 400)

curve = fold_change_bohr(b)

plt.plot(b, curve)

#Added this from exercise solution of one of the students because of bbox_inches
plt.savefig('exercise3.2f_bohrParam.svg', bbox_inches='tight')

plt.show()

# wt_theor = fold_change(c, 141.5)
# q18m_theor = fold_change(c, 16.56)
# q18a_theor = fold_change(c, 1328)

#Plotting of IPTG concentration for these
# plt.semilogx(iptg_wt, fold_wt, marker='.', linestyle='none', markersize=20, alpha=0.5)
# plt.semilogx(iptg_q18m, fold_q18m, marker='.', linestyle='none', markersize=20, alpha=0.5)
# plt.semilogx(iptg_q18a, fold_q18a, marker='.', linestyle='none', markersize=20, alpha=0.5)

# plt.xlabel('IPTG (mM)')
# plt.ylabel('Fold Change')
# plt.legend(('wt_lac', 'q18m_lac', 'q18a_lac'), loc='lower right')
# plt.margins(0.1)
# plt.title('IPTG Titration (Log Log)')
#plt.show()

#Plotting of IPTG concentration for these
# plt.loglog(cwt, fold_wt, marker='.', linestyle='none', markersize=20, alpha=0.5)
# plt.loglog(cq18m, fold_q18m, marker='.', linestyle='none', markersize=20, alpha=0.5)
# plt.loglog(cq18a, fold_q18a, marker='.', linestyle='none', markersize=20, alpha=0.5)

# plt.semilogx(c, wt_theor, marker='', markersize=20, alpha=0.5)
# plt.semilogx(c, q18m_theor, marker='.', linestyle='none', markersize=20, alpha=0.5)
# plt.semilogx(c, q18a_theor, marker='.', linestyle='none', markersize=20, alpha=0.5)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Fold Change')
# plt.legend(('wt_lac', 'q18m_lac', 'q18a_lac', 'wt_theor', 'q18m_theor', 'q18a_theor'), loc='lower right')
# plt.margins(0.1)
# plt.title('IPTG Titration (Semilogx)')
# plt.show()
