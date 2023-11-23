import matplotlib.pyplot as plt

# Example: Generating random data for demonstration
import numpy as np

data = np.random.randn(1000)  # Replace this line with your list of 1000 values

# Creating the histogram
plt.hist(data, bins=30, alpha=0.5)  # Adjust the number of bins as needed
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of 1000 Values")
plt.show()
