# plotting functions for the bootstrap page
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def population_plot(population_size = 10000):
    """Creates a population of observations and plots it"""
    # generate a population of observations
    population = np.random.normal(loc = 48, scale = 10,
                                  size = population_size).round(2)

    # plot a histogram of the population data, showing the mean, and with axis
    # labels
    plt.hist(population, label = "Population")
    plt.axvline(population.mean(), color = "darkblue", label = 'Population Mean')
    plt.xlabel('Approval Rating (%)')
    plt.ylabel('Frequency')
    plt.legend(bbox_to_anchor = (1, 1))
    plt.show()

    # return the population data so that it can be used with other functions
    return population

def population_plot_with_sample(population, sample_size = 20):
    """Takes population of observations and plots it. Draws a random sample from
    the population, and plots that alongside the population data."""
    # draw a sample from the population data
    sample = np.random.choice(population, size = sample_size)

    # plot the population data, the sample data, and the mean of each, with axis
    # labels
    plt.hist(population, label = "Population")
    plt.scatter(sample, np.repeat(20, len(sample)), marker = "|", color = 'red',
                                   label = "Sample Elements")
    plt.axvline(population.mean(), color = "darkblue",
                                   label = 'Population Mean')
    plt.axvline(sample.mean(), color = "darkred", label = 'Sample Mean')
    plt.xlabel('Approval Rating (%)')
    plt.ylabel('Frequency')
    plt.legend(bbox_to_anchor = (1, 1))
    plt.show()

def population_plot_with_unrepresentative_sample(population, sample_size = 20):
    """Takes population of observations and plots it. Draws a nonrandom sample 
    from the population, and plots that alongside the population data."""
    # randomly set the direction of extremeness for the sample
    if np.random.choice([0, 1]) == 0:
        extreme = population > 60
    else:
        extreme = population < 40

    # draw the unrepresentative sample
    sample = np.random.choice(population[extreme], size = sample_size)

    # plot the population data, the sample data, and the mean of each, with axis
    # labels
    plt.hist(population, label = "Population")
    plt.scatter(sample, np.repeat(20, len(sample)), marker = "|",
                color = 'red', label = "Sample")
    plt.axvline(population.mean(), color = "darkblue",
                label = 'Population Mean')
    plt.axvline(sample.mean(), color = "darkred", label = 'Sample Mean')
    plt.xlabel('Approval Rating (%)')
    plt.ylabel('Frequency')
    plt.legend(bbox_to_anchor = (1, 1))
    plt.show()

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
    plt.scatter(sample, np.repeat(20, len(sample)), marker = "|", color = 'red',
                                   label = "Sample Elements")
    plt.axvline(population.median(), color = "darkblue", 
                label = 'Population Median')
    plt.axvline(np.median(sample), color = "darkred", label = 'Sample Median')
    plt.ylabel('Frequency')
    add_x_labels_total_compensation()
    plt.show()


def add_x_labels_total_compensation():
    """Convenience function for adding x-axis labels and showing the legend."""
    plt.legend(bbox_to_anchor = (1, 1))
    plt.xlabel('Total Compensation')
    plt.xticks(rotation = 60)