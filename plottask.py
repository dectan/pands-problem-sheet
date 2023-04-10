#https://stackoverflow.com/questions/20011494/plot-normal-distribution-with-matplotlib
#https://chat.openai.com/chat


import numpy as np
import matplotlib.pyplot as plt

# Define the function h(x) = x^3
def h(x):
    return x ** 3

#Create an array of x values in the range 0, 10 and get y values using h(x) = x^3
x = np.linspace(1, 10)

y = h(x)

# Create a plot of h(x) vs. x
plt.plot(x, y, label='H(x) = x^3', color="red")

# Add labels to the x- and y-axes
#plt.xlabel('x')
#plt.ylabel('h(x)')

# Set the title of the plot
#plt.title('Plot of h(x) = x^3 in the range [0, 10]')

# Show the plot
#plt.show()


# Generate 1000 random values from a normal distribution with mean 5 and standard deviation 2
data = np.random.normal(5, 2, 1000)

# Create a histogram
plt.hist(data, bins = 10, label = 'Normal Distribution', color = "green")

# Add labels and a title
plt.xlabel('Value',fontsize="16",font = "Lucida Console")
plt.ylabel('Frequency',fontsize="16",font = "Lucida Console")
plt.title('Week 08 Task plottask.py',font = "Lucida Console",fontsize="20",color="orange")
plt.legend()
# Show both of the plots
plt.show()