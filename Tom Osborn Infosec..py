import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Prepare the data with consistent lengths
data = {
    'Bank': ['Bank 2', 'Bank 3', 'Bank 4', 'Bank 5', 'Bank 9', 'Bank 10', 
             'Bank 11', 'Bank 12', 'Bank 13', 'Bank 14', 'Bank 15', 
             'Bank 16', 'Bank 17', 'Bank 19', 'Bank 20'],
    'In-Business Risk Team': ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 
                              'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 
                              'Yes', 'Yes', 'No'],
    'Team Size': [10, 20, 50, None, 5, 10, 10, 100, None, None, 
                  40, None, 20, None, None],
    'Headcount Change': ['No', 'Yes', 'No', 'No', 'Yes', 'Yes', 
                         'No', 'Yes', 'No', 'No', 'Yes', 
                         'No', 'No', 'No', 'No'],
    'Confidence Level': [3, 4, 2, 3, 5, 4, 3, 4, 4, 3, 
                         4, 3, 5, 4, 4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Check the lengths of each column
print("Lengths of each column:")
for key in data.keys():
    print(f"{key}: {len(data[key])}")

# Convert Team Size to numeric and drop NaN values
df['Team Size'] = pd.to_numeric(df['Team Size'], errors='coerce')

# Analyze the presence of an in-business risk team
risk_team_presence = df['In-Business Risk Team'].value_counts(normalize=True) * 100

# Plotting In-Business Risk Team Presence
plt.figure(figsize=(8, 5))
sns.barplot(x=risk_team_presence.index, y=risk_team_presence.values, palette='viridis')
plt.title('In-Business Risk Team Presence (%)')
plt.xlabel('In-Business Risk Team')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Analyze Team Sizes
team_sizes = df['Team Size'].dropna().value_counts(normalize=True) * 100

# Plotting Team Sizes
plt.figure(figsize=(8, 5))
sns.barplot(x=team_sizes.index.astype(str), y=team_sizes.values, palette='magma')
plt.title('Reported Sizes of In-Business Risk Teams (%)')
plt.xlabel('Team Size (Nearest 10)')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Analyze Headcount Changes
headcount_changes = df['Headcount Change'].value_counts(normalize=True) * 100

# Plotting Headcount Changes
plt.figure(figsize=(8, 5))
sns.barplot(x=headcount_changes.index, y=headcount_changes.values, palette='coolwarm')
plt.title('Headcount Changes Over the Past Year (%)')
plt.xlabel('Headcount Change')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Analyze Confidence Levels
plt.figure(figsize=(8, 5))
sns.histplot(df['Confidence Level'], bins=5, kde=True, color='blue')
plt.title('Confidence Levels in Risk Management Framework')
plt.xlabel('Confidence Level (1-5)')
plt.ylabel('Frequency')
plt.xticks(ticks=[1, 2, 3, 4, 5])
plt.tight_layout()
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:14:10 2024

@author: ke225
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Specify the file path
file_path = r'C:\Users\ke225\Downloads\Karim Test.xlsx'

try:
    # Load the entire Excel file without specifying header
    df = pd.read_excel(file_path, header=None)  # Load without a specific header

    # Display the first few rows of the DataFrame to inspect the content
    print("DataFrame Loaded Successfully!")
    
    # Display the first few rows and column names
    print(df.head())  # Show first few rows to inspect the content
    print("\nColumn Names:")
    print(df.columns)  # Display column names to check for the expected name

    # Show the DataFrame's info to understand its structure
    print("\nDataFrame Info:")
    print(df.info())

    # Check for the number of rows and columns in the DataFrame
    print("\nShape of DataFrame:", df.shape)

except FileNotFoundError:
    print("The specified file was not found. Please check the file path.")
except ValueError as ve:
    print("An error occurred with the Excel file:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)

# Analyze Cyber Risk Management Data
def analyze_cyber_risk_management(data):
    """
    Analyze the cyber risk management data from banks and display key trends and insights.
    
    Parameters:
    data: DataFrame containing the responses from banks about their cyber risk management.
    """
    insights = []

    # Check for actual column name for In-Business Risk Team
    if 'In-Business Risk Team' in data.columns:
        risk_team_presence = data['In-Business Risk Team'].value_counts(normalize=True) * 100
        insights.append(f"\nIn-Business Risk Team Presence:\n{risk_team_presence.to_string()}")

        # Plotting In-Business Risk Team Presence
        plt.figure(figsize=(10, 6))
        sns.barplot(x=risk_team_presence.index, y=risk_team_presence.values, palette='viridis')
        plt.title('In-Business Risk Team Presence (%)')
        plt.xlabel('In-Business Risk Team Presence')
        plt.ylabel('Percentage (%)')
        plt.xticks(rotation=45)
        plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
        plt.show()
    else:
        print("sheet 1.")

    # Display all insights
    print("\n".join(insights))
# Print the columns in the DataFrame
print(df.columns)
import pandas as pd

# Define the column names
column_names = [
    'Bank', 'In-Business Risk Team', 'Team Size', 
    'Headcount Change', 'Confidence Level'
]

# Create DataFrame with the specified column names
data = {
    'Bank': ['Bank 2', 'Bank 3', 'Bank 4', 'Bank 5', 'Bank 9', 'Bank 10', 
             'Bank 11', 'Bank 12', 'Bank 13', 'Bank 14', 'Bank 15', 
             'Bank 16', 'Bank 17', 'Bank 19', 'Bank 20'],
    'In-Business Risk Team': ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 
                              'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 
                              'Yes', 'Yes', 'No'],
    'Team Size': [10, 20, 50, None, 5, 10, 10, 100, None, None, 
                  40, None, 20, None, None],
    'Headcount Change': ['No', 'Yes', 'No', 'No', 'Yes', 'Yes', 
                         'No', 'Yes', 'No', 'No', 'Yes', 
                         'No', 'No', 'No', 'No'],
    'Confidence Level': [3, 4, 2, 3, 5, 4, 3, 4, 4, 3, 
                         4, 3, 5, 4, 4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Assign the column names
df.columns = column_names

# Display the DataFrame
print(df.head())
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure the 'Team Size' is numeric and handle NaN values
df['Team Size'] = pd.to_numeric(df['Team Size'], errors='coerce')

# Analyze the presence of an in-business risk team
risk_team_presence = df['In-Business Risk Team'].value_counts(normalize=True) * 100

# Plotting In-Business Risk Team Presence
plt.figure(figsize=(8, 5))
sns.barplot(x=risk_team_presence.index, y=risk_team_presence.values, palette='viridis')
plt.title('In-Business Risk Team Presence (%)')
plt.xlabel('In-Business Risk Team')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Analyze Team Sizes
team_sizes = df['Team Size'].dropna().value_counts(normalize=True) * 100

# Plotting Team Sizes
plt.figure(figsize=(8, 5))
sns.barplot(x=team_sizes.index.astype(str), y=team_sizes.values, palette='magma')
plt.title('Reported Sizes of In-Business Risk Teams (%)')
plt.xlabel('Team Size (Nearest 10)')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Analyze Headcount Changes
headcount_changes = df['Headcount Change'].value_counts(normalize=True) * 100

# Plotting Headcount Changes
plt.figure(figsize=(8, 5))
sns.barplot(x=headcount_changes.index, y=headcount_changes.values, palette='coolwarm')
plt.title('Headcount Changes Over the Past Year (%)')
plt.xlabel('Headcount Change')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Analyze Confidence Levels
plt.figure(figsize=(8, 5))
sns.histplot(df['Confidence Level'], bins=5, kde=True, color='blue')
plt.title('Confidence Levels in Risk Management Framework')
plt.xlabel('Confidence Level (1-5)')
plt.ylabel('Frequency')
plt.xticks(ticks=[1, 2, 3, 4, 5])
plt.tight_layout()
plt.show()
