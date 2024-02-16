import os
import requests
from bs4 import BeautifulSoup
from ltr import preprocessyrics, toHindi, contains_hindi


path = 'lyrics'

# Make a search request to Genius API
url = 'https://www.jiosaavn.com/lyrics/sab-kuchh-tha-lyrics/AV4oCBMJAko'
response = requests.get(url)
# print(data)

# Check if the request was successful
if response.status_code == 200:
    # Extract relevant information from the response

    # Parse HTML content to extract lyrics
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())
    # with open('text_output.txt', 'w', encoding='utf-8') as f:
    # f.write(text_content + '\n')


# //*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[4]/div[1]/div/div[1]/div/p[1]
    elements = soup.find_all(
        'p', class_='Type__TypeElement-sc-goli3j-0 bGcjcI xt5C47eHPYNiriMJxGnC')

# Create or open a text file for writing
    # with open('text_output.txt', 'w', encoding='utf-8') as f:
    #     # Loop through each element and extract the text content
    #     for element in elements:
    #         text_content = element.text.strip()
    #         # Write the text content to the text file
    #         f.write(text_content + '\n')
    # For garhwalii.com
     # post-body-5372788924330859547
    # spans = soup.select("div[id = 'post-body-5372788924330859547']  div")
    # for span in spans:
    #     print(span.text)

    spans = soup.select("p[class = 'u-margin-bottom-none@sm'] span")
    for span in spans:
        print(span.text)

    # target_element = soup.select_one("#Blog1 > div > article > div.post-inner-area > div.post-body.entry-content > div:nth-child(9)")
    # spans = soup.select(
    #     "#Blog1 > div > article > div.post-inner-area > div.post-body.entry-content > div:nth-child(9) div")
    # for span in spans:
    #     print(span.text)

else:
    print(f"Error: {response.status_code}")
