import matplotlib.pyplot as plt
import pandas as pd

# Load the data from a CSV file
data = pd.read_csv('Data/students.csv')

# Creating mapping
mapping = {"year 1": 1,
           "Year 1": 1,
           "YEAR 1": 1,
           "year 2": 2,
           "Year 2": 2,
           "YEAR 2": 2,
           "year 3": 3,
           "Year 3": 3,
           "YEAR 3": 3,
           "year 4": 4,
           "Year 4": 4,
           "YEAR 4": 4}

# Formating using mapping>
data['Your current year of Study'] = data['Your current year of Study'].map(mapping)

# Group the data by age and calculate the average years of study
mean_years_of_study = data.groupby('Age')['Your current year of Study'].mean()

# Create a bar plot
mean_years_of_study.plot(kind='bar')

# Set the labels and title
plt.xlabel('Age Groups')
plt.ylabel('Average Years of Study')
plt.title('Average Years of Study by Age Groups')

# Display the plot
plt.show()
