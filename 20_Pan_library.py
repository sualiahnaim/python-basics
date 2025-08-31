# Pandas Library : Pandas stands for panel data and is the core library for data manipulation and data analysis. 
# It consists of single and multi-dimensional data structures for data manipulation.

import pandas as pd
s1=pd.Series([1,2,3,4,5])  # Pandas series object
print(s1)

# Series object from Dictionary
s2=pd.Series({'K1':10,'K2':20,'K3':30})
print(s2)

s3=pd.Series({'x1':20,'x2':80,'x3':70}, index=['x3','x1','x4','x2'])   # Changing Index position
print(s3)

# Extracting Individual Elements
l1=[1,2,3,4,5,6,7,8,9]
s4=pd.Series(l1)
print(s4[4])    # extracting index 4 element
print(s4[:5])   # print starting five elemets
print(s4[-5:])  # Print last five elements

# Basic Math operations on Series
s5=s4+10     # Addition
print(s5)
s6=s4-1      # Subtract
print(s6)
s7=s4*2      # Multiply
print(s7)
s8=s4/2      # Divide
print(s8)

# Add Two Series objects 
s9=pd.Series([1,2,3,4,5])
s10=pd.Series([10,20,30,40,50])
s11=s9+s10       # Concatination
print(s11)
