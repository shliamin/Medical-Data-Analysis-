import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file into a DataFrame
data = pd.read_csv('Data/students.csv')

# Clean the data by removing any invalid values (if necessary)
data = data.dropna()

# Convert 'Do you have anxiety?' column to numeric (replace 'Yes' with 1 and 'No' with 0)
data['Do you have Anxiety?'] = data['Do you have Anxiety?'].replace({'Yes': 1, 'No': 0})

# Group the data by age and calculate the absolute values of anxiety
anxiety_by_age = data.groupby('Age')['Do you have Anxiety?'].sum()

# Calculate the relative values of anxiety by age
total_anxiety = data['Do you have Anxiety?'].sum()
relative_anxiety_by_age = anxiety_by_age / total_anxiety

# Create a mask for students without anxiety
no_anxiety_mask = data['Do you have Anxiety?'] == 0

# Set the width of each bar
bar_width = 0.35

# Set the positions of the bars on the x-axis
age_labels = anxiety_by_age.index
bar_positions = range(len(age_labels))

# Visualize the absolute values of anxiety by age with side-by-side bars for students with and without anxiety
plt.figure(figsize=(10, 6))
plt.bar(bar_positions, anxiety_by_age.values, width=bar_width, color='blue', label='With Anxiety')
plt.bar([pos + bar_width for pos in bar_positions], anxiety_by_age.where(no_anxiety_mask).values, width=bar_width, color='green', label='No Anxiety')

# Customize the x-axis labels
plt.xticks([pos + bar_width/2 for pos in bar_positions], age_labels)

plt.xlabel('Age')
plt.ylabel('Absolute Anxiety Values')
plt.title('Absolute Anxiety Values by Age')
plt.legend()
plt.show()

# Visualize the relative values of anxiety by age
plt.figure(figsize=(10, 6))
plt.bar(relative_anxiety_by_age.index, relative_anxiety_by_age.values)
plt.xlabel('Age')
plt.ylabel('Relative Anxiety Values')
plt.title('Relative Anxiety Values by Age')
plt.show()
