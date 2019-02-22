import numpy as np
import matplotlib.pyplot as plt



print("Type of fighter histogram.")
print("\n Info: This is a histogram made from datasets coll")

# Three types to classify
# Creating a data set of 1000 values for each item
striker = 1000
grappler = 1000
kicker = 1000


# Using the average landed strikes per fight to classify each type
striker__landed_strikes = 150 + 30 * np.random.randn(striker)
grappler_landed_strikes = 50 + 35 * np.random.randn(grappler)
kicker_landed_strikes = 75 + 40 * np.random.rand(kicker)

# Histogram for our three types of fighters
# Each type is given a color
# Striker = blue, grappler = red, kicker = green
plt.hist([striker__landed_strikes, grappler_landed_strikes, kicker_landed_strikes], stacked=True, color=['b', 'r', 'g'])
plt.show()
