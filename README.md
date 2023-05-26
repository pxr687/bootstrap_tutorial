# Part 1 - Data Science & The Fundamental Problem

## Definitions
Data science - the implementation of statistics using code and algorithms

We could also partly define data science as the science of dealing with data under uncertainty.

**The fundamental problem of data science**: what we care about are populations, but all we (usually!) have access to are samples.

More spcecifically: we care about populations and parameters but all we have access to are samples and statistics
 
[Sampling error illustration - population plots and misleading samples] - maybe do a univariate statistic first (probably sensible to use the income distribution), and show a biased static sample. Then a bivariate relationship between obviously unrelated variables (prefence for vanilla ice cream on a scale of 1 - 100, and religiosity - make a joke about I'm not sure if anyone has data on this.

[Setup confidence intervals as a helpful tool in response to the Fundamental Problem - they provide a probabilistic guide to what the true value of a population parameter based on a sample statistic]

[Today we'll look at one way of generating confidence intervals, using a data science approach]

[You don't need to understand python to follow this tutorial - I'll explain or demonstrate what each line of code is doing]

## Beginning of textbook page

Add comments to all code, and explain what each section is doing. <b> ALSO </b> use a colour scheme to differentiate populations from samples.

### Employee Compensation in the City of San Francisco¶

Maybe orient people to the data a little bit, but showing the column names?

For the section about the total compensations looking strange when sorted (some are negative), maybe a joke about this looking illegal? ("Now you might think this means that the department of X were charging employers for the pleasure of working for them, which sounds...illegal... but there is another explanation...").

"Fairly typical for an income distribution - a lot of people have a little, a lot of people have some and a very small number of people have a lot"

Explain why we're using the median (if you imagine "pulling" on the long tail of the distribution, as you do that the mean will "follow" the tail and get less representative, but the median will remain more representative of the data points)

Use "live" Boolean indexing to count proportion of people over a certain income threshold.

### A Random Sample and an Estimate

Maybe add a cell just to show what the sampling function is doing, that can be run multiple times, demonstrate the "replace" argument

Some more illustrations at the end of section, really linking back to the Fundamental Problem: we are in a luxury situation here, we can "see" the population data. Contrast this with the situation we are normally in. Maybe do a "field plot" e.g. I want you to image all the employees are standing at a random location in a very lare field... colour their points by their income, show a sample being draw that highlights which points are in the sample and shows the median (show a static unrepresentative median, and them some "live" draws

"A certain proportion of the time we are going to get unrepresentative samples, what we need is some estimate of how 

### The Bootstrap: Resampling from the Sample

Add a funny image for lifting up by the bootstraps?


### A Resampled Median

### Bootstrap Empirical Distribution of the Sample Median¶

Comment and explain function code. 

This section could do with "unrolling" and more illustrations etc. 

For the graph "Population Median and Intervals of Estimates" REALLY break down what the graph shows, what has gone into the intervals.

Hammer home CORRECT interpretation of the confidence interval and common misinterpretations. The "confidence" part of confidence intervals refers to the METHOD by which they are constructed <- mention Bayes intervals for another lecture!


# Section at end - what if we bootstrap from an unrepresentative sample?

Stack overflow answer: https://stats.stackexchange.com/questions/157639/bootstrapping-wont-always-return-population-statistics-so-why-say-it-does

"Bootstrapping cannot remedy an unrepresentative sample" <- this is why replication and open science are so important!
