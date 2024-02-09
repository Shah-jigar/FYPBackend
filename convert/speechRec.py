
audio_file = "./Abhijeet Srivastava - Chashni (From Bharat).wav"


import speech_recognition as sr

def convert_audio_to_text(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data, language='hi-IN')
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Error with the API request; {e}")
        return None

# Replace 'your_audio_file.wav' with the path to your Hindi audio file
audio_file_path = "./songs/Romantic_301.wav"
result = convert_audio_to_text(audio_file_path)

if result:
    print("Hindi Lyrics:")
    print(result)
