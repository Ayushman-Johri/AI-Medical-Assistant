# # if you dont use pipenv uncomment the following:
# # from dotenv import load_dotenv
# # load_dotenv()

# #Step1a: Setup Text to Speech–TTS–model with gTTS
# import os
# from gtts import gTTS

# def text_to_speech_with_gtts_old(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)


# input_text="Hi this is Ai with Hassan!"
# text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

# #Step1b: Setup Text to Speech–TTS–model with ElevenLabs
# import elevenlabs
# from elevenlabs.client import ElevenLabs

# ELEVENLABS_API_KEY=os.environ.get("ELEVEN_API_KEY")

# def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
#     client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio=client.text_to_speech.convert(
#         text= input_text,
#         voice= "Aria",
#         output_format= "mp3_22050_32",
#         model= "eleven_turbo_v2"
#     )
#     elevenlabs.save(audio, output_filepath)

# #text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 

# #Step2: Use Model for Text output to Voice

# import subprocess
# import platform

# def text_to_speech_with_gtts(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")


# input_text="Hi this is Ai with Hassan, autoplay testing!"
# #text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")


# def text_to_speech_with_elevenlabs(input_text, output_filepath):
#     client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio=client.generate(
#         text= input_text,
#         voice= "Aria",
#         output_format= "mp3_22050_32",
#         model= "eleven_turbo_v2"
#     )
#     elevenlabs.save(audio, output_filepath)
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")

# #text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")
# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

# -------------------------
# Step1a: Setup gTTS
# -------------------------
# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#Step1a: Setup Text to Speech–TTS–model with gTTS
# import os
# from gtts import gTTS

# def text_to_speech_with_gtts_old(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)


# input_text="Hi this is Ai with Hassan!"
# text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

# #Step1b: Setup Text to Speech–TTS–model with ElevenLabs
# from elevenlabs import ElevenLabs

# ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")  # ✅ fixed (was ELEVEN_API_KEY)

# def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
#     client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     with open(output_filepath, "wb") as f:
#         response = client.text_to_speech.convert(
#             voice_id="pNInz6obpgDQGcFmaJgB",  # ✅ replace with your voice ID
#             model_id="eleven_multilingual_v2",
#             output_format="mp3_44100_128",
#             text=input_text
#         )
#         for chunk in response:
#             f.write(chunk)

# #text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 

# #Step2: Use Model for Text output to Voice

# import subprocess
# import platform

# def text_to_speech_with_gtts(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")


# input_text="Hi this is Ai with Hassan, autoplay testing!"
# #text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")


# def text_to_speech_with_elevenlabs(input_text, output_filepath):
#     client = ElevenLabs(api_key="sk_f9c337f9ffdbe28e791dcce210446b94098e20080d549fa8")
#     with open(output_filepath, "wb") as f:
#         response = client.text_to_speech.convert(
#             voice_id="pNInz6obpgDQGcFmaJgB",  # ✅ replace with your voice ID
#             model_id="eleven_multilingual_v2",
#             output_format="mp3_44100_128",
#             text=input_text
#         )
#         for chunk in response:
#             f.write(chunk)

#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")

# #text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")
# import os
# from elevenlabs import ElevenLabs
# from pydub import AudioSegment  # Yeh import zaroori hai

# # API Key .env file se automatically load ho jayegi
# ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

# def text_to_speech_with_elevenlabs(input_text, output_filepath="audio_output"):
#     """
#     Generates speech from text using ElevenLabs, saves it as an MP3,
#     converts it to WAV, and returns the path to the WAV file.
#     """
#     client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
#     # File paths define karein
#     mp3_path = f"{output_filepath}.mp3"
#     wav_path = f"{output_filepath}.wav"

#     # Step 1: ElevenLabs se MP3 generate karein
#     with open(mp3_path, "wb") as f:
#         response = client.text_to_speech.convert(
#             voice_id="pNInz6obpgDQGcFmaJgB",
#             model_id="eleven_multilingual_v2",
#             output_format="mp3_44100_128",
#             text=input_text
#         )
#         for chunk in response:
#             f.write(chunk)
    
#     print(f"MP3 audio saved to: {mp3_path}")

#     # Step 2: MP3 ko WAV mein convert karein
#     try:
#         audio = AudioSegment.from_mp3(mp3_path)
#         audio.export(wav_path, format="wav")
#         print(f"WAV audio saved to: {wav_path}")
#     except Exception as e:
#         print(f"Error converting MP3 to WAV: {e}")
#         return None

#     # Step 3: WAV file ka path return karein
#     return wav_path
# voice_of_doctor.py
import os
from elevenlabs import ElevenLabs
from pydub import AudioSegment

def text_to_speech_with_elevenlabs(input_text, output_filepath="audio_output"):
    """
    Generates speech from text using ElevenLabs, saves it as an MP3,
    converts it to WAV, and returns the path to the WAV file.
    """
    client = ElevenLabs(api_key=os.environ.get("ELEVENLABS_API_KEY"))
    
    mp3_path = f"{output_filepath}.mp3"
    wav_path = f"{output_filepath}.wav"

    with open(mp3_path, "wb") as f:
        response = client.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
            text=input_text
        )
        for chunk in response:
            f.write(chunk)
    
    print(f"MP3 audio saved to: {mp3_path}")

    try:
        audio = AudioSegment.from_mp3(mp3_path)
        audio.export(wav_path, format="wav")
        print(f"WAV audio saved to: {wav_path}")
    except Exception as e:
        print(f"Error converting MP3 to WAV: {e}")
        return None

    return wav_path