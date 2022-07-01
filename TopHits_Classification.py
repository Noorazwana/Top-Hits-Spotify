import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Top Hits Song
This app predicts the **Top Hits** song!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    year = st.sidebar.slider('Year', 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010)
    danceability = st.sidebar.slider('danceability', 0.5, 0.6, 0.7, 0.8, 0.9)
    energy = st.sidebar.slider('energy', 0.5, 0.6, 0.7, 0.8, 0.9)
    key = st.sidebar.slider('key', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    data = {'year': year,
            'danceability': danceability,
            'energy': energy,
            'genre': genre}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

TopHitsSpotify = pd.read_csv('songs_normalize.csv')
st.write('artist')
X = songs_normalize.drop('genre',axis=1)
Y = songs_normalize.genre

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(Top Hits.genre)

st.subheader('Prediction')
#st.write(iris.species[prediction])
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)

