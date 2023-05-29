# -*- coding: utf-8 -*-
"""Final practical DSBDA pr18

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LvsrQB8QsA3kK-gxfy9A-3PsJJtNUI-0
"""

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('Cleavland.csv')
data

columns=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num']
# -- 1. #3  (age)       
#       -- 2. #4  (sex)       
#       -- 3. #9  (cp)        
#       -- 4. #10 (trestbps)  
#       -- 5. #12 (chol)      
#       -- 6. #16 (fbs)       
#       -- 7. #19 (restecg)   
#       -- 8. #32 (thalach)   
#       -- 9. #38 (exang)     
#       -- 10. #40 (oldpeak)   
#       -- 11. #41 (slope)     
#       -- 12. #44 (ca)        
#       -- 13. #51 (thal)      
#       -- 14. #58 (num)

data.columns=columns
data

data.describe()

import matplotlib.pyplot as plt

# Plot a histogram of a numerical variable
plt.hist(data['age'])
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of AGE')
plt.show()

import seaborn as sns

# Plot a dot plot to compare a numerical variable across categories
# sns.stripplot(x='sex', y='num', data=data)  #x is categorical
sns.stripplot(x='sex',y='num',data=data)
plt.xlabel('sex')
plt.ylabel('num')
plt.title('Dot Plot of Numerical Variable by Category')
plt.show()

# Plot a bar plot of a categorical variable
sns.countplot(x='sex', data=data)
plt.xlabel('sex')
plt.ylabel('Frequency')
plt.title('Bar Plot of Categorical Variable')
plt.show()

# Plot a line chart of a numerical variable over time
plt.plot(data['age'], data['num'])
plt.xlabel('Time Variable')
plt.ylabel('Numerical Variable')
plt.title('Line Chart of Numerical Variable over Time')
plt.show()

# Plot a scatter plot to analyze the relationship between two numerical variables
plt.scatter(data['age'], data['chol'])
plt.xlabel('Numerical Variable 1')
plt.ylabel('Numerical Variable 2')
plt.title('Scatter Plot of Numerical Variables')
plt.show()

# Plot a pie chart to show the proportion of each category in a categorical variable
plt.pie(data['num'].value_counts(), labels=['less severe', 'severe', 'moderate', 'high', 'very high'], autopct='%1.1f%%')
plt.title('Pie Chart of Categorical Variable')
plt.axis('equal')
plt.show()

# Plot a box plot of a numerical variable
sns.boxplot(x='num', y='age', data=data)
plt.xlabel('Category Variable')
plt.ylabel('Numerical Variable')
plt.title('Box Plot of Numerical Variable by Category')
plt.show()

cp_counts = data['cp'].value_counts()
plt.bar(cp_counts.index, cp_counts.values)
plt.xlabel('Chest Pain Type')
plt.ylabel('Frequency')
plt.title('Distribution of Chest Pain Type')
plt.show()

# ct=data['cp'].unique().sum()
ct=data['cp'].value_counts()
print(ct.index)

