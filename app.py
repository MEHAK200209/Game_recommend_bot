import streamlit as st
from google_play_scraper import search, app
import pandas as pd

# Function to fetch and display app details
def display_app_details(app_id):
    # Fetch app details
    result = app(
        app_id,
        lang='en',  # Language in English
        country='us'  # Country as USA
    )
    # Display app details
    st.image(result['icon'], width=100)
    st.write('###', result['title'])
    st.write('**Genre:**', result['genre'])
    st.write('**Rating:**', result['score'])
    st.write('**Installs:**', result['installs'])
    st.write('**Description:**', result['description'])
    st.write('[More Info](%s)' % result['url'])

# Function to search apps by genre and save top 100 to CSV
def search_apps_by_genre(genre):
    results = search(
        f'free {genre} game',
        lang='en',
        country='us',
        n_hits=100  # Limit to the top 100 results
    )
    if results:
        apps_data = []
        for res in results:
            app_details = app(res['appId'], lang='en', country='us')
            apps_data.append({
                'name': app_details['title'],
                'package_name': app_details['appId'],
                'description': app_details['description'],
                'icon_url': app_details['icon'],
                'genre': app_details['genre'],
                'rating': app_details['score'],
                'installs': app_details['installs'],
                'url': app_details['url']
            })
            display_app_details(res['appId'])
        df = pd.DataFrame(apps_data)
        df.to_csv('games_data.csv', index=False)
        st.write("Top 100 games saved to `games_data.csv`")
    else:
        st.write("No results found for the genre:", genre)

# Streamlit App
def main():
    st.title('Game Recommendation')
    
    genre = st.text_input('Enter the genre (e.g., shooting, puzzle):', '')

    if st.button('Search'):
        if genre:
            search_apps_by_genre(genre)

if __name__ == "__main__":
    main()
