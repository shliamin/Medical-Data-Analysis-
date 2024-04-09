import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file into a DataFrame
data = pd.read_csv('Data/students.csv')

# Clean the data by removing any invalid values (if necessary)
data = data.dropna()

# Convert 'Do you have Depression?' column to numeric (replace 'Yes' with 1 and 'No' with 0)
data['Do you have Depression?'] = data['Do you have Depression?'].replace({'Yes': 1, 'No': 0})

# Group the data by age and calculate the absolute values of depression
depression_by_age = data.groupby('Age')['Do you have Depression?'].sum()

# Calculate the relative values of depression by age
total_depression = data['Do you have Depression?'].sum()
relative_depression_by_age = depression_by_age / total_depression

# Create a mask for students without depression
no_depression_mask = data['Do you have Depression?'] == 0

# Set the width of each bar
bar_width = 0.35

# Set the positions of the bars on the x-axis
age_labels = depression_by_age.index
bar_positions = range(len(age_labels))

# Visualize the absolute values of depression by age with side-by-side bars for students with and without depression
plt.figure(figsize=(10, 6))
plt.bar(bar_positions, depression_by_age.values, width=bar_width, color='blue', label='With Depression')
plt.bar([pos + bar_width for pos in bar_positions], depression_by_age.where(no_depression_mask).values, width=bar_width, color='green', label='No Depression')

# Customize the x-axis labels
plt.xticks([pos + bar_width/2 for pos in bar_positions], age_labels)

plt.xlabel('Age')
plt.ylabel('Absolute Depression Values')
plt.title('Absolute Depression Values by Age')
plt.legend()
plt.show()

# Visualize the relative values of depression by age
plt.figure(figsize=(10, 6))
plt.bar(relative_depression_by_age.index, relative_depression_by_age.values)
plt.xlabel('Age')
plt.ylabel('Relative Depression Values')
plt.title('Relative Depression Values by Age')
plt.show()
