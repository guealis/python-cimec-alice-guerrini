# Anorexia Treatment Comparison Study
This project analyzes data from an experimental study conducted by Prof. Brian Everitt, focusing on the effects of various treatments for young girls suffering from anorexia. 

For the analysis I tried to replicate the statistical methods described in the book "Statistical Methods for the Social Sciences" (FIFTH EDITION) by Alan Agresti.

### The CORRECT FILE to run is anorexia_dat_treat_analysis.py

## Overview
The dataset contains weight measurements (in pounds) taken before and after a fixed treatment period. Participants were randomly assigned to one of three treatment groups:

* Cognitive Behavioral Therapy
* Family Therapy
* Control Group

Here, weights were converted from pounds to kilograms.

## Project Structure
The analysis is divided into two main parts:

## 1. Descriptive Statistics and Repeated Measures ANOVA
### Descriptive Statistics:
  * Computed for weights before and after the experimental period, segmented by treatment group.
  * Includes measures like mean, standard deviation, median, and quartiles.
### Visualization:
  * Plots to graphically describe the response distributions before and after the experimental period for each treatment.
### Repeated Measures ANOVA:
  * Conducted using the Pingouin statistical package to assess whether there are statistically significant differences in weight change across the three treatment groups.

## 2. Focused Analysis on Weight Change
### Weight Change Analysis:
* Specifically focuses on the weight change after Cognitive Behavioral Therapy and compares it to the weight change in the control group.
### Two-Sample T-Test:
* Performed to determine if there is a significant difference in weight change between these two groups.
  
## Custom Functions
Two custom functions were developed to aid in the analysis:

    hypothesis_test_result():

Facilitates interpretation of statistical test results by determining whether to reject or fail to reject the null hypothesis based on the p-value.

    eff_size():

Calculates Cohen's d, a measure of effect size, to quantify the difference between two groups and interpret its magnitude.

## Installation
To run this project, you will need to have Python installed along with the following libraries:

* pandas
* numpy
* matplotlib
* seaborn
* pingouin
* scipy.stats

## Data Source
The data used in this analysis originates from an experimental study by Prof. Brian Everitt.
The data set can be found in the Anorexia Data File at the web text: https://users.stat.ufl.edu/~aa/smss/data/Anorexia.dat

## References
* "Statistical Methods for the Social Sciences" (FIFTH EDITION) by Alan Agresti.
