import streamlit as st
import pandas as pd

@st.cache
def load_films():
    data_films = pd.read_csv("films.csv")
    return data_films
def load_series():
    #data_series = pd.read_csv("series.csv")
    return data_series

data_films = load_films()
#data_series = load_series()

#--------------------------------------------------Visuel---------------------------------------------------------

# Title
st.markdown("<h1 style='text-align: center; color: red;'>Films & Series Library</h1>", unsafe_allow_html=True)

# Sidebar with buttons and expanders
with st.sidebar:
    st.subheader("Menu")
    # Movies
    expander_movie = st.expander("Movies")
    raw_movies = expander_movie.button("All movies")
    # Movies by type
    expander_movie.text("Movie By type")  
    movie1, movie2, movie3 = expander_movie.container().columns(3)
    drama = movie1.button("Drama")
    horror = movie1.button("Horror")
    dark = movie1.button("Dark")
    biography = movie1.button('Biography')
    action = movie2.button("Action")
    comedy = movie2.button("Comedy")
    animation = movie2.button('Animation')
    mystery = movie2.button('Mystery')
    crime = movie3.button('Crime')
    adventure = movie3.button('Adventure')
    western = movie3.button('Western')
    
    # Series
    expander_serie = st.expander("Series")
    raw_series = expander_serie.button("All series")
    # Actors
    actors_list_films = [""]
    for i in range (len(data_films["actors"])):
        actors_list_films += data_films["actors"][i].split(',')
    actors_films = expander_movie.selectbox("Search an actor", set(actors_list_films))
    actors_series = expander_serie.text_input("Enter an actor of serie (respect case)")

# Contents
container_search = st.container()
container_search.markdown("<h2 style='text-align: center; color: blue;'>Your search</h2>", unsafe_allow_html=True)
data_sorted = data_films
# Sort
st.markdown("<p style='text-align: center; font-size: 24px;'>Sorted by ...</p>", unsafe_allow_html=True)
filtered_var = st.multiselect("",["date", "score", "time"])

# Graphs
more_info = st.container()
more_info.markdown("<h2 style='text-align: center; color: blue;'>More infos</h2>", unsafe_allow_html=True)
more_info.markdown("<h3 style='color: green;'>Films</h3>", unsafe_allow_html=True)
more_info.bar_chart(data_films["title"].groupby(data_films["type"]).count())
more_info.markdown("<h3 style='color: green;'>Series</h3>", unsafe_allow_html=True)
# more_info.bar_chart(data_series["title"].groupby(data_series["type"]).count())

#----------------------------------------------Gestion des requêtes------------------------------------------------
# function search
def search(data_sorted, button="",actors_films=""):
    data_sorted = data_sorted.loc[data_films["type"].str.contains(button)]
    if len(filtered_var) > 0:
        data_sorted = data_sorted.sort_values(by=filtered_var, ascending=False)
    if actors_films != "":
        data_sorted = data_sorted.loc[data_sorted["actors"].str.contains(f'{actors_films}')]
    return data_sorted
    
# Button actions
if raw_movies:
    data_sorted = data_films
elif drama:
    data_sorted = search(data_sorted, "Drama")
elif horror:
    data_sorted = search(data_sorted, "Horror")
elif action:
    data_sorted = search(data_sorted, "Action")
elif adventure:
    data_sorted = search(data_sorted, "Adventure")
elif comedy:
    data_sorted = search(data_sorted, "Comedy")
elif crime:
    data_sorted = search(data_sorted, "Crime")
elif dark:
    data_sorted = search(data_sorted, "Film-Noir")
elif biography:
    data_sorted = search(data_sorted, "Biography")
elif dark:
    data_sorted = search(data_sorted, "Film-Noir")
elif animation:
    data_sorted = search(data_sorted, "Animation")
elif mystery:
    data_sorted = search(data_sorted, "Mystery")
elif western:
    data_sorted = search(data_sorted, "Western")
if actors_films != "":
    data_sorted = search(data_sorted, actors_films=actors_films)

container_search.write(data_sorted)