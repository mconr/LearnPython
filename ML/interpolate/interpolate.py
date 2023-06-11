import numpy as np
from scipy import interpolate

# create a sample array with some missing values
arr = np.array([1, 3, 8, 10, 12, 15, np.nan,np.nan,np.nan,np.nan, 15, 26,30, 45, np.nan,np.nan,np.nan, 28, 39])

# find the indices of the missing values
missing_indices = np.where(np.isnan(arr))[0]
print(missing_indices)

# create a function for linear interpolation
available_indices = np.where(~np.isnan(arr))[0]
print(available_indices)

x=available_indices
y=arr[available_indices]
print(x)
print(y)
