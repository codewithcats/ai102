#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

#%%
x = np.random.randint(0, 100, (16, 2))
x

#%%
y = np.random.randint(0, 100, (1, 2))
y



#%%
np.sqrt(((x-y)**2).sum(axis=1))

#%%

distance_2d = lambda x, y: np.sqrt(((x-y)**2).sum(axis=1))
