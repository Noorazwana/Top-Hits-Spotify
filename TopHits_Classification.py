import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("https://raw.githubusercontent.com/Noorazwana/Top-Hits-Spotify/main/songs_normalize.csv")
df.head()

df.tail

df.year.unique()

s1=(len(df.query('year==1998')))
s2=(len(df.query('year==1999')))
s3=(len(df.query('year==2020')))
s= s1+s2+s3
print("The total number of songs:",s)

df_years_drop = df[(df['year'] <2000) | (df['year'] > 2019)].index
df = df.drop(df_years_drop) #removing the rows from dataframe based on the above condition

df.shape
df.columns
df.dtypes

artist=df['artist'].value_counts()
artist

tp_artists_songs= artist[:5]
tp_artists_name =artist[:5].index
fig = plt.figure(figsize = (10, 5))
plt.bar(tp_artists_name,tp_artists_songs,width = 0.4,color="forestgreen")
plt.xlabel("Artists")
plt.ylabel("No of Songs")
plt.title('Top Artists with Hit Songs',color = 'black',fontsize = 20)
plt.show()

genre = df['genre'].value_counts()
genre
