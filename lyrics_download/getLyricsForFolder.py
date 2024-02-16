import os
from pprint import pprint
from geniusLyricsDownload import Genius_lyrics, CustomException


def getFilesInFolder(folder_path):
    file_paths = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            path1 = file_path.split('\\')
            file_paths.append(path1[1])
    return file_paths


folder_path = 'downloads/emotion/happy'
files = getFilesInFolder(folder_path)
not_found = []
count = 0
for file in files:
    print(file)
    temp = file.split(".opus")[0].split(" - ")
    print(temp)
    artist = temp[0]
    song = temp[-1]
    try:
        Genius_lyrics(song, artist)
        count += 1
    except CustomException as e:
        not_found.append(file)

print(count)
print(not_found)
print(len(not_found))

['Aastha Gill - Buzz.opus', 'Abhijeet Bhattacharya - Main Khiladi Tu Anari.opus', 'Abhijeet Bhattacharya - Main Koi Aisa Geet Gaoon.opus', 'Abhijeet Bhattacharya - Waada Raha Sanam (Duet).opus', 'Adnan Sami - Aye Udi Udi Udi.opus', 'AKASA - Shola.opus', 'Akull - Faraar.opus', 'Akull - Soulmate.opus', 'Alka Yagnik - Dekha Hai Pehli Baar-Duet.opus', 'Alka Yagnik - Kaho Naa Pyar Hai (Happy).opus', 'Alka Yagnik - Kuch To Hua Hai.opus', 'Alka Yagnik - Main Tujhse Aise Milun.opus', 'Alka Yagnik - Mujhe Pyar Hua Allamiya.opus', 'Amit Trivedi - Love You Zindagi.opus', 'Anuradha Paudwal - Achutam Keshwam.opus', 'Arijit Singh - Gerua (From #Dilwale#).opus', 'Arijit Singh - Saanson Ko (From #Zid#).opus', 'Arijit Singh - Tere Hoke Rahengay.opus', 'Arijit Singh - Tu Hi Hai.opus', 'Ash King - Kill Chori.opus', 'Asha Bhosle - Le Gayi.opus', 'B Praak - Naah Goriye.opus', 'Badshah - Top Tucker.opus', 'Clinton Cerejo - Kya Karoon#.opus', 'Darshan Raval - Ek Ladki Ko Dekha Toh Aisa Laga - Title Track.opus', 'Darshan Raval - KhairMangde - Male Version.opus', 'Darshan Raval - Rabba Mehr Kari.opus', 'DIVINE - 3#59 AM.opus', 'Gulzar - Sajde.opus', 'Hariharan - Mhare Hiwra Main Nache Mor.opus', 'Ishaan Khan - Aise Na Mujhe Tum Dekho.opus', 'K.K. - Ek Nazar Mein Bhi.opus', 'Kavita Krishnamurthy - Pyar Hua Chupke Se.opus', 'Kavita Krishnamurthy - Rehnaa Hai Tere Dil Mein.opus', 'Kumar Sanu - Baazigar O Baazigar.opus', 'Kumar Sanu - Chura Ke Dil Mera.opus', 'Kumar Sanu - Duniya Mein Aaye.opus', 'Kumar Sanu - Jab Koi Baat Bigad Jaye.opus', 'Kumar Sanu - Jeeta Hoon Jiske Liye.opus', 'Kumar Sanu - Kitna Haseen Chehra.opus', 'Kumar Sanu - Kuchh Na Kaho (Happy).opus', 'Kumar Sanu - O Lal Dupatte Wali.opus', 'Kumar Sanu - Raja Ko Rani Se- Kumar Sanu & Alka Yagnik.opus', 'Kumar Sanu - Ye Kaali Kaali Aankhen.opus', 'Lata Mangeshkar - Dil To Pagal Hai.opus', 'Lata Mangeshkar - Maye Ni Maye.opus', 'Lucky Ali - Na Tum Jano Na Hum.opus', 'Mellow D - Drunk n High.opus', 'Minmini - Chhoti Si Aasha (Version, 1).opus', 'Mpower - Zindagi Ko Hi5.opus', 'Neha Kakkar - Dil Ko Karaar Aaya (From #Sukoon#).opus', 'Pritam - Hawayein.opus', 'Pritam - The Breakup Song (From #Ae Dil Hai Mushkil#).opus', 'Roop Kumar Rathod - Dilko Tumse Pyar Hua.opus', 'S. P. Balasubrahmanyam - Bahut Pyar Karte Hai-Male.opus', 'S. P. Balasubrahmanyam - Pehla Pehla Pyar.opus', 'S. P. Balasubrahmanyam - Saathiya Tune Kya Kiya.opus', 'S. P. Balasubrahmanyam - Tumse Milne Ki Tamanna Hai.opus', 'Sachin-Jigar - Panghat.opus', 'Sadhana Sargam - Saat Samundar Paar (Happy).opus', 'Salim-Sulaiman - Haule Haule.opus', 'Shaan - Chand Sifarish.opus', 'Shankar Ehsaan Loy - Tattoo Waaliye.opus', 'Shankar Mahadevan - Pretty Woman.opus', 'Shankar Mahadevan - Tumhe Aaj Maine Jo Dekha.opus', 'Shreya Ghoshal - Shikdum.opus', 'Sonu Nigam - Chup Chup Ke.opus', 'Sukriti Kakar - Sona Lagda.opus', 'Tony Kakkar - Booty Shake.opus', 'Tony Kakkar - Chocolate (From #Sangeetkaar#).opus', 'Tony Kakkar - Kurta Pajama (From #Sangeetkaar#).opus', 'Tony Kakkar - Yaari Hai.opus', 'Udit Narayan - Chote Chote Bhaiyon Ke Bade Bhaiya.opus', 'Udit Narayan - Koi Mil Gaya.opus', 'Udit Narayan - Too Cheez Badi Hain (Duet).opus', 'Udit Narayan - Yeh Ladka Hai Deewana.opus', 'Vayu - Naagin.opus', 'Vinod Rathod - Ae Mere Humsafar.opus', 'Vishal-Shekhar - Ghungroo.opus', 'Vishal-Shekhar - Hey Shona.opus', 'Vishal-Shekhar - Jai Jai Shivshankar.opus', 'Vishal-Shekhar - Nashe Si Chadh Gayi.opus', 'Zara Khan - BellBottom Theme - Dhoom Tara.opus']
