import numpy as np
import matplotlib.pyplot as plt

# Generating some random data
# for an example
data = [1,1,1,1,1,2,3,4,1,4,2]

# Plotting the histogram.
plt.hist(data.sort(), bins=25, density=True, alpha=0.6, color='b')

plt.show()


