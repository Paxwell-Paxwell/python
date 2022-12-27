import numpy as np
import matplotlib.pyplot as plt

# Generate the t array using linspace with the given start, stop, and number of points 
t = np.linspace(-0.04, 0.04, 40*200)

# Calculate X1 and X2 using the given equations
X1 = 20*np.cos(2*np.pi*40*(t-0.0075)-0.4*np.pi)
X2 = 20*np.cos(2*np.pi*40*(t-0.0075)-0.4*np.pi)

# Plot X1 and X2 as a function of t
plt.plot(t, X1, label='X1')
plt.plot(t, X2, label='X2')

# Add a legend and labels to the x and y axes
plt.legend()
plt.xlabel('t')
plt.ylabel('X1, X2')

# Display the plot
plt.show()
