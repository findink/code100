# From: @lgq of CN/HITSZ/IOTS, 2022/06;
# To  : Everyone; with MIT license;
# What: plot data in format; 
#       input : data 
#       output: figure
# Updater:

import matplotlib.pyplot as plt
import numpy as np

from sklearn.manifold import TSNE
from sklearn.datasets import load_iris,load_digits
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import os

x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

def plot_y(y):
    plt.plot(y)
    plt.show()

def plot_xy(x,y):
    plt.plot(x,y)
    plt.show()


# 2022/06/20
def tsne_2D(x,y):
    X_tsne = TSNE(n_components=2,random_state=33).fit_transform(x)
    plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y,label="t-SNE")
    plt.legend()
    plt.show()


def tsne_3D(x,y):
    X_tsne = TSNE(n_components=3,random_state=33).fit_transform(x)
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(X_tsne[:, 0], X_tsne[:, 1],X_tsne[:, 2], c=y)
    plt.show()

    
