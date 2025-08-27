# 🤖 AI Medical Assistant with Vision and Voice

This project is a proof-of-concept application that simulates a medical consultation using a multimodal AI. Users can ask questions with their voice and upload a medical image (like a skin condition). The AI analyzes both the voice query and the image to provide a suggestion, which is then spoken back to the user.

---
## ✨ Key Features

-   **Voice-to-Text:** Uses the Whisper model via the Groq API for real-time speech recognition.
-   **Multimodal Analysis:** Employs the LLaVA vision-language model to understand both text and images simultaneously.
-   **Text-to-Speech:** Leverages the ElevenLabs API to convert the AI's response into natural-sounding speech.
-   **Interactive UI:** Built with Gradio for a simple and user-friendly web interface.

---
## 🛠️ Tech Stack

-   **Language:** Python
-   **APIs & Models:** Groq (LLaVA, Whisper), ElevenLabs API
-   **Libraries:** Gradio, Pydub, SoundDevice
-   **Environment:** Pipenv

---
## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Ayushman-Johri/AI-Medical-Assistant.git](https://github.com/Ayushman-Johri/AI-Medical-Assistant.git)
    cd AI-Medical-Assistant
    ```
2.  **Install dependencies using Pipenv:**
    ```bash
    pipenv install
    ```
3.  **Create a `.env` file** in the root directory and add your API keys:
    ```
    GROQ_API_KEY="your_groq_api_key"
    ELEVENLABS_API_KEY="your_elevenlabs_api_key"
    ```
4.  **Run the application:**
    ```bash
    pipenv run python gradio_app.py
    ```
