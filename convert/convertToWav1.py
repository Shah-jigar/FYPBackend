# Works well but not all lines of song are being picked up by listener

# Import libraries
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Create a speech recognition object
r = sr.Recognizer()

def transcribe_large_audio(path):
    """Split audio into chunks and apply speech recognition"""
    # Open audio file with pydub
    sound = AudioSegment.from_wav(path)

    # Split audio where silence is 700ms or greater and get chunks
    chunks = split_on_silence(sound, min_silence_len=650, silence_thresh=sound.dBFS-10, keep_silence=700)
    
    # Create folder to store audio chunks
    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    
    whole_text = ""
    # Process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # Export chunk and save in folder
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")

        # Recognize chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # Convert to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print(f"Error recognizing audio in {chunk_filename}: {str(e)}")
            except sr.RequestError as e:
                print(f"Google API request failed in {chunk_filename}: {str(e)}")

            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text

    # Return text for all chunks
    return whole_text




result = transcribe_large_audio('something.wav')

print(result)
print(result, file=open('result.txt', 'w'))