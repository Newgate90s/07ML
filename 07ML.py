import numpy as np
import matplotlib.pyplot as plt

bombers = 500
fighters = 500

# Average wingspan of a bomber is 28 feet
# Average wingspan of a fighter is 24 feet
# I am going to add plus/minus 4 feet to each different type of plane wingspan

bomber_wingspan = 28 + 4 * np.random.randn(bombers)
fighter_wingspan = 24 + 4 * np.random.randn(fighters)

# Visualize our data in a histogram
# Bombers in blue and fighters in red

plt.hist([bomber_wingspan, fighter_wingspan], stacked=True, color=['b', 'r'])
plt.show()
