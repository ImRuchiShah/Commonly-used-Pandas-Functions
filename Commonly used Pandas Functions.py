#!/usr/bin/env python
# coding: utf-8

# ### Commonly used Pandas Functions:
# 
# Pandas is one of the most widely used libraries in the data science community and it’s a powerful tool that can help you with data manipulation, cleaning, and analysis.
# 
# - pd.read_csv()
# - df.describe()
# - df.info()
# - df.plot()
# - df.iloc()
# - df.loc()
# - df.assign()
# - df.query()
# - df.sort_values()
# - df.sample()
# - df.isnull()
# - df.fillna()
# - df.dropna()
# - df.drop()
# - pd.pivot_table()
# - df.groupby()
# - df.transpose()
# - df.merge()
# - df.rename()
# - df.to_csv()
# 

# ### pd.read_csv()

# In[1]:


import pandas as pd


# In[4]:


df = pd.read_csv('C:/Users/RUCHITA/Documents/Downloads/baby_names.csv')
df.head()


# ### df.describe()

# In[5]:


print(df.describe())


# In[6]:


df.describe(include='all') 


# In[7]:


df.describe(exclude='number') # exclude numerical columns


# ### df.info()
# 
# df.info() is a method in pandas that is used to get a concise summary of the DataFrame, including the number of non-null values in each column, the data types of each column, and the memory usage of the DataFrame.

# In[8]:


print(df.info())


# ### df.plot()

# In[11]:


df['gndr'].value_counts().plot(kind='bar')


# ### df.iloc()
# Pandas’ .iloc() function is used to select rows and columns by their integer-based index in a DataFrame. It is used to select rows and columns by their integer-based location.

# In[12]:


# Select the first row
print(df.iloc[0])


# In[13]:


# Select the first two rows
print(df.iloc[:2])


# In[14]:


# Select the first column
print(df.iloc[:, 0])


# In[15]:


# Select the first two columns
print(df.iloc[:, :2])


# In[16]:


# Select the (1, 1) element
print(df.iloc[1, 1])


# ### df.loc()
# Pandas’ .loc() function is used to select rows and columns by their label-based index in a DataFrame. It is used to select rows and columns by their label-based location.

# In[18]:


# Select the column name 'Gender'
print(df.loc[:,'gndr'])


# In[22]:


# Select the columns named 'Year of Birth' and 'Gender'
print(df.loc[:, ['brth_yr', 'gndr']])


# ### df.assign()
# Pandas’ .assign() function is used to add new columns to a DataFrame, based on the computation of existing columns. It allows you to add new columns to a DataFrame without modifying the original dataframe. The function returns a new DataFrame with the added columns.

# In[25]:


df_new = df.assign(count_plus_5=df['cnt'] + 5)
df_new.head()


# ### df.query()
# Pandas’ .query() function allows you to filter a DataFrame based on a Boolean expression. It allows you to select rows from a DataFrame using a query string similar to SQL. The function returns a new DataFrame containing only the rows that satisfy the Boolean expression.

# In[27]:


# Select rows where age is greater than 30 and income is less than 65000
df_query = df.query('cnt > 30 and rnk < 20')
df_query.head()


# In[28]:


# Select rows where gender is Male
df_query = df.query("gndr == 'MALE'")
df_query.head()


# ### df.sort_values()
# Pandas’ .sort_values() function allows you to sort a DataFrame by one or multiple columns. It sorts the DataFrame based on the values of one or more columns, in ascending or descending order. The function returns a new DataFrame sorted by the specified column(s).

# In[29]:


# Sort by age in ascending order
df_sorted = df.sort_values(by='cnt')
df_sorted.head()


# In[30]:


# Sort by income in descending order
df_sorted = df.sort_values(by='rnk', ascending=False)
df_sorted.head()


# In[31]:


# Sort by multiple columns
df_sorted = df.sort_values(by=['cnt', 'rnk'])
df_sorted.head()


# ### df.sample()
# Pandas’ .sample() function allows you to randomly select rows from a DataFrame. It returns a new DataFrame containing the randomly selected rows. The function takes several parameters that allow you to control the sampling process, such as the number of rows to return, and whether or not to sample with replacement and seed for reproducibility.

# In[32]:


# Sample 2 rows without replacement
df_sample = df.sample(n=2, replace=False, random_state=1)
df_sample


# In[33]:


# Sample 3 rows with replacement
df_sample = df.sample(n=3, replace=True, random_state=1)
df_sample


# In[34]:


# Sample 2 rows without replacement with specific column to be chosen
df_sample = df.sample(n=2, replace=False, random_state=1, axis=1)
df_sample


# ### df.isnull()

# In[35]:


df.isnull()


# ### df.fillna()

# In[36]:


# fill missing values with 0
df.fillna(0)

# forward-fill missing values (propagates last valid observation forward to next)
df.fillna(method='ffill')

# backward-fill missing values (propagates next valid observation backward to last)
df.fillna(method='bfill')

# fill missing values using interpolation
df.interpolate()


# In[37]:


# fill missing values in place
df.fillna(0, inplace=True)


# ### df.dropna()

# In[41]:


# You can remove all rows containing at least one missing value by calling df.dropna().
df = df.dropna()


# In[42]:


# If you want to remove only the columns that contain at least one missing value you can use df.dropna(axis=1)
df = df.dropna(axis=1)


# In[43]:


# You can also set thresh parameter to keep only the rows/columns that have at least thresh non-NA/null values.
df = df.dropna(thresh=2)


# ### df.drop()
# df.drop() is a method used in the Pandas library to remove rows or columns from a DataFrame by specifying the corresponding labels. It can be used to drop one or multiple rows or columns based on their labels.
# 
# You can remove a specific row by calling df.drop() and passing the index label of the row you want to remove, and the axis parameter set to 0 (default is 0)

# In[44]:


# remove the first row of the DataFrame.
df_drop = df.drop(0)


# In[45]:


# drop multiple rows by passing a list of index labels
df_drop = df.drop([0,1])


# In[47]:


# drop columns by passing the labels of the columns you want to remove and setting the axis parameter to 1:

df_drop = df.drop(['cnt', 'rnk'], axis=1)


# ### pd.pivot_table()
# 
# pd.pivot_table() is a method in the Pandas library that is used to create a pivot table from a DataFrame. A pivot table is a table that summarizes and aggregates data in a more meaningful and organized way, by creating a new table with one or more columns as the index, one or more columns as values, and one or more columns as attributes.

# In[50]:


pivot_table = pd.pivot_table(df, index='ethcty', values='cnt', aggfunc='sum')
pivot_table.head()


# In[53]:


pivot_table = pd.pivot_table(df, index=['ethcty','gndr'], values= 'cnt' , aggfunc=['sum','count'])
pivot_table.head(20)


# ### df.groupby()
# 
# df.groupby() is a method in the Pandas library that is used to group rows of a DataFrame based on one or multiple columns. This allows you to perform aggregate operations on the groups, such as calculating the mean, sum, or count of the values in each group.
# 
# df.groupby() returns a GroupBy object, which you can then use to perform various operations on the groups, such as calculating the sum, mean, or count of the values in each group.

# In[54]:


grouped = df.groupby('gndr')
# Print the mean of each group
print(grouped.mean())


# In[55]:


grouped = df.groupby(['gndr', 'ethcty'])

# Print the sum of each group
print(grouped.sum())


# ### df.transpose()

# In[56]:


# Transpose the DataFrame
df_transposed = df.transpose()

# Print the transposed DataFrame
df_transposed.head()


# In[57]:


# It can also be done using T attributes on the dataframe. df.T will do the same as df.transpose().

df_transposed = df.T
df_transposed.head()


# ### df.merge()

# In[58]:


# Create the first DataFrame
df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                   'value': [1, 2, 3, 4]})

# Create the second DataFrame
df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'],
                   'value': [5, 6, 7, 8]})

# Merge the two DataFrames on the 'key' column
merged_df = df1.merge(df2, on='key')

# Print the merged DataFrame
print(merged_df)


# #You can also merge multiple columns by passing a list of columns to the on parameter.
# 
# merged_df = df1.merge(df2, on=['key1','key2'])
# 
# #You can also specify a different column name to merge by using left_on and right_on parameters.
# 
# merged_df = df1.merge(df2, left_on='key1', right_on='key3')

# ### df.rename()

# In[60]:


# Rename column 'Count' to 'count'
df_rename = df.rename(columns={'cnt': 'count'})
df_rename.head()


# In[61]:


#You can also use a dictionary to rename multiple columns at once:

df_rename = df.rename(columns={'count': 'Count', 'rnk':'rank'})
df_rename.head()


# In[63]:


#You can also rename the index similarly:

df_rename = df.rename(index={0:'first',1:'second',2:'third'})
df_rename.head()


# ### df.to_csv()
# 
# df.to_csv() is a method used in the Pandas library to export a DataFrame to a CSV file. CSV stands for "Comma Separated Values" and it is a popular file format for storing data in a tabular form.
# 
# For example, let’s say we want to save df that you want to export to a CSV file. You can export the DataFrame to a CSV file by calling df.to_csv() and passing the file name as a string:
# 
# 

# In[64]:


df.to_csv('data.csv')


# This will save the DataFrame to a file named data.csv in the current working directory. You can also specify the path of the file by passing it to the method:
# 
# #### df.to_csv('path/to/data.csv')
# 
# You can also specify the separator used in the CSV file by passing the sep parameter. By default, it’s set to “,”.
# 
# #### df.to_csv('path/to/data.csv', sep='\t')
# 
# It is also possible to only save specific columns of the DataFrame by passing the list of column names to the columns parameter, and also to save only specific rows by passing a boolean mask to the index parameter.
# 
# #### df.to_csv('path/to/data.csv', columns=['Rank','Count'])
# You can also use the index parameter to specify whether to include or exclude the index of the dataframe in the exported CSV file.
# 
# #### df.to_csv('path/to/data.csv', index=False)
# This will exclude the index of the dataframe in the exported CSV file.
# 
# You can also use na_rep parameter to replace missing values in the exported CSV file with a specific value.
# 
# #### df.to_csv('path/to/data.csv', na_rep='NULL')

# In[ ]:




