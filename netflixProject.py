'''

     apne pass 8000s netflix rows ka data hi
     isko visualzie krege kregen ki konsi movie kinti der ki unki kya ratinges kb release hui thi graphs ke format me
           


'''


#step 1:- Import the libarires

import  pandas as pd
import  matplotlib.pyplot as plt


#step 2:- Load the data
df=pd.read_csv('netflix_titles.csv')

#step 3:- Clean the data
df=df.dropna(subset=['type','release_year','rating','country','duration'])#dropna ka mtlb jis row me missing value (NaN) ho, use remove kar do
                                                                          #subset specify krta sirf in columns ko check karo ,Baaki columns me NaN ho, to koi problem nahi


#Graph Draw krnege
type_counts=df['type'].value_counts()#DataFrame ka ek column select ho raha hai
'''
 .value_counts()
        Har unique value ko count karta hai
        Automatically descending order me sort karta hai
        Result Series ke form me aata hai
'''
# plt.figure(figsize=(6,5))#ye figure hi apne graph ke window ka size rhega wo batata hi
#
# plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'])
# plt.title('Number of Movies Vs TV Shows on Netflix')
# plt.xlabel('Type')
# plt.ylabel('Count')
# plt.savefig('movies_vs_tvshows.png')
# plt.tight_layout()
# plt.show()


#AB CONENT KI RATING KINTI JADYA DISTRIBUTED HI USKE LIYE APNE PIE CHART BANAYEGE

# rating_counts=df['rating'].value_counts()
# plt.figure(figsize=(6,6))
# plt.pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%',startangle=90)
# plt.title('Percentage Content Ratings')
# plt.tight_layout()
# plt.savefig('content_ratings.png')
# plt.show()


#Movie ka duration kinta distrubtion wo baneyge histogram ka used krke

# movie_df=df[df['type']=='Movie'].copy()
# movie_df['duration_int']=movie_df['duration'].str.replace('min','').astype(int)
#
# plt.figure(figsize=(8,6))
# plt.hist(movie_df['duration_int'],bins=30,color='purple',edgecolor='black')
# plt.title('Distributation of movie duration ')
# plt.xlabel('Duration (minutes')
# plt.ylabel('Number of movies')
# plt.tight_layout()
# plt.savefig('movie_duration_histogram.png')
# plt.show()
#


#ab apne scatter plot banyege jaha pr apne releasing year vs no of shows
# release_counts=df['release_year'].value_counts().sort_index()
# plt.figure(figsize=(10,6))
# plt.scatter(release_counts.index,release_counts.values,color='red')
# plt.title('Release Year Vs Number of Shows')
# plt.xlabel('Release Year')
# plt.ylabel('Number of shows')
# plt.tight_layout()
# plt.savefig('release_year_scatter.png')
# plt.show()

# coutry_counts=df['country'].value_counts().head(10)
# plt.figure(figsize=(8,6))
# plt.barh(coutry_counts.index,coutry_counts.values,color='teal')
# plt.title('Top 10 Countries Number of Shows')
# plt.xlabel('Number of Shows')
# plt.ylabel('Country')
# plt.tight_layout()
# plt.savefig('top10_countries.png')
# plt.show()

content_by_year=df.groupby(['release_year','type']).size().unstack().fillna(0)

fig,ax=plt.subplots(1,2,figsize=(12,5))

#first subplots:movies
ax[0].plot(content_by_year.index,content_by_year['Movie'],color='blue')
ax[0].set_title('Movies Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

#second subplots:TV Shows
ax[0].plot(content_by_year.index,content_by_year['TV Show'],color='blue')
ax[0].set_title('TV Shows Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

fig.suptitle('comparison of movies and tv shows released over years')
plt.tight_layout()
plt.savefig('movies_tv_shows_comparison.png')
plt.show()