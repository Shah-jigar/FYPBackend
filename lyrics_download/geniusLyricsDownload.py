import requests
from bs4 import BeautifulSoup

def Genius_lyrics(song_title, artist_name):
    access_token = '3mMduEpFc43-RQmPpffLONmmSnBTZWWIzlcqioYtTJyc1QDOm_RsLeNOtYptwYpA'

    # Make a search request to Genius API
    url = f'https://api.genius.com/search?q={song_title} {artist_name}'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    data = response.json()

    # Check if the request was successful
    if response.status_code == 200:
        # Extract relevant information from the response
        hits = data['response']['hits']
        if hits:
            first_hit = hits[0]['result']
            song_title = first_hit['title']
            artist_name = first_hit['primary_artist']['name']
            lyrics_url = first_hit['url']

            print(f"Song: {song_title} by {artist_name}")
            print(f"Lyrics URL: {lyrics_url}")

            # Make a request to the lyrics URL
            lyrics_response = requests.get(lyrics_url)
            if lyrics_response.status_code == 200:
                # Parse HTML content to extract lyrics
                soup = BeautifulSoup(lyrics_response.text, 'html.parser')
                lyrics_div = soup.find('div', class_='Lyrics__Container-sc-1ynbvzw-1')
                # <div data-lyrics-container="true" class="Lyrics__Container-sc-1ynbvzw-1 kUgSbL">[Verse 1]<br>हम तेरे बिन अब रह नहीं सकते<br>तेरे बिना क्या वजूद मेरा?<br>हम तेरे बिन अब रह नहीं सकते<br>तेरे बिना क्या वजूद मेरा?<br>तुझ से जुदा अगर हो जाएँगे<br>तो ख़ुद से ही हो जाएँगे जुदा<br><br>[Chorus]<br>क्योंकि तुम ही हो, अब तुम ही हो<br>ज़िंदगी अब तुम ही हो<br>चैन भी, मेरा दर्द भी<br>मेरी आशिक़ी अब तुम ही हो<br><br>[Verse 2]<br>तेरा-मेरा रिश्ता है कैसा?<br>एक पल दूर गवारा नहीं<br>तेरे लिए हर रोज़ हैं जीते<br>तुझ को दिया मेरा वक्त सभी<br>कोई लमहा मेरा ना हो तेरे बिना<br>हर साँस पे नाम तेरा<br><br>[Chorus]<br>क्योंकि तुम ही हो, अब तुम ही हो<br>ज़िंदगी अब तुम ही हो<br>चैन भी, मेरा दर्द भी<br>मेरी आशिक़ी अब तुम ही हो<br>तुम ही हो, तुम ही हो<br><br>[Verse 3]<br>तेरे लिए ही जिया मैं<br>ख़ुद को जो यूँ दे दिया है<br>तेरी वफ़ा ने मुझ को सँभाला<br>सारे ग़मों को दिल से निकाला<br>तेरे साथ मेरा है नसीब जुड़ा<br>तुझे पा के अधूरा ना रहा<br><br>[Chorus]<br>क्योंकि तुम ही हो, अब तुम ही हो<br>ज़िंदगी अब तुम ही हो<br>चैन भी, मेरा दर्द भी<br>मेरी आशिक़ी अब तुम ही हो<br><br>क्योंकि तुम ही हो, अब तुम ही हो<br>ज़िंदगी अब तुम ही हो<br>चैन भी, मेरा दर्द भी<br>मेरी आशिक़ी अब तुम ही हो</div>
                if lyrics_div:
                    lyrics = lyrics_div.get_text('\n', strip=True)
                    
                    file_path = artist_name +"-" +song_title+'.txt'
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(lyrics)

                    # print(f"\nLyrics:\n{lyrics}")
                else:
                    print("Lyrics not found on the page.")
            else:
                print(f"Error fetching lyrics: {lyrics_response.status_code}")
        else:
            print("Song not found.")
    else:
        print(f"Error: {response.status_code}")
# Anup Jalota - Ae Malik Tere Bande Hum
song_title = 'Ae Malik Tere Bande Hum'
artist_name = 'Anup Jalota'

song_name = "Udd Jaa Kaale Kaava"
artist_name = "Udit Narayan, Alka Yagnik, Mithoon, Uttam Singh"
Genius_lyrics(song_name, artist_name)