import requests
from bs4 import BeautifulSoup
import json

def scrape_top_games():
    url = 'https://play.google.com/store/games?hl=en_IN&gl=US'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    games = []

    # Modify the selectors based on the actual HTML structure of the page
    game_elements = soup.select('div.card')  # Example selector

    for game in game_elements[:100]:  # Limit to top 100 games
        name = game.select_one('a.title').get_text()
        package = game['data-docid']
        description = game.select_one('div.description').get_text()
        icon_url = game.select_one('img.cover-image')['src']
        link = f'https://play.google.com/store/apps/details?id={package}'

        games.append({
            'name': name,
            'package': package,
            'description': description,
            'icon_url': icon_url,
            'link': link
        })

    with open('data/games.json', 'w') as f:
        json.dump(games, f, indent=4)

if __name__ == '__main__':
    scrape_top_games()
