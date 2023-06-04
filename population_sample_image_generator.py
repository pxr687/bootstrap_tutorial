# generates a plot that shows the population data, and random sampling, in real time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, Markdown

def field_plot(babies_pop, fontsize = 8, figsize = (12,12), 
               fontweight = "ultralight"):
    """Generates a plot that shows the population data, and random sampling,
    in real time."""

    n_rows = 103
    n_cols = 12

    # create a figure
    plt.figure(figsize = figsize)

    # show population data 
    plt.subplot(1, 2, 1)
    count = 0
    for i in np.arange(n_rows):
        for j in np.arange(n_cols):
            plt.text(j, i,
                babies_pop['birthweight_kg'].iloc[count].round(1).astype("str"),
                size = fontsize,  ha='center', va='center', color='black', 
                weight = fontweight, snap = True)
            count = count + 1
            
    # adjust axes
    plt.title(f"Population mean = ${babies_pop['birthweight_kg'].mean().round(2)}$")
    plt.xlim(-0.5, n_cols + 0.5)
    plt.ylim(-0.5, n_rows + 0.5)
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')

    # show faded population data, and highlighted sample
    plt.subplot(1, 2, 2)
    sample_indexes = np.random.choice(np.arange(len(babies_pop)), 25)
    count = 0
    for i in np.arange(n_rows):
        for j in np.arange(n_cols):
            if count not in sample_indexes:
                plt.text(j, i,
                        babies_pop['birthweight_kg'].iloc[count].round(1).astype("str"),
                         ha='center', va='center',
                        size = fontsize,
                        color='grey',
                        weight= fontweight,
                        snap=True, alpha = 0.5)
                count = count + 1
            else:
                plt.text(j, i,
                        babies_pop['birthweight_kg'].iloc[count].round(1).astype("str"),
                        ha='center', va='center',
                        size = fontsize,
                        color='red',
                        weight='bold',
                        snap=True)
                count = count + 1
    plt.title(f"Random Sample Mean = ${babies_pop['birthweight_kg'].iloc[sample_indexes].mean().round(2)}$")

    # adjust axes
    plt.xlim(-0.5, n_cols + 0.5)
    plt.ylim(-0.5, n_rows + 0.5)
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')
    plt.show()
