import subprocess
import os
import math
import speech_recognition as sr

# Function to get the duration of the audio file
def get_audio_duration(file_path):
    result = subprocess.run(['ffprobe', '-i', file_path, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")], capture_output=True)
    return float(result.stdout)

# Function to split the audio file into segments
def split_audio(file_path, segment_duration):
    subprocess.run(["ffmpeg", "-i", file_path, "-f", "segment", "-segment_time", str(segment_duration), "-c", "copy", "segment_%03d.wav"])

# Function to transcribe each segment
def transcribe_segments(num_segments):
    recognizer = sr.Recognizer()
    transcripts = []

    for i in range(1, num_segments + 1):
        segment_file = f"segment_{i:03d}.wav"
        if not os.path.exists(segment_file):
            transcripts.append("Segment not found")
            continue
        
        with sr.AudioFile(segment_file) as source:
            audio_data = recognizer.record(source)  # Read the entire audio file

        # Perform speech recognition
        try:
            transcript = recognizer.recognize_google(audio_data)
            transcripts.append(transcript)
        except sr.UnknownValueError:
            transcripts.append("Speech recognition could not understand audio")
        except sr.RequestError as e:
            transcripts.append("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return transcripts

# Main function to transcribe audio file
def transcribe_audio(file_path, segment_duration):
    # Step 1: Convert Opus file to WAV format
    subprocess.run(["ffmpeg", "-i", file_path, "-c:a", "pcm_s16le", "-ar", "16000", "-ac", "1", "converted_audio.wav"])

    # Step 2: Split the audio file into segments
    split_audio("converted_audio.wav", segment_duration)
    
    # Step 3: Get the number of segments
    audio_duration = get_audio_duration("converted_audio.wav")
    num_segments = math.ceil(audio_duration / segment_duration)
    
    # Step 4: Transcribe each segment
    transcripts = transcribe_segments(num_segments)
    
    # Step 5: Combine the transcripts
    final_transcript = " ".join(transcripts)
    return final_transcript

# Example usage
audio_file_path = "C:\Projects\python\FYPBackend\downloads\genre\Garhwali\Anil - Jawa Pardesh.opus"
segment_duration = 30  # 5 minutes
transcript = transcribe_audio(audio_file_path, segment_duration)
print("Final Transcript:", transcript)
