import requests
from bs4 import BeautifulSoup
from pprint import pprint
def get_playlist_songs(playlist_url):
    # Send a GET request to the playlist URL
    response = requests.get(playlist_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        # soup = BeautifulSoup(html_snippet, 'html.parser')

        # Find all ul elements with the class "_row list_data"
        ul_elements = soup.find_all('div', class_='_grp')[1:]
        # pprint(ul_elements)
        # Extract song names from each ul element
        song_names = []
        artist_names = []
        for ul_element in ul_elements:
            artist_name = ""
            # song_name = ul_element.find('span', class_='t_over').get_text(strip=True)
            span_element = ul_element.find('span', class_='t_over')
            # Remove the inner <span> element if it exists
            inner_span = span_element.find('span', class_='new_premium')
            if inner_span:
                inner_span.extract()
            # Extract the text
            song_name = span_element.get_text(strip=True)
            song_names.append(song_name)
            # Extract the artist name
            artist_name_elements = ul_element.find_all('a', class_='_link')
            artist_names.append(', '.join([artist.get_text(strip=True) for artist in artist_name_elements]))

        # return song_titles
        return song_names,artist_names
    else:
        print(f"Error: Unable to fetch the playlist. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    playlist_url = "https://gaana.com/playlist/gaana-dj-2020s-happy-hits-hindi"
    songs, artists = get_playlist_songs(playlist_url)

    if songs:
        print("Songs in the playlist:")
        # for index, song in enumerate(songs, start=1):
        #     print(f"{song}")
        # lst = []
        # for i in songs:
        #     t = i.split("Premium  ")
        #     lst.append(t[1])
            # print(t[1])
        # print(lst)
        print(songs)
        print(artists)