import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(16, 9))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    slope = result.slope
    intercept = result.intercept
    start_year = df["Year"].min()
    end_year = 2051
    best_fit_data = {
        "year": [],
        "predicted_sea_level": []
    }

    for year in range(start_year, end_year):
        best_fit_data["year"] = [year for year in range(start_year, end_year)]
        best_fit_data["predicted_sea_level"] = [slope * year + intercept for year in range(start_year, end_year)]
    
    plt.plot(best_fit_data["year"], best_fit_data["predicted_sea_level"], 'r')
    
    # Plot a horizontal line crossing prediction for year 2050
    """ind = best_fit_data["year"].index(2050)
        y = best_fit_data["predicted_sea_level"][ind]
        plt.axhline(y=y, xmin=0, xmax=1, color='r', linestyle='--', linewidth=1)
    """
    
    # Create second line of best fit
    start_year = 2000
    end_year = 2051
    df_recent = df.loc[df["Year"] >= start_year]

    result = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    slope = result.slope
    intercept = result.intercept

    for year in range(start_year, end_year):
        best_fit_data["year"] = [year for year in range(start_year, end_year)]
        best_fit_data["predicted_sea_level"] = [slope * year + intercept for year in range(start_year, end_year)]

    plt.plot(best_fit_data["year"], best_fit_data["predicted_sea_level"], 'g')

    # Plot a horizontal line crossing prediction for year 2050
    """ind = best_fit_data["year"].index(2050)
        y = best_fit_data["predicted_sea_level"][ind]
        plt.axhline(y=y, xmin=0, xmax=1, color='g', linestyle='--', linewidth=1)
    """

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    
    # Plot a vertical line for the year 2000
    plt.axvline(x=2000, ymin=0.025, ymax=.975, color='grey', linestyle=':', linewidth=1)
    #plt.text(0.69, .9, 'Year = 2000', rotation=0, transform=ax.transAxes)
    
    # Plot a vertical line for the year 2050
    # plt.axvline(x=2050, ymin=0, ymax=1, color='r', linestyle=':', linewidth=1)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()