### INF601 - Advanced Programming in Python
### Kadin Heacock
### Miniproject1

# imports
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import pprint

if not os.path.exists("Charts"):
    os.mkdir("Charts")

# Reading the .csv file
data = pd.read_csv( filepath_or_buffer= 'WLD_RTP_details_2023-10-02.csv', index_col=0, parse_dates=True)

df = pd.DataFrame(data)

for col in df.columns:
    series = df[col]

    print(series)



    # numpy to give the number of country's
    a = np.array(countrys)

    if len(countrys) == 26:
        # Example: Plot the first numeric column against the index
        plt.figure(figsize=(10, 6))
        plt.plot(data.index, data.iloc[:, 0], label=data.columns[0])  # Plotting the first numeric column
        plt.title('Time Series Plot of ' + data.columns[0])
        plt.xlabel('Date')
        plt.ylabel(data.columns[0])
        plt.legend()
        plt.grid()
        plt.tight_layout()
        row.plot(title=f'Row {index}', xlabel='Column Index', ylabel='Value')
        plt.savefig(f'Charts\\{food_inflation}.png')
        plt.show()
    else:
        print("No numeric data available for plotting.")