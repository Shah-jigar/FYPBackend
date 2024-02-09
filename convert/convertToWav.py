"./Abhijeet Srivastava - Chashni (From Bharat).opus"

import os
# opus_path = "./Abhijeet Srivastava - Chashni (From Bharat).opus"
opus_path = "./opus/Anup Jalota - Ae Malik Tere Bande Hum.opus"
wav_path = 'Anup Jalota - Ae Malik Tere Bande Hum.wav'
os.system(f'ffmpeg -i "{opus_path}" -vn "{wav_path}"')