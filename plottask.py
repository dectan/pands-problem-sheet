import numpy as np
import matplotlib.pyplot as plt

# Define the function h(x) = x^3
def h(x):
    return x ** 3

# Generate a range of x-values from 0 to 10
x = np.linspace(0, 10)

# Evaluate h(x) for each value of x
y = h(x)

# Create a plot of h(x) vs. x
plt.plot(x, y)

# Add labels to the x- and y-axes
plt.xlabel('x')
plt.ylabel('h(x)')

# Set the title of the plot
plt.title('Plot of h(x) = x^3 in the range [0, 10]')

# Show the plot
#plt.show()


# Generate 1000 random values from a normal distribution with mean 5 and standard deviation 2
data = np.random.normal(5, 2, 1000)

# Create a histogram
plt.hist(data)

# Add labels and a title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Normal Distribution (mean=5, std=2)')

# Show both of the plots
plt.show()