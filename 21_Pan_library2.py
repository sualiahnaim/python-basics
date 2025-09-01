# Pandas DataFrame : Dataframe is a 2 dimensional data structure

# Creating a dataframe
import pandas as pd
d1=pd.DataFrame({'Name':('sualiah','yuvraj','sagil'),'Marks':(89,75,61)})
print(d1)

# How to read a dataset 
iris=pd.read_csv('iris.CSV')
print(iris.head())   # for upper five records
print(iris.tail())   # for lower five records
print(iris.shape)    # counting a rows and coloumns
print(iris.describe()) # Basic knowledge for data  
print(iris.info())

# Basic Maths & Statistics operations
print(iris['sepal_length'].mean())
print(iris['sepal_length'].median())
print(iris['sepal_length'].mode())
print(iris['petal_length'].max())
print(iris['petal_length'].min())
print(iris['petal_length'].std())
print(iris['sepal_length'].var())

# For data selection
print(iris['species'].unique())
print(iris['species'].count())
print(iris.iloc[0:5])



