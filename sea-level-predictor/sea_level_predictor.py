import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.figure(figsize=(20, 7))
    plt.scatter(x, y)
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    # Predict the sea level rise in the year 2050
    x1 = pd.Series([x for x in range(1880, 2051, 1)])

    # Add the line of best fit to the scatter plot
    plt.plot(x1, slope * x1 + intercept)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    x2 = x1[x1 >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    y2 = slope * x2 + intercept
    plt.plot(x2, y2)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()