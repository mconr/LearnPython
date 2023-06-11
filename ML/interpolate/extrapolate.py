import numpy as np
from scipy import interpolate

# Generate a NumPy array with 20 random values
x = np.arange(1, 21)
y = np.random.randint(1, 100, size=20)

# Define a function to perform linear extrapolation
def extrapolate(x, y, x_new):
    f = interpolate.interp1d(x, y, kind='linear', fill_value="extrapolate")
    y_new = f(x_new)
    return y_new

# Extrapolate the data to the next 10 days
x_new = np.arange(21, 31)
y_new = extrapolate(x, y, x_new)

# Print the original values with their corresponding day numbers
print("Original values:")
for i in range(len(x)):
    print("Day", x[i], ":", y[i])

# Print the extrapolated values
print("\nExtrapolated values for the next 10 days:")
for i in range(len(x_new)):
    print("Day", x_new[i], ":", y_new[i])
