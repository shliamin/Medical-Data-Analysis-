import pandas as pd
from scipy import stats

# Load the data from a CSV file
data = pd.read_csv('Data/students.csv')

# Preprocess the CGPA column to extract numeric values
data['CGPA'] = data['What is your CGPA?'].str.extract(r'([\d.]+)').astype(float)

# Creating two groups: students with depression and students without depression
students_with_depression = data[data['Do you have Depression?'] == 'Yes']
students_without_depression = data[data['Do you have Depression?'] == 'No']

# Calculating the mean grades for each group
mean_grades_with_depression = students_with_depression['CGPA'].mean()
mean_grades_without_depression = students_without_depression['CGPA'].mean()

# Conducting the statistical test
t_statistic, p_value = stats.ttest_ind(students_with_depression['CGPA'], students_without_depression['CGPA'])

# Outputting the results
print("Mean grade for students with depression:", mean_grades_with_depression)
print("Mean grade for students without depression:", mean_grades_without_depression)
print("Statistical test: t =", t_statistic, ", p =", p_value)
