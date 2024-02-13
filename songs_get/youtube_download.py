# Download songs from youtube

import yt_dlp


def download_music(artist, song, output_path='./downloads'):
    # Create the search query
    search_query = f'ytsearch:{artist} {song} audio'

    # Set up options for yt_dlp to download in Opus format
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/{artist} - {song}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'opus',  # Specify Opus format
            'preferredquality': '192',
        }],
        'noplaylist': True,
        'quiet': False,
        # 'extract_flat': True,  # This ensures that artist and title are extracted
        # 'postprocessor_args': ['-metadata', f'artist={artist}', '-metadata', f'title={song}'],

    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([search_query])
            print("Download complete.")
        except yt_dlp.DownloadError as e:
            print(f"Error: {e}")


def download_video(artist, song, output_path='./downloads'):
    # Create the search query
    search_query = f'ytsearch:{artist} {song}'

    # Set up options for yt-dlp to download in mp4 format
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'outtmpl': f'{output_path}/{artist} - {song}.%(ext)s',
        'noplaylist': True,
        'quiet': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([search_query])
            print("Download complete.")
        except yt_dlp.DownloadError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    output_path = './downloads/emotion/sad'

    Songs =  ['Ranjha Bichda', 'Tanhaiyyan - A LOVE BALLAD', 'Main Nahi Hoon', 'Barbaad', 'Lambi Judaai 2.0', 'Jhoota Tera Pyar', 'Tujhe Yaad Na Meri Ayee - 2', 'Kalleyan', 'Faasla', 'Sun Ranjheya', 'Nindiya', 'Kya Loge Tum', 'Ek Hi Toh Dil', 'Lost', 'Zohrajabeen', 'Haaye Dard', 'Yaad Aati Hai', 'Filhall', 'Baarish Ki Jaaye', 'Tauba Meri Tauba', 'Tubhi Royega', 'Jaana', 'Aate Rehte Hain', 'Tu Kaun Hai', 'Toot Jaaun', 'Tabah Kar Gaye', 'Tere Pyar Mein (feat. Vineet Raina & Alisha Panwar)', 'Rootha Re', 'Filhaal2 Mohabbat', 'Bidaai', 'Pyaar Karte Ho Na', 'Bairagi Mann', 'Maar Sutteya', 'Duur', 'Dil Todta Hai', 'Manzoor', 'Duniya', 'Theherjaa', 'Mila Na Dil Ko', 'Das Ki Kasoor', 'Saadgi To Hamari', 'Alvida', 'Yaad', 'Chalo Theek Hai', 'Dil Sambhalta Nahin', 'Kuch Tumhara Kuch Hamara', 'Baarishon Mein', 'Muskuraa Lena Tum', 'Ro Rahi Hu', 'Woh Tere Pyar Ka Gham', 'Kahin Na Lage', 'Iss Baarish Mein Unplugged By Yasser Desai', 'Mubarak Ho', 'Dhokhha', 'Hayaa', 'Darbadar', 'Kashmakash', 'Raah Dikha De', 'Tenu Aunda Nahi', 'Maaf Nahi Karega', 'Ishq Samundar', 'Kajal', 'Alvida', 'Minnatein', 'Ishq Ki Baarish', 'Tujhe Chaahta Hoon Kyun', 'Jaana Hai Toh Jaa', 'Kirdaar, Episode 2', 'Tutt Gaya', 'Namonishan', 'Bewafa', 'Dil Toota Hi Raha', 'Arsaa', 'HeartWoken', 'Maan Le (From "Chitrakut")', 'Jo Hoga Accha Hoga, Episode 1', 'Saasein Thami Hai (From "Damned Graveyard")', 'Bechari', 'Kayi Din Huye', 'Kya Kar Diya', 'Dhokebaaz', 'Jee Lenge Hum', 'The Fall', 'Jaa Rahe Ho', 'Dua Karo', 'Yeh Kyun Kiya', 'Saamna', 'Main Royaan', 'Yaad Aati Nahin', 'Tere Bin Jeena Kya', 'Mitra Re', 'Ishq Nahi Karte', 'Ek Tu Hi Toh Hai', 'Shayad', 'Kabhii Tumhhe', 'Rihaayi De', 'Mehrama', 'Main Tumhara', 'Pyaar Toh Tha', 'Tujhe Yaad Badi Aaungi']
    Artists =  ['Stebin Ben, Nilesh Ahuja, Kumaar', 'Shaan', 'Ali Zafar', 'Laqshay Kapoor, Gourov Dasgupta, Kunaal Vermaa', 'Shilpa Joshi', 'Rahat Fateh Ali Khan', 'B Praak, Jaani, Jatin-Lalit', 'AKASA, Taaruk', 'Darshan Raval, Shirley Setia', 'Goldie Sohel', 'Sanchit Balhara, Ankit Balhara, Supriyaa Pathak, Atharv Bakshi, Kausar Munir', 'B Praak, Jaani, Akshay Kumar', 'Raman Romana, Hiten, Dilwala', 'Pranav Chandran', 'B Praak, Jaani', 'Darshan Raval', 'Harrdy Sandhu, Abhishek Singh', 'B Praak', 'B Praak, Nawazuddin Siddiqui, Sunanda Sharma', 'Mamta Sharma', 'Crown J', 'Jay Bhattacharya', 'B Praak, Jaani', 'Shadow And Light, Salim Merchant, Pavithra Chari', 'Anmol Daniel', 'Altamash Faridi', 'Krishna Beura, Vineet Raina, Alisha Panwar', 'Romy, Madhubanti Bagchi, Vivek Hariharan', 'B Praak, Akshay Kumar, Nupur Sanon, Ammy Virk', 'Yashita Sharma', 'Javed-Mohsin, Stebin Ben, Shreya Ghoshal', 'Shaan', 'Gajendra Verma, Flipsyde', 'Kasyap', 'Piyush Ambhore', 'Dev Arijit', 'B Praak, Sunny Singh', 'Raveena Paul', 'Divij Naik', 'Rahul Sathu, Ikka', 'Raj Barman, Raju Das', 'Adnan Sami', 'Shafqat Amanat Ali, Naveed Nashad', 'Amaal Mallik, Kaushal Kishore', 'Alka Yagnik, Daboo Malik', 'Harish Sagane, Soham Naik', 'Darshan Raval', 'Palak Muchhal, Zain Imam, Sana Khan', 'Simar Sethi', 'Amruta Fadnavis', 'Prateek Bajpai', 'Yasser Desai', 'Soham Naik', 'Raj Barman', 'Anurag Mohn', 'Jubin Nautiyal, Vishal Mishra, Raj Shekhar', 'Antara Mitra, Mohammed Irfan', 'Mohit Chauhan, Asees Kaur, Shubham-Ana', 'Prini Siddhant Madhav', 'Simar Sethi', 'King, Arjun Kanungo', 'Shriya Jain, Purabi Bhargava, Utkarsh Gupta', 'Harshavardhan Wavre, Leena Bose', 'Mohammed Irfan', 'Simar Sethi', 'Amaal Mallik, Kunaal Vermaa', 'Siddharth Kasyap, Mohammed Irfan, Kumaar', 'Rahul Jain', 'Stebin Ben', 'Nikhita Gandhi, Shankar Mahadevan ', 'Paras Chopra', 'Mohammed Irfan', 'Amit Mishra, Fukra Insaan', 'Rabbit Sack C', 'Arijit Singh, Somesh Saha', 'Rahul Jain', 'Shahid Mallya', 'Afsana Khan', 'Yasser Desai', 'Vishal Mishra', 'Jaani, Afsana Khan', 'Shaan', 'Jasleen Royal', 'Yasser Desai, Kunaal Vermaa', 'Stebin Ben, Siddharth Kasyap, Kumaar', 'Vishal Mishra', 'AKASA', 'Yasser Desai, Tanveer Evan, Rajat Nagpal', 'Pawan Singh, Salim-Sulaiman', 'Vishal Mishra, Rupali Jagga', 'Arijit Singh, Jasleen Royal', 'B Praak', 'Stebin Ben, Aman Pant', 'Pritam, Arijit Singh', 'Darshan Raval, Javed-Mohsin', 'A. R. Rahman', 'Pritam, Darshan Raval, Antara Mitra', 'Jonita Gandhi, Hriday Gattani, A. R. Rahman', 'Sachin-Jigar, Jubin Nautiyal, Asees Kaur', 'Palak Muchhal']
    
    print("Songs count: " + str(len(Songs)))
    print("Artist count: " + str(len(Artists)))

    for song, artist in zip(Songs, Artists):
        print(artist.split(", ")[0]+" - " + song)
        download_music(artist.split(', ')[0], song, output_path)

    # song_list =[('Gulabi Sharara', 'Inder Arya'), ('Cream Paudara Mashakbeen Uttrakhandi', 'Maya Upadhyay'), ('Dhai Hathe Dhameli Mashakbeen ( Feat. Manoj Arya, Priyanka Meher )', 'Manoj Arya, Priyanka Meher'), ('Hey Madhu Mashakbeen', 'Inder Arya'), ('Mathu Mathu Uttrakhandi', 'Inder Arya, Jyoti Arya'), ('Aawa Dida Bhulo...Thando Re Thando', 'Narendra Singh Negi'), ('Inder Arya', 'Mero Lehanga'), ('Nazar Na Lago Pahadi', 'Inder Arya'), ('Modern Kumaun Pahadi', 'Inder Arya'), ('Kamar Pida', '-'), ('Thando Re Thando', 'Meena Rana, Narendra Singh Negi, Anuradha Nirala'), ('Mera Dandi Kanthiyon Ka Muluk', 'Meena Rana, Narendra Singh Negi'), ('Sapna Syali Garhwali DJ Song', 'Saurav Maithani, Anisha Ranghar, Sanjay Bhandari, Raj Tiger'), ('Dyo Lagi', 'Gunjan Dangwal, Vivek Nautiyal'), ('Fyonladiya Twe Dekhik', 'Kishan Mahipal'), ('Bol Heera', 'Inder Arya'), ('Baand Bijora', 'Narendra Singh Negi'), ('Balma', 'Sanjay Kumola, Meena Rana'), ('Hafta Me 2.0 (Uttrakhandi)', 'Inder Arya, Meena Rana'), ('Jhumki', 'Darshan Farswan'), ('Pyari Nirmala', 'Saurav Maithani'), ('Mero Lehenga 2', 'Inder Arya, Jyoti Arya'), ('Saniyo Ma', 'Sanjay Kumola, Meena Rana, Ajay Solanki'), ('Mashakbeena Mashakbeen (Uttrakhandi)', 'Meena Rana'), ('Rajula (Feat. Inder Arya)', 'Inder Arya'), ('Nandre Tu', 'Rohit Chauhan'), ('Surju', 'Sanjay Kumola, Meena Rana'), ('Shiv Jatadhari Bhairav', 'Darshan Farswan'), ('Mathu Mathu Hitali Meri Bana Uttrakhandi', 'Jitendra Tomkyal'), ('Tera Nakhra', 'Rohit Chauhan'), ('Gajra', 'Sanjay Bhandari, Anisha Ranghar'), ('Heera Samdhini', 'Gajender Rana'), ('Ghuguti Ghuron Laigi', 'Meena Rana, Narendra Singh Negi'), ('Lehenga 4', 'Inder Arya, Mamta Arya'), ('Bedu Pako Baramasa', 'Meena Rana, Manglesh Dangwal, Janardan Prasad Nautiyal, Mukesh Kathait'), ('Lehenga 3 Kumauni album', 'Jyoti Arya, Inder Arya'), ('Santu Chori', 'Gajendra Rana'), ('Lehenga 3', 'Inder Arya, Jyoti Arya'), ('Meri Bhanuli', 'Inder Arya'), ('Bol Heera 2', 'Inder Arya, Jyoti Arya'), ('Main Chun Nauni Pauri Ki', 'Anisha Ranghar, Raj Tiger'), ('Bangaal Choori', 'Kishan Mahipal'), ('Chaita Ki Chaitwala (Jaagar)', 'Chandra Singh Rahi'), ('Insta Baand', 'Vijay Prakash'), ('Meri Jogni', 'Mohan Bisht, Anisha Ranghar'), ('Mohini', 'Rohit Chauhan'), ('Hit Madhuli 2', 'Inder Arya'), ('Thando Re Thando', 'Instrumental'), ('Rangeela Dupatta', 'Keshar Panwar, Anisha Ranghar'), ('Laadi Chandra', 'Anisha Ranghar, Sanjay Bhandari'), ('Garhwal Ki Daandi Kaathi', '-')]
    # for i in song_list:
    #     download_music(i[1], i[0],output_path)
