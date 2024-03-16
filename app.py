import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=32b5ff69e83f997a25a83211da6e403c&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']




def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    
    return recommended_movies, recommended_movies_posters



movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)


similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].tolist()  # Convert the column to a list
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])  # Use names[0] directly without quotes
        st.image(posters[0])  # Use posters[0] directly without quotes
    with col2:
        st.text(names[1])  # Use names[1] directly without quotes
        st.image(posters[1])  # Use posters[1] directly without quotes
    with col3:
        st.text(names[2])  # Use names[2] directly without quotes
        st.image(posters[2])  # Use posters[2] directly without quotes
    with col4:
        st.text(names[3])  # Use names[3] directly without quotes
        st.image(posters[3])  # Use posters[3] directly without quotes
    with col5:
        st.text(names[4])  # Use names[4] directly without quotes
        st.image(posters[4])  # Use posters[4] directly without quotes
