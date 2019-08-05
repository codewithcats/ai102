#%%
import numpy as np

#%%
def matrix(input):
    return np.array(np.mat(input))


#%%
x_train = matrix("""
40 1.72;
49 1.62;
58 1.71;
51 1.80;
81 1.59;
92 1.50;
100 1.58;
91 1.68
""")
x_train

#%%
y_train = np.array([
    "T",
    "T",
    "T",
    "T",
    "F",
    "F",
    "F",
    "F"
]).reshape(-1, 1)
y_train
#%%
x_valid = matrix("""
50 1.70;
90 1.60;
75 1.65
""")
x_valid

#%%
y_valid = np.array([
    "T",
    "F",
    "F",
]).reshape(-1, 1)
y_valid


#%%
def normalize(input):
    min = input.min(axis=0, keepdims=True)
    max = input.max(axis=0, keepdims=True)
    return (input - min)/(max - min)

normalize(x_train)

#%%
