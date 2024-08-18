import openai

from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file_path = r"C:\Users\PythonProjects\pycode\tts_story2.mp3"
with open(audio_file_path, 'rb') as audio_file:
    # Call the Whisper API to transcribe the audio file
    response = openai.Audio.transcribe(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )

# Save the transcription to a text file
#with open('transcription.txt', 'w') as text_file:
#    text_file.write(response)

# Print the transcription
print(response)
