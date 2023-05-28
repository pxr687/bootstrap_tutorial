# plotting functions for the bootstrap page
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, Markdown

def population_plot_sf_data(sf2015, bins = []):
    """Plot the population data from sf2015 dataframe"""
    population = sf2015['Total Compensation']

    # plot a histogram of the population data, showing the median, and with axis
    # labels
    plt.hist(population, label = "Population", bins = bins)
    plt.axvline(population.median(), color = "darkblue", 
                label = 'Population Median')
    plt.ylabel('Frequency')
    add_x_labels_total_compensation()
    plt.show()

def population_plot_sf_data_with_sample(sf2015, bins = [], sample_size = 500):
    """Plot the population data from sf2015 dataframe, draw a random sample and
    show it."""
    population = sf2015['Total Compensation']

    sample = np.random.choice(population, size = sample_size, replace = False)

    # plot a histogram of the population data, showing the median, and with axis
    # labels
    plt.hist(population, label = "Population", bins = bins)
    plt.axvline(population.median(), color = "darkblue", 
                label = 'Population Median')
    plt.scatter(sample, np.repeat(20, len(sample)), marker = "|", color = 'red',
                                   label = "Sample Elements")
    plt.axvline(np.median(sample), color = "darkred", label = 'Sample Median')
    plt.ylabel('Frequency')
    add_x_labels_total_compensation()
    plt.show()

def add_x_labels_total_compensation():
    """Convenience function for adding x-axis labels and showing the legend."""
    plt.legend(bbox_to_anchor = (1, 1))
    plt.xlabel('Total Compensation')
    plt.xticks(rotation = 60)

def plot_our_sample(our_sample, sf_bins):
    our_sample.plot.hist(bins=sf_bins, color = 'red', label = "Sample")

    # show the sample median
    plt.axvline(np.median(our_sample), color = 'darkred', label = "Sample Median")

    # show the legend, add x-axis labels
    add_x_labels_total_compensation()
    plt.show()

    display(Markdown(f"Sample Median = {round(np.median(our_sample))}"))