"./Abhijeet Srivastava - Chashni (From Bharat).opus"

import os
# opus_path = "./Abhijeet Srivastava - Chashni (From Bharat).opus"
opus_path = "downloads\genre\Garhwali\Anil - Chakdait Chhora.opus"
wav_path = 'something.wav'
os.system(f'ffmpeg -i "{opus_path}" -vn "{wav_path}"')