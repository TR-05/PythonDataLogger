from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
import time
import dataClass as dc
import math
import numpy as np

FPS = 60.0
# Data save time
save_time = 4
num_graphs = 2



# number of data points
n = FPS * save_time
refresh_rate = 1.0 / FPS

# Calculate the number of subplots needed
num_plots = num_graphs + 1

# Determine the number of rows and columns needed
num_cols = 3  # You can adjust this based on your preference
num_rows = (num_plots + num_cols - 1) // num_cols  # Calculate the number of rows needed

# Create the subplots
figure, axs = pyplot.subplots(nrows=num_rows, ncols=num_cols, figsize=(15, 7))

# Flatten the axs array for easy indexing
axs = axs.flatten()

# Create a list to store dataClass objects
data_classes = [dc.dataClass(refresh_rate, save_time, axs[i]) for i in range(num_graphs)]

start_time = time.time()
# Updates the data list, keeping the same length and removing the oldest element
def updateData(frame):
    t = time.time() - start_time
    # Iterate through the list and call addData for each dataClass object
    for data_class in data_classes:
        data_class.addData(t, math.sin(.5 * t))
    # Return the updated lines
    return [data_class.line for data_class in data_classes]

img = pyplot.imread("Assets/VURC-HighStakes-H2H-TileColor66_71-2000x2000.png")
img = np.clip(img, 0, 1)
# Create a figure and an axis
axs[num_graphs].imshow(img, extent=[0, 144, 0, 144], zorder=0, animated=False)  # Changed to valid index [1, 2]


# Define the labels for each subplot
y_labels = [['d1', 'd2', 'd3'], ['d3', 'y (inch)', 'd1']]

for i in range(len(axs) -1):
        axs[i].set_xlabel('Time (s)')
        #axs[i].set_ylabel(y_labels[i])
        axs[i].grid(True)
axs[num_graphs].grid(False)

animation = FuncAnimation(figure, updateData, interval=(refresh_rate * 1000.0), blit=True, cache_frame_data=True)
pyplot.show()