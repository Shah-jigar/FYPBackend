# Download songs from youtube

import yt_dlp

def download_music(artist, song, output_path='./downloads/gharwali'):
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

if __name__ == "__main__":
    # songs = ['Hum Bekhudi Mein Tum Ko Pukare', 'Koi Sagar Dil Ko Bahlata Nahin', 'Rang Aur Noor Ki Barat', 'Hui Sham Unka Khayal Aa Gaya', 'Mere Mehboob Kahin Aur', 'Guzre Hain Aaj Ishq Mein Ham', 'Muddat Huyi Hai', 'Diya Yeh Dil Agar Usko', 'Yeh Na Thi Hamari Qismat', 'Nukta Chin Hai', 'Baithe Hain', 'Falsafe Ishq Mein Pesh Aaye Sawalon Ki Tarha', 'Dil Ki Baat Kahi Nahin Jaati', 'Jo Unki Tamanna Hai', 'Haaye Mehamaan Kahan Yeh Gham E Jana Hoga', 'Maine Jab Se Tujhe Aye Jaan E Ghazal', 'Zikar Us Pariwash Ka', 'Dard Minnat Kashe', 'Humko Mita Sake Yeh Zamane Mein Dam Nahin', 'Shauq Har Rang', 'Ek Hi Baat Zamane Ki Kitabon Mein Nahin', 'Ghazab Kiya Tere Waade Pe', 'Bas Ke Dushwar Hai', 'Zindagi Aaj Mere Naam Se', 'Jab Tere Pyarke Afsana', 'Kisi Ki Yaad Mein Payi Hain', 'Tod Do Ahd E Mohabbat', 'Jalwo Waqt', 'Aaj Mere Kareeb', 'Main Deep Jalaye Baitha Hoon', 'Poochh Na Mujh Se', 'Chhalke Teri Ankhon Se', 'Na Kisi Ki Aankh Ka Noor Hoon', 'Jane Kya Dhoondti Rahti Hai', 'Lagta Nahin Dil Mera']
    # artist_name = 'Mohammed Rafi'

    # songs1 = ['Udd Jaa Kaale Kaava (From "Gadar 2")', 'Leke Prabhu Ka Naam (From "Tiger 3")', 'Phir Aur Kya Chahiye (From "Zara Hatke Zara Bachke")', 'Tum Kya Mile (From "Rocky Aur Rani Kii Prem Kahaani")', 'JALSA 2.0', 'Khairiyat (From "Gadar 2")', 'Ruaan (From "Tiger 3")', 'Main Nikla Gaddi Leke (From "Gadar 2")', 'What Jhumka ? (From "Rocky Aur Rani Kii Prem Kahaani")', 'Heeriye (feat. Arijit Singh)', 'Chorni', 'Dil Kya Kare', 'Tu Meri Hai', 'Main Khiladi', 'Habibti (From "Honey 3.0")', 'Jai Ganesha (From "Ganapath")', 'Tere Vaaste (From "Zara Hatke Zara Bachke")', 'Oonchi Oonchi Waadi (From "OMG 2")', '100 Million', 'Yaar Ka Sataya Hua Hai', 'Zihaal e Miskin', 'Dil Haareya', 'Doriyaan', 'Love Like That (feat. Ali Sethi)', 'Hone Do Jo Hota Hai (From "Kho Gaye Hum Kahan")', 'Dastoor', 'Dil Jhoom', 'Ram Dhun', 'Ve Kamleya (From "Rocky Aur Rani Kii Prem Kahaani")', 'Bolo Ram Ram', 'Kya Loge Tum', 'Husn', 'Mahiye Jinna Sohna', 'Jaane Jaan - Title Track (From "Jaane Jaan")', 'Zohrajabeen', 'Siyapati Ram', 'Bairiya', 'Mulaqat', 'Guzarish', 'Laapata', 'In Raahon Mein (From "The Archies")', 'Yahi Toh Hai Zindagi (From "Tarla")', 'Naiyo Lagda', 'Sunoh (From "The Archies")', 'Aadat', 'Saajan Ve', 'Baarish Ke Mausam Mein', 'Billi Billi', 'Tu hai kahan', 'Mera Piya Ghar Aaya 2.0']
    # artists = ['Udit Narayan', 'Pritam', 'Sachin-Jigar', 'Pritam', 'Satinder Sartaaj', 'Arijit Singh', 'Pritam', 'Udit Narayan', 'Pritam', 'Jasleen Royal', 'DIVINE', 'Stebin Ben', 'Jigar Saraiya', 'Udit Narayan', 'Yo Yo Honey Singh', 'Vishal Mishra', 'Sachin-Jigar', 'Hansraj Raghuwanshi', 'DIVINE', 'B Praak', 'Javed-Mohsin', 'Arijit Singh', 'Arijit Singh', 'Jonita Gandhi', 'OAFF', 'Jasleen Royal', 'Mithoon', 'Kailash Kher', 'Pritam', 'Sonu Nigam', 'B Praak', 'Anuv Jain', 'Darshan Raval', 'Sachin-Jigar', 'B Praak', 'Rohin Das', 'Arijit Singh', 'Prateek Kuhad', 'Jonita Gandhi', 'King', 'Arijit Singh', 'Suhit Abhyankar', 'Himesh Reshammiya', 'Ankur Tewari', 'Lisa Mishra', 'Darshan Raval', 'Stebin Ben', 'Sukhbir', 'Aur', 'Neeti Mohan']
    # song_name = 'Main Bhi Shaamil Tha Gunahegaaron Mein'
    # for song in songs:
    #     download_music(artist_name, song)
    # for i in range(0,len(songs)):
    #     download_music(artists[i], songs1[i])

    song_list =[('Gulabi Sharara', 'Inder Arya'), ('Cream Paudara Mashakbeen Uttrakhandi', 'Maya Upadhyay'), ('Dhai Hathe Dhameli Mashakbeen ( Feat. Manoj Arya, Priyanka Meher )', 'Manoj Arya, Priyanka Meher'), ('Hey Madhu Mashakbeen', 'Inder Arya'), ('Mathu Mathu Uttrakhandi', 'Inder Arya, Jyoti Arya'), ('Aawa Dida Bhulo...Thando Re Thando', 'Narendra Singh Negi'), ('Inder Arya', 'Mero Lehanga'), ('Nazar Na Lago Pahadi', 'Inder Arya'), ('Modern Kumaun Pahadi', 'Inder Arya'), ('Kamar Pida', '-'), ('Thando Re Thando', 'Meena Rana, Narendra Singh Negi, Anuradha Nirala'), ('Mera Dandi Kanthiyon Ka Muluk', 'Meena Rana, Narendra Singh Negi'), ('Sapna Syali Garhwali DJ Song', 'Saurav Maithani, Anisha Ranghar, Sanjay Bhandari, Raj Tiger'), ('Dyo Lagi', 'Gunjan Dangwal, Vivek Nautiyal'), ('Fyonladiya Twe Dekhik', 'Kishan Mahipal'), ('Bol Heera', 'Inder Arya'), ('Baand Bijora', 'Narendra Singh Negi'), ('Balma', 'Sanjay Kumola, Meena Rana'), ('Hafta Me 2.0 (Uttrakhandi)', 'Inder Arya, Meena Rana'), ('Jhumki', 'Darshan Farswan'), ('Pyari Nirmala', 'Saurav Maithani'), ('Mero Lehenga 2', 'Inder Arya, Jyoti Arya'), ('Saniyo Ma', 'Sanjay Kumola, Meena Rana, Ajay Solanki'), ('Mashakbeena Mashakbeen (Uttrakhandi)', 'Meena Rana'), ('Rajula (Feat. Inder Arya)', 'Inder Arya'), ('Nandre Tu', 'Rohit Chauhan'), ('Surju', 'Sanjay Kumola, Meena Rana'), ('Shiv Jatadhari Bhairav', 'Darshan Farswan'), ('Mathu Mathu Hitali Meri Bana Uttrakhandi', 'Jitendra Tomkyal'), ('Tera Nakhra', 'Rohit Chauhan'), ('Gajra', 'Sanjay Bhandari, Anisha Ranghar'), ('Heera Samdhini', 'Gajender Rana'), ('Ghuguti Ghuron Laigi', 'Meena Rana, Narendra Singh Negi'), ('Lehenga 4', 'Inder Arya, Mamta Arya'), ('Bedu Pako Baramasa', 'Meena Rana, Manglesh Dangwal, Janardan Prasad Nautiyal, Mukesh Kathait'), ('Lehenga 3 Kumauni album', 'Jyoti Arya, Inder Arya'), ('Santu Chori', 'Gajendra Rana'), ('Lehenga 3', 'Inder Arya, Jyoti Arya'), ('Meri Bhanuli', 'Inder Arya'), ('Bol Heera 2', 'Inder Arya, Jyoti Arya'), ('Main Chun Nauni Pauri Ki', 'Anisha Ranghar, Raj Tiger'), ('Bangaal Choori', 'Kishan Mahipal'), ('Chaita Ki Chaitwala (Jaagar)', 'Chandra Singh Rahi'), ('Insta Baand', 'Vijay Prakash'), ('Meri Jogni', 'Mohan Bisht, Anisha Ranghar'), ('Mohini', 'Rohit Chauhan'), ('Hit Madhuli 2', 'Inder Arya'), ('Thando Re Thando', 'Instrumental'), ('Rangeela Dupatta', 'Keshar Panwar, Anisha Ranghar'), ('Laadi Chandra', 'Anisha Ranghar, Sanjay Bhandari'), ('Garhwal Ki Daandi Kaathi', '-')]
    output_path='./downloads/gharwali'
    for i in song_list:
        download_music(i[1], i[0],output_path)
