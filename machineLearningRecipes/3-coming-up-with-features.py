import numpy as np
import matplotlib.pyplot as plt


greyhounds = 500
labs = 500

grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_height = 24 + 4 * np.random.randn(labs)

plt.hist([grey_height, lab_height], stacked=True, color = ['r', 'b'])
plt.show()

# Choosing a good feature
#   Avoid useless (or misleading) features
#   Choose independent features
#   Avoid redundant features
#   Easy to understand
#       Ex: Given the option of Longitude & Latitude vs "Net Distance", choose "Net Distance" for ease of understanding