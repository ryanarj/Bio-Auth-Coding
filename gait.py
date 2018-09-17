import pandas as pd
import matplotlib.pyplot as plt
import csv

time_values = []
x_values = []
y_values = []
z_values = []

with open('gaitData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        time_values.append(round(float(row[0]), 4))
        x_values.append(round(float(row[1]), 4))
        y_values.append(round(float(row[2]), 4))
        z_values.append(round(float(row[3]), 4))

plt.plot(x_values)
plt.xlabel('X')
plt.title('Raw Data – X')
plt.show()