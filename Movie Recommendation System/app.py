import streamlit as st
import pandas as pd
import pickle
import requests

st.title('Movie Recommendation System')

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

chosen_movie = st.selectbox("Enter a Movie", movies['title'].values)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedf.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    # recommended_movies_posters = []

    for i in movies_list:
        movie_id = i[0]
        # recommended_movies_posters.append(fetch_poster(i[0]))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies # recommended_movies #, recommended_movies_posters

if st.button('Recommend'):
    names = recommend(chosen_movie)
    for i in names:
        st.write(i)
