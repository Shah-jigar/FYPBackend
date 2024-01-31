import requests
from bs4 import BeautifulSoup

def get_lyrics(song_name, artist_name):
    # Define the URL for the lyrics search
    url = f"https://www.musixmatch.com/lyrics/{artist_name}-{song_name}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the lyrics element in the HTML
        lyrics_element = soup.find("div", {"class": "lyrics__content"})

        # Check if the lyrics element was found
        if lyrics_element:
            # Extract the lyrics text
            lyrics = lyrics_element.get_text()

            # Return the lyrics
            return lyrics

        else:
            # Return an error message if the lyrics element was not found
            return "Lyrics not found."

    else:
        # Return an error message if the request was not successful
        return "Error: Unable to retrieve lyrics."

# Test the function with a Hindi song
    "Abhijeet Srivastava - Chashni (From Bharat)"
song_name = "Udd Jaa Kaale Kaava"
artist_name = "Udit Narayan, Alka Yagnik, Mithoon, Uttam Singh"
lyrics = get_lyrics(song_name, artist_name)
print(lyrics)