import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file into a DataFrame
data = pd.read_csv('Data/students.csv')

# Clean the data by removing any invalid values (if necessary)
data = data.dropna()

# Convert 'Do you have Panic_attack?' column to numeric (replace 'Yes' with 1 and 'No' with 0)
data['Do you have Panic attack?'] = data['Do you have Panic attack?'].replace({'Yes': 1, 'No': 0})

# Group the data by age and calculate the absolute values of Panic_attack
Panic_attack_by_age = data.groupby('Age')['Do you have Panic attack?'].sum()

# Calculate the relative values of Panic_attack by age
total_Panic_attack = data['Do you have Panic attack?'].sum()
relative_Panic_attack_by_age = Panic_attack_by_age / total_Panic_attack

# Create a mask for students without Panic_attack
no_Panic_attack_mask = data['Do you have Panic attack?'] == 0

# Set the width of each bar
bar_width = 0.35

# Set the positions of the bars on the x-axis
age_labels = Panic_attack_by_age.index
bar_positions = range(len(age_labels))

# Visualize the absolute values of Panic_attack by age with side-by-side bars for students with and without Panic_attack
plt.figure(figsize=(10, 6))
plt.bar(bar_positions, Panic_attack_by_age.values, width=bar_width, color='blue', label='With Panic_attack')
plt.bar([pos + bar_width for pos in bar_positions], Panic_attack_by_age.where(no_Panic_attack_mask).values, width=bar_width, color='green', label='No Panic_attack')

# Customize the x-axis labels
plt.xticks([pos + bar_width/2 for pos in bar_positions], age_labels)

plt.xlabel('Age')
plt.ylabel('Absolute Panic Attack Values')
plt.title('Absolute Panic Attack Values by Age')
plt.legend()
plt.show()

# Visualize the relative values of Panic_attack by age
plt.figure(figsize=(10, 6))
plt.bar(relative_Panic_attack_by_age.index, relative_Panic_attack_by_age.values)
plt.xlabel('Age')
plt.ylabel('Relative Panic Attack Values')
plt.title('Relative Panic Attack Values by Age')
plt.show()
