import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Load the data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Take a look
df

# Slice out big forces
df_big_force = df[df['impact force (mN)'] > 1000]

# Look at it
df_big_force

#Finding correlations between two frog variables.
plt.plot(df['impact force (mN)'], df['adhesive force (mN)'], marker='.',
         linestyle='none')
plt.xlabel('impact force (mN)')
plt.ylabel('adhesive force (mN)')
