### INF601 - Advanced Programming in Python
### Kadin Heacock
### Miniproject1

# imports
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Saves the graphs to the Charts file
if not os.path.exists("Charts"):
    os.mkdir("Charts")

# Reading the .csv file
data = pd.read_csv( filepath_or_buffer= 'WLD_RTP_details_2023-10-02.csv', index_col=0, parse_dates=True)

country = ["june"]

df = pd.DataFrame(data)

def col():
# Used to grab the 2 columns needed for the graph
    for col in df.columns:
        series = df[col]


    # Graphically display the country's and there inflation percentage in 2023
if len(country) == 1:
    # Example: Plot the first numeric column against the index
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data.iloc[:, 0], label=data.columns[0])  # Plotting the first numeric column
    plt.title('Time Series Plot of ' + data.columns[0])
    plt.xlabel('Date')
    plt.ylabel(data.columns[0])
    plt.legend()
    plt.grid()
    plt.tight_layout()
  #  row.plot(title=f'Row {index}', xlabel='Column Index', ylabel='Value')
    plt.savefig(f'Charts\\{country}.png')
    plt.show()
else:
    print("No numeric data available for plotting.")