str ="""Gulabi Sharara
Inder Arya

Cream Paudara Mashakbeen Uttrakhandi
Maya Upadhyay

Dhai Hathe Dhameli Mashakbeen ( Feat. Manoj Arya, Priyanka Meher )
Manoj Arya, Priyanka Meher

Hey Madhu Mashakbeen
Inder Arya

Mathu Mathu Uttrakhandi
Inder Arya, Jyoti Arya

Aawa Dida Bhulo...Thando Re Thando
Narendra Singh Negi
 
Inder Arya
Mero Lehanga

Nazar Na Lago Pahadi
Inder Arya

Modern Kumaun Pahadi
Inder Arya

Kamar Pida
-

Thando Re Thando
Meena Rana, Narendra Singh Negi, Anuradha Nirala

Mera Dandi Kanthiyon Ka Muluk
Meena Rana, Narendra Singh Negi

Sapna Syali Garhwali DJ Song
Saurav Maithani, Anisha Ranghar, Sanjay Bhandari, Raj Tiger

Dyo Lagi
Gunjan Dangwal, Vivek Nautiyal

Fyonladiya Twe Dekhik
Kishan Mahipal

Bol Heera
Inder Arya

Baand Bijora
Narendra Singh Negi

Balma
Sanjay Kumola, Meena Rana

Hafta Me 2.0 (Uttrakhandi)
Inder Arya, Meena Rana

Jhumki
Darshan Farswan

Pyari Nirmala
Saurav Maithani

Mero Lehenga 2
Inder Arya, Jyoti Arya

Saniyo Ma
Sanjay Kumola, Meena Rana, Ajay Solanki

Mashakbeena Mashakbeen (Uttrakhandi)
Meena Rana

Rajula (Feat. Inder Arya)
Inder Arya

Nandre Tu
Rohit Chauhan

Surju
Sanjay Kumola, Meena Rana

Shiv Jatadhari Bhairav
Darshan Farswan

Mathu Mathu Hitali Meri Bana Uttrakhandi
Jitendra Tomkyal

Tera Nakhra
Rohit Chauhan

Gajra
Sanjay Bhandari, Anisha Ranghar

Heera Samdhini
Gajender Rana

Ghuguti Ghuron Laigi
Meena Rana, Narendra Singh Negi

Lehenga 4
Inder Arya, Mamta Arya

Bedu Pako Baramasa
Meena Rana, Manglesh Dangwal, Janardan Prasad Nautiyal, Mukesh Kathait

Lehenga 3 Kumauni album
Jyoti Arya, Inder Arya

Santu Chori
Gajendra Rana

Lehenga 3
Inder Arya, Jyoti Arya

Meri Bhanuli
Inder Arya

Bol Heera 2
Inder Arya, Jyoti Arya

Main Chun Nauni Pauri Ki
Anisha Ranghar, Raj Tiger

Bangaal Choori
Kishan Mahipal

Chaita Ki Chaitwala (Jaagar)
Chandra Singh Rahi

Insta Baand
Vijay Prakash

Meri Jogni
Mohan Bisht, Anisha Ranghar

Mohini
Rohit Chauhan

Hit Madhuli 2
Inder Arya

Thando Re Thando
Instrumental

Rangeela Dupatta
Keshar Panwar, Anisha Ranghar

Laadi Chandra
Anisha Ranghar, Sanjay Bhandari

Garhwal Ki Daandi Kaathi
-"""

t = str.split("\n")
# print(t)
songs = []
for i in range(0,51*3,3):
    t1 = (t[i],t[i+1])
    songs.append(t1)
print(len(songs))
print(songs)
