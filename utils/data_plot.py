# From: @lgq of CN/HITSZ/IOTS, 2022/06;
# To  : Everyone; with MIT license;
# What: plot data in format; 
#       input : data 
#       output: figure
# Updater:

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

def plot_y(y):
    plt.plot(y)
    plt.show()

def plot_xy(x,y):
    plt.plot(x,y)
    plt.show()
