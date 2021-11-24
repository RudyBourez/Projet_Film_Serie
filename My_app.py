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
    actors_films = expander_movie.text_input("Enter an actor of movie(respect case)")
    actors_series = expander_serie.text_input("Enter an actor of serie (respect case)")

container_search = st.container()
container_search.write("Your search")

# Filters
st.markdown("<h2 style='text-align: center; color: blue;'>Filtered_by ...</h2>", unsafe_allow_html=True)
filtered_var = st.multiselect("",["date", "score", "time"])

# Button actions
if raw_movies:
    data_sorted = data_films
    container_search.write(data_sorted)
elif drama:
    if len(filtered_var) > 0:
        data_sorted = data_films.loc[data_films["type"].str.contains("Drama")].sort_values(by=filtered_var, ascending=False)
    else :
        data_sorted = data_films.loc[data_films["type"].str.contains("Drama")]
    container_search.write(data_sorted)
elif horror:
    if len(filtered_var) > 0:
        data_sorted = data_films.loc[data_films["type"].str.contains("Horror")].sort_values(by=filtered_var, ascending=False)
    else :
        data_sorted = data_films.loc[data_films["type"].str.contains("Horror")]
    container_search.write(data_sorted)
elif action:
    if len(filtered_var) > 0:
        data_sorted = data_films.loc[data_films["type"].str.contains("Action")].sort_values(by=filtered_var, ascending=False)
    else :
        data_sorted = data_films.loc[data_films["type"].str.contains("Action")]
    container_search.write(data_sorted)
elif adventure:
    if len(filtered_var) > 0:
        data_sorted = data_films.loc[data_films["type"].str.contains("Adventure")].sort_values(by=filtered_var, ascending=False)
    else :
        data_sorted = data_films.loc[data_films["type"].str.contains("Adventure")]
    container_search.write(data_sorted)
elif comedy:
    if len(filtered_var) > 0:
        data_sorted = data_films.loc[data_films["type"].str.contains("Comedy")].sort_values(by=filtered_var, ascending=False)
    else :
        data_sorted = data_films.loc[data_films["type"].str.contains("Comedy")]
    container_search.write(data_sorted)
elif crime:
    if len(filtered_var) > 0:
        data_sorted = data_films.loc[data_films["type"].str.contains("Crime")].sort_values(by=filtered_var, ascending=False)
    else :
        data_sorted = data_films.loc[data_films["type"].str.contains("Crime")]
    container_search.write(data_sorted)

elif actors_films != "":
    data_sorted = data_films.loc[data_films["actors"].str.contains(actors_films)]
    container_search.write(data_sorted)