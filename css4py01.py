# -*- coding: utf-8 -*-
"""
Spyder Editor

Project1.
"""

import pandas as pd

df = pd.read_csv ("movie_dataset.csv")
print (df)
print (df.describe())

# remove all rows with N/A
df2 = df.dropna()
print(df2)
print (df2.describe())

# calculate the mean of revenue
df2 ['Revenue (Millions)'].mean()

# sort by years
df3 = df2.sort_values(by= 'Year')

print(df3)

# data for years after 2014(2015-2017)

df4 = df3.loc[df3["Year" ]> 2014]


print(df4)

#calculate revenue after 2014

df4 ['Revenue (Millions)'].mean()



#number of movies in 2016 using original csv (df)

movies_2016 = df.loc[df["Year" ] == 2016]

print (movies_2016.describe())

""" 
            Rank    Year  ...  Revenue (Millions)   Metascore
count   297.000000   297.0  ...          205.000000  268.000000
mean    376.444444  2016.0  ...           54.690976   58.283582
std     299.408219     0.0  ...           88.842649   17.784651
min       3.000000  2016.0  ...            0.000000   11.000000
25%     107.000000  2016.0  ...            3.440000   44.750000
50%     299.000000  2016.0  ...           21.200000   59.500000
75%     617.000000  2016.0  ...           63.030000   72.000000
max    1000.000000  2016.0  ...          532.170000   99.000000

"""

# alternatively

movies_2016.index.size
# 297

# Movies by Cristopher Nolan

CN_movies = df.loc[df["Director" ] == "Christopher Nolan"]

print(CN_movies)
"""
     Rank                  Title  ... Revenue (Millions) Metascore
36     37           Interstellar  ...             187.99      74.0
54     55        The Dark Knight  ...             533.32      82.0
64     65           The Prestige  ...              53.08      66.0
80     81              Inception  ...             292.57      74.0
124   125  The Dark Knight Rises  ...             448.13      78.0

"""

CN_movies.index.size

# 5

"""

# Rating of 8.0
Rating = df.loc[df["Rating" ] >= 8.0]

print (Rating.describe())

"""
"""
           Rank         Year  ...  Revenue (Millions)  Metascore
count   78.000000    78.000000  ...           74.000000  73.000000
mean   283.820513  2011.705128  ...          143.596216  78.109589
std    250.106613     3.388709  ...          166.492187  10.796812
min      1.000000  2006.000000  ...            0.610000  42.000000
25%     94.000000  2009.000000  ...           17.892500  73.000000
50%    179.500000  2012.000000  ...          103.725000  79.000000
75%    465.750000  2015.000000  ...          201.827500  86.000000
max    992.000000  2016.000000  ...          936.630000  98.000000

"""

# median rating  for movies by CN

import statistics


CN_movies['Rating'].median()

# Find the year with the highest average rating

Highest_avg_rating = df
Highest_avg_rating.groupby('Year')['Rating'].mean()

"""
Year
2006    7.125000
2007    7.133962
2008    6.784615
2009    6.960784
2010    6.826667
2011    6.838095
2012    6.925000
2013    6.812088
2014    6.837755
2015    6.602362
2016    6.436700
Name: Rating, dtype: float64
"""

#Percentage increase in number of movies made between 2006 and 2016

import numpy as np


movies_2006 = df.loc[df["Year" ] == 2006]
print(movies_2006.describe())

movies_2007 = df.loc[df["Year" ] == 2007]
print(movies_2007.describe())

movies_2008 = df.loc[df["Year" ] == 2008]
print(movies_2008.describe())

movies_2009= df.loc[df["Year" ] == 2009]
print(movies_2009.describe())

movies_2010 = df.loc[df["Year" ] == 2010]
print(movies_2010.describe())

movies_2011 = df.loc[df["Year" ] == 2011]
print(movies_2011.describe())

movies_2012 = df.loc[df["Year" ] == 2012]
print(movies_2012.describe())

movies_2013 = df.loc[df["Year" ] == 2013]
print(movies_2013.describe())

movies_2014 = df.loc[df["Year" ] == 2014]
print(movies_2014.describe())

movies_2015 = df.loc[df["Year" ] == 2015]
print(movies_2015.describe())

movies_2016 = df.loc[df["Year" ] == 2016]
print(movies_2016.describe())

percentage_increase = pd.Series([44,297])

percentage_increase.pct_change()*100


# Common actor

Top_actor1 = df2.Actors.mode()
print(Top_actor1)



Top_actor = df['Actors'].value_counts().idxmax()
print(Top_actor)



common_value = df2['Actors'].mode()
print(common_value)
print (common_value.describe())

df8 = common_value

df8.value_counts().nlargest(3)



# df2.groupby('Actors').agg(lambda x: x.mode().iloc[0])




# common_actors = df2['Actors'].mode
# print(common_actors)

# df2['Actors'].value_counts().nlargest(3)
# df2['Actors'].value_counts().nlargest

# df['Actors'].value_counts().nlargest(1).index[0]

# df['Actors'].value_counts().nlargest(2).index[0]

# #unique genres

# Genre = df2.loc[df2["Genre" ] == :]
                
# s = df2['Genre']
# Unique_genres = s.loc['Genre':['Thriller', 'Action', 'Fantasy', 'Adventure','Sci-Fi', 'Comedy', 'Horror', 'Romance', 'Biography',  'Family',  'Drama',  'Crime', 'Mystery' ]]


unique_genre = df2.groupby(['Genre'])['Title'].value_counts().sort_values(ascending=False)
# print(unique_genre)

# unique_genre = df2.loc["Genre" :['Thriller', 'Action', 'Fantasy', 'Adventure','Sci-Fi', 'Comedy', 'Horror', 'Romance', 'Biography',  'Family',  'Drama',  'Crime', 'Mystery']]


unique_genre['Thriller','Music', 'Sport', 'Action', 'Fantasy', 'Adventure','Sci-Fi', 'Comedy', 'Horror', 'Romance', 'Biography',  'Family',  'Drama',  'Crime', 'Mystery'] = 'Genre'.str.split(' ', expand=True)


# plot correlation

import matplotlib.pyplot as plt

import numpy as np

x = df2["Revenue (Millions)"]
y = df2 ["Rating"]
z = df2 ["Votes"]
a = df2 ["Rank"]
b = df2 ["Metascore"]

plt.scatter(x, y)
plt.xlabel("Revenue")
plt.ylabel("Rating")

plt.plot(z, x)
plt.xlabel("Votes")
plt.ylabel("Revenue")


# rating vs rank
plt.plot(a, y )
plt.xlabel("Rank")
plt.ylabel("Rating")

#metascore vs votes

plt.plot(b, z )
plt.xlabel("Metascore")
plt.ylabel("Votes")

plt.scatter(b, z )
plt.xlabel("Metascore")
plt.ylabel("Votes")


# # rating vs rank
plt.scatter(y, x )
plt.ylabel("Revenue (Millions)")
plt.xlabel("Rating")


# #votes vs rank
plt.scatter(a, x)
plt.xlabel("Revenue (Millions)")
plt.ylabel("Rank")

plt.plot(a, x )
plt.xlabel("Revenue (Millions)")
plt.ylabel("Rank")


