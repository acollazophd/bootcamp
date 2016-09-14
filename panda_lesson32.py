import numpy as np
import pandas as pd

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

#read the data
!head -n 20 data/frog_tongue_adhesion.csv



#a) Extract the impact time of all impacts that had an adhesive strength of
#magnitude greater than 2000 Pa.

df_adhesive_streng = df[df['adhesive strength (Pa)'] < -2000]

#read the file
df_adhesive_streng

#now make it a value equal to This
adh_sub = df_adhesive_streng = df[df['adhesive strength (Pa)'] < -2000]
adh_sub.loc[:, 'impact time (ms)']

#Extract the impact force and adhesive force for all of Frog II's strikes.
df.loc[df['ID']=='II', ['impact force (mN)', 'adhesive force (mN)']]

#Extract the adhesive force and the time the frog pulls on the target for
#juvenile frogs (Frogs III and IV).
df.loc[df['ID'].isin(['III', 'IV']), ['adhesive force (mN)', 'time frog pulls on target (ms)', 'ID']]

#Extract all of Frog I's impact forces and compute the mean.
