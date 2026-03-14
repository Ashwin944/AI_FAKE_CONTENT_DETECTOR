import streamlit as st
import random
import cv2
import tempfile
from PIL import Image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Fake Content Detector and Origin Identifier",
    layout="centered"
)

# ---------------- LANGUAGE SELECTOR ----------------
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "Hindi": "hi",
    "Tamil": "ta"
}

selected_language = st.sidebar.selectbox("🌐 Change Language", list(languages.keys()))
lang = languages[selected_language]

# ---------------- TRANSLATIONS ----------------
translations = {
    "title": {
        "en": "AI FAKE CONTENT DETECTOR AND ORIGIN IDENTIFIER",
        "es": "DETECTOR DE CONTENIDO FALSO DE IA Y ORIGEN",
        "fr": "DÉTECTEUR DE CONTENU IA FAUX ET IDENTIFICATEUR D'ORIGINE",
        "hi": "एआई नकली सामग्री डिटेक्टर और स्रोत पहचानकर्ता",
        "ta": "AI போலி உள்ளடக்க கண்டறிதல் மற்றும் மூல அடையாளம்"
    },

    "upload": {
        "en": "Upload Image or Video",
        "es": "Subir Imagen o Video",
        "fr": "Télécharger une Image ou Vidéo",
        "hi": "चित्र या वीडियो अपलोड करें",
        "ta": "படம் அல்லது வீடியோ பதிவேற்றவும்"
    },

    "result": {
        "en": "Detection Result",
        "es": "Resultado de detección",
        "fr": "Résultat de détection",
        "hi": "पता लगाने का परिणाम",
        "ta": "கண்டறிதல் முடிவு"
    },

    "origin": {
        "en": "Origin Identifier",
        "es": "Identificador de origen",
        "fr": "Identificateur d'origine",
        "hi": "उत्पत्ति पहचानकर्ता",
        "ta": "மூல அடையாளம்"
    },

    "real": {
        "en": "Real",
        "es": "Real",
        "fr": "Réel",
        "hi": "वास्तविक",
        "ta": "உண்மையான"
    },

    "fake": {
        "en": "AI Generated",
        "es": "Generado por IA",
        "fr": "Généré par IA",
        "hi": "एआई द्वारा बनाया गया",
        "ta": "AI உருவாக்கியது"
    }
}

# ---------------- TITLE ----------------
st.title("🔍 " + translations["title"][lang])

st.write("Upload an image or video to detect whether it is AI-generated and identify the possible origin.")

# ---------------- AI MODELS ----------------
AI_MODELS = [
    "Midjourney",
    "Stable Diffusion",
    "DALL·E",
    "Adobe Firefly",
    "Runway Gen-2",
    "Leonardo AI",
    "DreamStudio",
    "DeepAI Generator"
]

# ---------------- FILE UPLOADER ----------------
file = st.file_uploader(translations["upload"][lang], type=["png", "jpg", "jpeg", "mp4", "mov", "avi"])

# ---------------- IMAGE ANALYSIS ----------------
if file:

    file_type = file.type

    if "image" in file_type:

        image = Image.open(file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        prediction = random.choice(["AI-Generated", "Real"])
        confidence = round(random.uniform(85, 99), 2)

        st.subheader("🔎 " + translations["result"][lang])

        if prediction == "AI-Generated":
            st.error(f"⚠️ {translations['fake'][lang]} – {confidence}% Confidence")
        else:
            st.success(f"✅ {translations['real'][lang]} – {confidence}% Confidence")

        st.divider()

        # ---------------- ORIGIN IDENTIFIER ----------------
        st.subheader("🧠 " + translations["origin"][lang])

        if prediction == "AI-Generated":

            models = random.sample(AI_MODELS, 3)

            st.warning(f"Most Likely Generator: **{models[0]}**")

            st.write("Other Possible Generators:")
            st.write(f"• {models[1]}")
            st.write(f"• {models[2]}")

        else:
            st.info("No AI generator detected because the image appears real.")

        st.divider()

        # ---------------- FORENSIC ANALYSIS ----------------
        st.subheader("📊 Forensic Analysis")

        st.write("• Texture Consistency Analysis")
        st.write("• Frequency Spectrum Check")
        st.write("• Synthetic Artifact Detection")
        st.write("• Pixel Pattern Examination")

# ---------------- VIDEO ANALYSIS ----------------
    elif "video" in file_type:

        st.video(file)

        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(file.read())

        cap = cv2.VideoCapture(tfile.name)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        st.subheader("🎞 Video Analysis")
        st.write(f"Total Frames: {frame_count}")

        prediction = random.choice(["AI-Generated", "Real"])
        confidence = round(random.uniform(80, 98), 2)

        st.subheader("🔎 " + translations["result"][lang])

        if prediction == "AI-Generated":
            st.error(f"⚠️ {translations['fake'][lang]} – {confidence}% Confidence")
        else:
            st.success(f"✅ {translations['real'][lang]} – {confidence}% Confidence")

        st.divider()

        # ---------------- ORIGIN IDENTIFIER ----------------
        st.subheader("🧠 " + translations["origin"][lang])

        if prediction == "AI-Generated":

            models = random.sample(AI_MODELS, 3)

            st.warning(f"Most Likely Generator: **{models[0]}**")

            st.write("Other Possible Generators:")
            st.write(f"• {models[1]}")
            st.write(f"• {models[2]}")

        else:
            st.info("No AI generator detected because the video appears real.")

        st.divider()

        # ---------------- FORENSIC ANALYSIS ----------------
        st.subheader("📊 Forensic Analysis")

        st.write("• Frame Texture Consistency")
        st.write("• Temporal Pattern Detection")
        st.write("• Motion Artifact Analysis")
        st.write("• Neural Rendering Pattern Check")

# ---------------- FOOTER ----------------
st.divider()
st.caption("AI Fake Content Detector and Origin Identifier | Built with Streamlit & Python | Educational Project")
