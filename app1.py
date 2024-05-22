import streamlit as st
from google_play_scraper import search, app
import logging
import random

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Function to fetch and display app details
def display_app_details(app_id):
    result = app(
        app_id,
        lang='en',
        country='us'
    )
    st.image(result['icon'], width=150)
    st.markdown(f"<h2 style='color:#1f77b4;'>{result['title']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<b>Genre:</b> {result['genre']}", unsafe_allow_html=True)
    st.markdown(f"<b>Rating:</b> {result['score']}", unsafe_allow_html=True)
    st.markdown(f"<b>Installs:</b> {result['installs']}", unsafe_allow_html=True)
    st.markdown(f"<b>Last Updated:</b> {result.get('updated', 'N/A')}", unsafe_allow_html=True)
    st.markdown(f"<b>Required Android Version:</b> {result.get('androidVersion', 'N/A')}", unsafe_allow_html=True)
    st.markdown(f"<p>{result['description']}</p>", unsafe_allow_html=True)
    st.markdown(f"[More Info]({result['url']})")

# Function to search apps by genre and display 3-4 random results
def search_apps_by_genre(genre):
    logging.info(f"Search initiated for genre: {genre}")
    results = search(
        genre,
        lang='en',
        country='us',
        n_hits=10  # Fetch more results to allow random selection
    )
    if results:
        selected_results = random.sample(results, min(4, len(results)))  # Select 3-4 random results
        for res in selected_results:
            display_app_details(res['appId'])
    else:
        st.warning(f"No results found for the genre: {genre}")
        logging.warning(f"No results found for the genre: {genre}")

# Streamlit App
def main():
    st.set_page_config(page_title="Game Recommendation Engine", page_icon=":video_game:", layout="centered")

    st.markdown("""
        <style>
            body {
                background: url('https://i.imgur.com/EoY6oPb.jpg');
                background-size: cover;
            }
            .main-container {
                background: rgba(255, 255, 255, 0.8);
                padding: 3rem;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                max-width: 800px;
                margin: auto;
            }
            .stButton button {
                background-color: #FFA07A;
                color: white;
                border-radius: 8px;
                padding: 0.75rem 1.5rem;
                font-size: 1.1rem;
                transition: background-color 0.3s ease;
            }
            .stButton button:hover {
                background-color: #FF6347;
            }
            .stButton button:active {
                background-color: #FF4500;
            }
            h1 {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: #FF6347;  /* Change title color */
                text-align: center;
                font-size: 2.5rem;
                font-weight: bold;
                margin-bottom: 0.5rem;
            }
            h3 {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: #333333;
                text-align: center;
                font-size: 1.25rem;
                color: #666666;
                margin-bottom: 2rem;
            }
            .input-box {
                margin-bottom: 1rem;
            }
            .button-group {
                display: flex;
                justify-content: center;
                gap: 1rem;
            }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.header("Instructions")
    st.sidebar.write("""
        1. Enter a game genre in the text box.
        2. Click 'Submit' to get game recommendations.
        3. Click 'Reset' to clear your input and start over.
    """)
    st.sidebar.header("About")
    st.sidebar.write("""
        This Game Recommendation Engine helps you find games based on your favorite genres. 
        It fetches data from the Google Play Store and provides details about each game.
    """)

    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1>Video Game Recommendation Engine</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Select a game genre to get started!</h3>", unsafe_allow_html=True)

    genre = st.text_input('Enter the genre (e.g., shooting, puzzle):', '')

    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('Submit'):
            if genre:
                with st.spinner('Fetching recommendations...'):
                    st.markdown("<h3 class='subtitle'>Recommendations:</h3>", unsafe_allow_html=True)
                    search_apps_by_genre(genre)
            else:
                st.error("Please enter a genre to search.")
                logging.error("Search attempted without entering a genre.")
    
    with col2:
        if st.button('Reset'):
            st.experimental_rerun()

    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("""
        <style>
            footer {visibility: hidden;}
            .reportview-container .main .block-container{padding-top: 3rem;}
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()