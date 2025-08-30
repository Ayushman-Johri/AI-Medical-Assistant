# # if you dont use pipenv uncomment the following:
# # from dotenv import load_dotenv
# # load_dotenv()

# #VoiceBot UI with Gradio
# import os
# import gradio as gr

# from brain_of_doctor import encode_image, analyze_image_with_query
# from voice_of_patient import record_audio, transcribe_with_groq
# from voice_of_doctor import text_to_speech_with_gtts, text_to_speech_with_elevenlabs

# #load_dotenv()

# system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
#             What's in this image?. Do you find anything wrong with it medically? 
#             If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
#             your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
#             Donot say 'In the image I see' but say 'With what I see, I think you have ....'
#             Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
#             Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


# def process_inputs(audio_filepath, image_filepath):
#     speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
#                                                  audio_filepath=audio_filepath,
#                                                  stt_model="whisper-large-v3")

#     # Handle the image input
#     if image_filepath:
#         doctor_response = analyze_image_with_query(query=system_prompt+speech_to_text_output, encoded_image=encode_image(image_filepath), model="meta-llama/llama-4-scout-17b-16e-instruct") #model="meta-llama/llama-4-maverick-17b-128e-instruct") 
#     else:
#         doctor_response = "No image provided for me to analyze"

#     voice_of_doctor = text_to_speech_with_elevenlabs(input_text=doctor_response, output_filepath="final.mp3") 

#     return speech_to_text_output, doctor_response, voice_of_doctor


# # Create the interface
# iface = gr.Interface(
#     fn=process_inputs,
#     inputs=[
#         gr.Audio(sources=["microphone"], type="filepath"),
#         gr.Image(type="filepath")
#     ],
#     outputs=[
#         gr.Textbox(label="Speech to Text"),
#         gr.Textbox(label="Doctor's Response"),
#         gr.Audio(type="filepath", label="Doctor's Voice")  # ✅ fixed
#     ],
#     title="AI Doctor with Vision and Voice"
# )

# iface.launch(debug=True)

# #http://127.0.0.1:7860
# import os
# import gradio as gr

# from brain_of_doctor import encode_image, analyze_image_with_query
# from mic_test import transcribe_with_groq 
# from voice_of_doctor import text_to_speech_with_elevenlabs

# # Pipenv .env file ko automatically load kar lega

# system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
#             What's in this image?. Do you find anything wrong with it medically? 
#             If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
#             your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
#             Donot say 'In the image I see' but say 'With what I see, I think you have ....'
#             Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
#             Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


# def process_inputs(audio_filepath, image_filepath):
#     # ✅ FIX 1: Check if inputs are provided.
#     if audio_filepath is None or image_filepath is None:
#         return "Error: Missing Input", "Please record your audio and upload an image.", None

#     # Step 1: Patient ki voice ko text mein convert karein
#     stt_output = transcribe_with_groq(stt_model="whisper-large-v3", 
#                                       audio_filepath=audio_filepath,
#                                       GROQ_API_KEY=os.environ.get("GROQ_API_KEY"))

#     # Step 2: Image ko analyze karein aur doctor ka response generate karein
#     doctor_response_text = analyze_image_with_query(
#         query=system_prompt + stt_output, 
#         encoded_image=encode_image(image_filepath), 
#         # ✅ FIX 2: Use a vision model that can see images.
#         model="meta-llama/llama-4-scout-17b-16e-instruct" 
#     )

#     # Step 3: Doctor ke response ko voice mein convert karein (WAV format mein)
#     doctor_voice_path = text_to_speech_with_elevenlabs(
#         input_text=doctor_response_text, 
#         output_filepath="doctor_response_audio"
#     ) 

#     return stt_output, doctor_response_text, doctor_voice_path


# # Gradio Interface banayein
# iface = gr.Interface(
#     fn=process_inputs,
#     inputs=[
#         gr.Audio(sources=["microphone"], type="filepath", label="Patient's Voice Query"),
#         gr.Image(type="filepath", label="Upload Medical Image")
#     ],
#     outputs=[
#         gr.Textbox(label="Patient's Query (Speech-to-Text)"),
#         gr.Textbox(label="Doctor's Text Response"),
#         gr.Audio(type="filepath", label="Doctor's Voice Response (WAV)")
#     ],
#     title="AI Doctor with Vision and Voice",
#     description="Record your health query and upload an image. The AI doctor will respond in text and voice."
# )

# iface.launch(debug=True)
# app.py
import os
import gradio as gr

from brain_of_doctor import encode_image, analyze_image_with_query
# Note: Ensure you have a working transcribe_with_groq function in one of your files.
# I am assuming it's in voice_of_patient.py as per our previous discussion.
from voice_of_patient import transcribe_with_groq
from voice_of_doctor import text_to_speech_with_elevenlabs

system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


def process_inputs(audio_filepath, image_filepath):
    if audio_filepath is None or image_filepath is None:
        return "Error: Missing Input", "Please record your audio and upload an image.", None

    try:
        stt_output = transcribe_with_groq(stt_model="whisper-large-v3", 
                                          audio_filepath=audio_filepath,
                                          GROQ_API_KEY=os.environ.get("GROQ_API_KEY"))

        doctor_response_text = analyze_image_with_query(
            query=system_prompt + stt_output, 
            encoded_image=encode_image(image_filepath), 
            model="meta-llama/llama-4-scout-17b-16e-instruct" 
        )

        doctor_voice_path = text_to_speech_with_elevenlabs(
            input_text=doctor_response_text, 
            output_filepath="doctor_response_audio"
        ) 

        return stt_output, doctor_response_text, doctor_voice_path
    
    except Exception as e:
        print(f"An error occurred in process_inputs: {e}")
        return "Error", f"An internal error occurred: {e}", None


iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="Patient's Voice Query"),
        gr.Image(type="filepath", label="Upload Medical Image")
    ],
    outputs=[
        gr.Textbox(label="Patient's Query (Speech-to-Text)"),
        gr.Textbox(label="Doctor's Text Response"),
        gr.Audio(type="filepath", label="Doctor's Voice Response (WAV)")
    ],
    title="AI Doctor with Vision and Voice",
    description="Record your health query and upload an image. The AI doctor will respond in text and voice."
)

iface.launch()