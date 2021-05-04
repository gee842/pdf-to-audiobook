
from google.cloud import texttospeech
import json
import random
import os
import re


def comment_to_mp3(input_text, FILEPATH_QUOTA,POST_ID,voice='en-US-Wavenet-H'):
    num_of_chars = len(input_text)

    with open(FILEPATH_QUOTA, 'r') as f:
        line = f.readline()
        quota_remaining = int(line)
        if quota_remaining < num_of_chars+100:
            raise Exception("Quota depleted :(")
    

    selected_voice = voice
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=input_text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
        name=selected_voice
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(FILEPATH_QUOTA, 'w') as f:
        quota_remaining -= num_of_chars
        print(f"-----QUOTA REMAINING: {quota_remaining}-----")
        f.write(str(quota_remaining))

    with open(f"./{POST_ID}.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print(f'Audio content written to file "{POST_ID}.mp3"')



if __name__ == '__main__':
    text = open('./newconverted.txt','r')
    fulltext = text.read()
    text.close()
    quota_path = './quota.txt'
    truncated_text = fulltext[1:1000]
    comment_to_mp3(truncated_text,quota_path,f'part1',voice="en-GB-Wavenet-B")