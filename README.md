
# Student Mental Health Analysis

This project analyzes the mental health data of students and visualizes the results using Python. The analysis includes data on anxiety, depression, and panic attacks, along with their relation to age and years of study.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have Python 3.x installed.
- You have `pip` installed.

## Installation

To install the required libraries, run the following commands:

```sh
pip install pandas matplotlib scipy notebook
```

## Setting Up the Project

1. **Clone the repository:**
   
   If the project is hosted on a version control system like GitHub, you can clone the repository. Otherwise, download the project files.

   ```sh
   git clone https://github.com/shliamin/Python-Medical-Data-Analysis.git
   ```

2. **Navigate to the project directory:**

   ```sh
   cd Python-Medical-Data-Analysis
   ```

3. **Ensure the `students.csv` file is in the project directory.**

## Running the Jupyter Notebook

1. **Start Jupyter Notebook:**

   Run the following command to start Jupyter Notebook:

   ```sh
   jupyter notebook
   ```

2. **Open the notebook:**

   In the Jupyter Notebook interface, navigate to and open the `Student Mental Health Analysis.ipynb` file.

3. **Run the notebook:**

   Execute each cell in the notebook sequentially to perform the analysis and generate the visualizations.

## Notebook Contents

The notebook contains the following sections:

1. **Import necessary libraries:** Import `pandas`, `matplotlib.pyplot`, and `scipy.stats`.
2. **Load data:** Load data from the `students.csv` file into a DataFrame and display column names.
3. **Data preparation:** Convert relevant columns to numeric and clean the 'Your current year of Study' column.
4. **Anxiety Analysis:** Analyze and visualize anxiety data by age.
5. **Depression Analysis:** Analyze and visualize depression data by age.
6. **Panic Attack Analysis:** Analyze and visualize panic attack data by age.
7. **Age vs. Year of Study Analysis:** Analyze and visualize the relationship between age and year of study.
8. **T-Test Analysis:** Perform a t-test between students with and without anxiety for years of study.

## Example Output

Below are examples of the visualizations and analysis you will generate:

- Absolute and relative values of anxiety, depression, and panic attacks by age.
- Relationship between age and year of study.
- Results of the t-test between students with and without anxiety.

