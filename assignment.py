#!/usr/bin/env python
# coding: utf-8

# In[29]:


pip install pandas

Q1: How many rows and columns are there in books.csv dataset?
# In[26]:


import pandas as pd

# Loading the file
ex = pd.read_csv('Downloads/books.csv')
#Finding number of rows & columns
num_r, num_c = ex.shape

print(f'Number of rows: {num_r}')
print(f'Number of columns: {num_c}')

Q2: How many books do not have an original title?
# In[14]:


import pandas as pd

# Loading the file
ex = pd.read_csv('Downloads/books.csv')

books_without_original_title = ex['original_title'].isnull().sum()

print(f'Number of books without an original title: {books_without_original_title}')

Q3: How many unique books are present in the dataset ? Evaluate based on the 'book_id' after removing null values in the original_title column.
# In[27]:


import pandas as pd

# Loading the file
ex = pd.read_csv('Downloads/books.csv')

# Drop rows where 'original_title' is null
ex_cleaned = ex.dropna(subset=['original_title'])

# Count the number of unique books based on 'book_id'
unique_books_count = ex_cleaned['book_id'].nunique()

print(f'Number of unique books : {unique_books_count}')

Q4: What is the average rating of all the books in the dataset based on ‘average_rating’?
# In[28]:


import pandas as pd

# Loading the file
ex = pd.read_csv('Downloads/books.csv')

# Calculating the average rating based on 'average_rating'
average_rating = ex['average_rating'].mean()

print(f'Average rating of all books: {average_rating:.2f}')

Q5: Find the number of books published in the year ‘2000’ based on the ‘original_publication_year’.
# In[35]:


import pandas as pd

# Loading the file
ex = pd.read_csv('Downloads/books.csv')

# Filter rows where 'original_publication_year' is '2000'
books_2000 = ex[ex['original_publication_year'] == 2000]

# Getting the count of books published in 2000
num_books = books_2000.shape[0]

print(f'Number of books published in the year 2000: {num_books}')

Q6: Which book (title) has the maximum number of ratings based on ‘work_ratings_count’?
# In[36]:


import pandas as pd

# Loading the file
ex = pd.read_csv('Downloads/books.csv')

# Find the book with the maximum number of ratings
max_ratings = ex[ex['work_ratings_count'] == ex['work_ratings_count'].max()]

# Getting the book with the maximum number of ratings
max_ratings_title = max_ratings['title'].values[0]

print(f'The book with the maximum number of ratings is: {max_ratings_title}')

Q7)Bucket the average_rating of books into 11 buckets [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0] with 0.5 decimal rounding (eg: average_rating 3.0 to 3.49 will fall in bucket 3.0).Plot bar graph to show total number of books in each rating bucket.
# In[39]:


import pandas as pd
import matplotlib.pyplot as plt

# Loading the file
ex = pd.read_csv('Downloads/books.csv')

bins = [0,  0.5,  1.0,  1.5,  2.0,  2.5,  3.0,  3.5,  4.0,  4.5,  5.0]

# Creating0 a new column 'rating_bucket' based on the average_rating
ex['rating_bucket'] = pd.cut(ex['average_rating'], bins, include_lowest=True, right=False)

# Counting the number of books in each rating bucket
rating_counts = ex['rating_bucket'].value_counts().sort_index()

# Plotting the graph
plt.bar(rating_counts.index.astype(str), rating_counts)
plt.xlabel('Rating Bucket')
plt.ylabel('Number of Books')
plt.title('Number of Books in Each Rating Bucket')
plt.xticks(rotation=25)
plt.show()


# In[ ]:




