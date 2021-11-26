import streamlit as st
import pandas as pd

@st.cache
def load():
    data_films = pd.read_csv("films.csv")
    data_series = pd.read_csv("series.csv") 
    return data_films, data_series

data_films, data_series = load()


#--------------------------------------------------Visuel---------------------------------------------------------

st.markdown("<h1 style='text-align: center; color: red;'>Films & Series Library</h1>", unsafe_allow_html=True)

# Sidebar with buttons and expanders
with st.sidebar:
    st.subheader("Menu")
    #---------------------Movies------------------------
    expander_movie = st.expander("Movies")
    raw_movies = expander_movie.button("All movies")
    # Movies by type
    type_films = [""]
    for i in range (len(data_films["type"])):
        type_films += data_films["type"][i].split(',')
    buttons_films = expander_movie.selectbox("Movie by type", set(type_films))
    
    #---------------------Series-----------------------
    type_series = [""]
    for i in range (len(data_series["type"])):
        type_series += data_series["type"][i].split(',')
    expander_serie = st.expander("Series")
    raw_series = expander_serie.button("All series")
    # Series by type
    buttons_series = expander_serie.selectbox("Serie by type", set(type_series))

    #----------------------Actors---------------------
    actors_list_films = [""]
    for i in range (len(data_films["actors"])):
        actors_list_films += data_films["actors"][i].split(',')
    actors_films = expander_movie.selectbox("Search an actor", set(actors_list_films))

    actors_list_series = [""]
    for i in range (len(data_series["actors"])):
        actors_list_series += data_series["actors"][i].split(',')
    actors_series = expander_serie.selectbox("Search an actor", set(actors_list_series))


#-------------------------------Contents-------------------------
container_search = st.container()
container_search.markdown("<h2 style='text-align: center; color: blue;'>Your search</h2>", unsafe_allow_html=True)
data_sorted = data_films
#---------------------------------Sort---------------------------
st.markdown("<p style='text-align: center; font-size: 24px;'>Sorted by ...</p>", unsafe_allow_html=True)
filtered_var = st.multiselect("",["date", "score", "time"])

#-------------------------------Graphs--------------------------
more_info = st.container()
more_info.markdown("<h2 style='text-align: center; color: blue;'>More infos</h2>", unsafe_allow_html=True)
more_info.markdown("<h3 style='color: green;'>Films</h3>", unsafe_allow_html=True)
more_info.bar_chart(data_films["title"].groupby(data_films["type"]).count())
more_info.markdown("<h3 style='color: green;'>Series</h3>", unsafe_allow_html=True)
#more_info.bar_chart(data_series["title"].groupby(type_series).count())

#----------------------------------------------Gestion des requêtes------------------------------------------------

#---------------------------function search--------------------------
def search(data_sorted, button, filtered_var, actors):
    """This function runs all requests made by the user such as switching between films & series"""
    if button != "":
        data_sorted = data_sorted.loc[data_sorted["type"].str.contains(button)]
    if len(filtered_var) > 0:
        data_sorted = data_sorted.sort_values(by=filtered_var, ascending=False)
    if actors != "":
        data_sorted = data_sorted.loc[data_sorted["actors"].str.contains(f'{actors}')]
    return data_sorted, button    

#----------------------------------Requests------------------------------------

if raw_movies:
    data_sorted = data_films
if buttons_films:
    data_sorted, buttons_films = search(data_films, buttons_films, filtered_var, actors_films)
if actors_films:
    data_sorted, buttons_films = search(data_films, buttons_films, filtered_var, actors_films)

if raw_series:
    data_sorted = data_series
if buttons_series:
    data_sorted, buttons_series = search(data_series, buttons_series, filtered_var, actors_series)
if actors_series:
    data_sorted, buttons_series = search(data_series, buttons_series, filtered_var, actors_series)

if filtered_var:
    data_sorted, buttons_films = search(data_sorted, buttons_films, filtered_var, actors_films)

container_search.write(data_sorted)