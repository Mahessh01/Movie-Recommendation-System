import streamlit as st
import pickle as pkl
import pandas as pd
import requests

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right,#141E30,#243B55);
}

.title{
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:white;
}

.subtitle{
    text-align:center;
    color:#d6d6d6;
    font-size:18px;
    margin-bottom:30px;
}

.poster{
    border-radius:15px;
}

.movie-name{
    text-align:center;
    font-size:18px;
    font-weight:bold;
    color:white;
    margin-top:10px;
}

footer{
visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# LOAD DATA
# -------------------------

movies = pd.DataFrame(
    pkl.load(open("movie_dict.pkl","rb"))
)

similarity = pkl.load(open("similarity.pkl","rb"))

# -------------------------
# FETCH POSTER
# -------------------------

def fetch_poster(movie_id):

    url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

    try:

        data=requests.get(url).json()

        if data.get("poster_path"):

            return "https://image.tmdb.org/t/p/w500"+data["poster_path"]

    except:

        pass

    return "https://via.placeholder.com/500x750?text=No+Poster"

# -------------------------
# RECOMMEND
# -------------------------

def recommend(movie):

    movie_index=movies[movies["title"]==movie].index[0]

    distances=similarity[movie_index]

    movie_list=sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x:x[1]
    )[1:6]

    names=[]
    posters=[]

    for i in movie_list:

        movie_id=movies.iloc[i[0]]["id"]

        names.append(
            movies.iloc[i[0]]["title"]
        )

        posters.append(
            fetch_poster(movie_id)
        )

    return names,posters

# -------------------------
# HEADER
# -------------------------

st.markdown(
    "<div class='title'>🎬 Movie Recommendation System</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Discover movies similar to your favorites 🍿</div>",
    unsafe_allow_html=True
)

# -------------------------
# SELECT MOVIE
# -------------------------

selected_movie=st.selectbox(
    "Choose your favourite movie",
    movies["title"].values
)

# -------------------------
# BUTTON
# -------------------------

if st.button("🍿 Recommend Movies",use_container_width=True):

    with st.spinner("Finding similar movies..."):

        names,posters=recommend(selected_movie)

    st.markdown("## Recommended for You")

    cols=st.columns(5)

    for i,col in enumerate(cols):

        with col:

            st.image(posters[i],use_container_width=True)

            st.markdown(
                f"<div class='movie-name'>{names[i]}</div>",
                unsafe_allow_html=True
            )

st.markdown("---")

st.markdown(
"""
<center style='color:white'>
by Mahesh AKA Batman
</center>
""",
unsafe_allow_html=True
)