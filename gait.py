import numpy as np
import matplotlib.pyplot as plt
import csv

time_values = []
x_values = []
y_values = []
z_values = []

# Get all the values
with open('gaitData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        time_values.append(round(float(row[0]), 4))
        x_values.append(round(float(row[1]), 4))
        y_values.append(round(float(row[2]), 4))
        z_values.append(round(float(row[3]), 4))

# Plot and show the x, y, z values
plt.plot(x_values, label='x')
plt.plot(y_values, label='y')
plt.plot(z_values, label='z')
plt.title('Raw Data – X')
plt.legend()
plt.show()

# Remove 15% of the data from the start and the end
threshold = len(x_values) * .15
new_x_values = x_values[int(threshold):-int(threshold)]
new_y_values = y_values[int(threshold):-int(threshold)]
new_z_values = z_values[int(threshold):-int(threshold)]
time_values = time_values[int(threshold):-int(threshold)]

# Plot and show the new Data
plt.figure()
plt.plot(new_x_values, label='x')
plt.plot(new_y_values, label='y')
plt.plot(new_z_values, label='z')
plt.show()

# Get the mean
x_val = (new_x_values - np.mean(new_x_values))
y_val = (new_y_values - np.mean(new_y_values))
z_val = (new_z_values - np.mean(new_z_values))


# Get the combined vector magnitude and then inteprolate the times with the magnitude vector
magnitude_vec2 = np.sqrt(x_val**2 + y_val**2 + z_val**2)
times = np.linspace(int(min(time_values)), int(max(time_values)),
                       (int(max(time_values)) - int(min(time_values))) * 5)
data = np.interp(times, time_values, magnitude_vec2)

# Plot and show the data
plt.figure()
plt.plot(times, data, label='Combined Magnitude')
plt.legend()
plt.show()

# Get the lenght of the array and also zero out the array
x = len(data)-3
new_data = np.zeros(x)
weights = [0.75, 0.15, 0.1]
for i in range(x):
    for j in weights:
        new_data[i] += j * data[i]


# Plot and show the enhanced data
plt.figure()
plt.title('Enhanced Data')
plt.plot(new_data)
plt.legend()
plt.show()

# Extract the histogram
plt.title('Features')
plt.hist(new_data)
plt.legend()
plt.show()