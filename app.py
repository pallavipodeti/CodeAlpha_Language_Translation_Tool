import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile
import pyperclip

st.set_page_config(page_title="Language Translation Tool", page_icon="🌍")

st.title("🌍 Language Translation Tool")
st.write("Translate text between multiple languages")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

text = st.text_area("Enter Text to Translate")

source_lang = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target_lang = st.selectbox(
    "Target Language",
    list(languages.keys())
)

if st.button("Translate"):
    if text.strip():

        translated_text = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("Translation Successful")

        st.subheader("Translated Text")
        st.text_area(
            "Output",
            translated_text,
            height=150
        )

        # Copy Button
        if st.button("📋 Copy Translation"):
            pyperclip.copy(translated_text)
            st.success("Copied to Clipboard!")

        # Text To Speech
        st.subheader("🔊 Listen to Translation")

        tts = gTTS(
            text=translated_text,
            lang=languages[target_lang].split("-")[0]
        )

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)

            audio_file = open(fp.name, "rb")
            st.audio(audio_file.read(), format="audio/mp3")

    else:
        st.warning("Please enter some text.")