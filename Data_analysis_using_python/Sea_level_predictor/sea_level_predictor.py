import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    # plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    linear_regression_one = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_axis_A = range(1880, 2051)
    y_axis_A = x_axis_A * linear_regression_one.slope + linear_regression_one.intercept
    plt.plot(x_axis_A, y_axis_A)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    linear_regression_two = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_axis_B = range(2000, 2051)
    y_axis_B = x_axis_B * linear_regression_two.slope + linear_regression_two.intercept

    # Add labels and title
    plt.figure(figsize = (10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(x_axis_A, y_axis_A)
    plt.plot(x_axis_B, y_axis_B)
    plt.xlabel('Year')
    plt.xticks(range(1850, 2076, 25))
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
