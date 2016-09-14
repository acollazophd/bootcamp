import numpy as np

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#Load data files from Grant works
bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
bs_replicate = np.mean(bs_sample)
bs_replicate

# Number of replicas
n_reps = 100000

# Initialize bootstrap replicas array
bs_replicates_1975 = np.empty(n_reps)

# Compute replicates
for i in range(n_reps):
    bs_sample = np.random.choice(bd_1975, size=len(bd_1975))
    bs_replicates_1975[i] = np.mean(bs_sample)

conf_int_1975 = np.percentile(bs_replicates_1975, [2.5, 97.5])

# Number of replicas
n_reps = 100000

# Initialize bootstrap replicas array
bs_replicates_2012 = np.empty(n_reps)

# Compute replicates for mean in this case but could us np.std as well
for i in range(n_reps):
    bs_sample = np.random.choice(bd_2012, size=len(bd_2012))
    bs_replicates_2012[i] = np.mean(bs_sample)

# Compute the confidence interval
conf_int_2012 = np.percentile(bs_replicates_2012, [2.5, 97.5])


def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)


# Generate 1000 random numbers on uniform interval
n = np.random.random(size=1000)
np.empty()


#Define a function with call signature draw_bs_reps(data, func, size=1),
#where func is a function that takes in an array and returns a statistic.
def draw_bs_reps(data, np.mean(), size=1):
    return np.random.random(size=1000)


for i in range(np.random.choice):



# # Compute ECDFs for 1975 and 2012
# x_1975, y_1975 = ecdf(bd_1975)
# x_2012, y_2012 = ecdf(bd_2012)
# x_1975_bs, y_1975_bs =ecdf(bs_sample)
#
#from second lesson
#
# # Plot the ECDFs
# plt.plot(x_1975, y_1975, marker='.', linestyle='none')
# plt.plot(x_1975_bs, y_1975_bs, marker='.', linestyle='none', alpha=0.5)
# plt.margins(0.02)
# plt.xlabel('beak depth (mm)')
# plt.ylabel('ECDF')
# plt.legend(('1975', 'bootstrap'), loc='lower right')


#from first lesson

# # Plot the ECDFs
# plt.plot(x_1975, y_1975, marker='.', linestyle='none')
# plt.plot(x_2012, y_2012, marker='.', linestyle='none')
# plt.margins(0.02)
# plt.xlabel('beak depth (mm)')
# plt.ylabel('ECDF')
# plt.legend(('1975', '2012'), loc='lower right')
#
# plt.show()
