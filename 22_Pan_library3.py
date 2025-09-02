import pandas as pd

# Create a sample data
data = {
    'Name': ['Sualiah', 'Yuvraj', 'Sagil', 'Arjun', 'Kiran'],
    'Age': [21, 23, 22, 24, 23],
    'Marks': [89, 75, 61, 92, 85],
    'City': ['Moradabad', 'Delhi', 'Delhi', 'Noida', 'Delhi']
}
df = pd.DataFrame(data)    # Print original data
print(df)

print("\nSort by Marks:\n", df.sort_values(by='Marks', ascending=False))    # Sorting the data a/c to marks

print("\nStudents with Marks > 80:\n", df[df['Marks'] > 80])         # Filtering rows

print("\nGroup by City (Average Marks):\n", df.groupby('City')['Marks'].mean())   # Grouping 

df['Result'] = ['Pass' if m >= 60 else 'Fail' for m in df['Marks']]  # Adding new column result
print("\nWith Result Column:\n", df)

print("\nAfter Dropping Age Column:\n", df.drop(columns=['Age']))   # Remove column

print("\nRename Columns:\n", df.rename(columns={'Marks': 'Scores'}))  # Rename columns
 
print("\nCity Counts:\n", df['City'].value_counts())    # Value counts

print("\nUnique Cities:\n", df['City'].unique())    # Unique values


