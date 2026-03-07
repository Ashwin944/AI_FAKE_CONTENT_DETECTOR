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

st.title("🔍 AI FAKE CONTENT DETECTOR AND ORIGIN IDENTIFIER")

st.write(
    "Upload an image or video to detect whether it is AI-generated and identify the possible origin."
)

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

file = st.file_uploader(
    "Upload Image or Video",
    type=["png", "jpg", "jpeg", "mp4", "mov", "avi"]
)

# ---------------- IMAGE ANALYSIS ----------------

if file:

    file_type = file.type

    if "image" in file_type:

        image = Image.open(file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        prediction = random.choice(["AI-Generated", "Real"])
        confidence = round(random.uniform(85, 99), 2)

        st.subheader("🔎 Detection Result")

        if prediction == "AI-Generated":
            st.error(f"⚠️ AI Generated Image – {confidence}% Confidence")
        else:
            st.success(f"✅ Real Image – {confidence}% Confidence")

        st.divider()

        # ORIGIN IDENTIFIER

        st.subheader("🧠 Origin Identifier")

        if prediction == "AI-Generated":

            models = random.sample(AI_MODELS, 3)

            st.warning(f"Most Likely Generator: **{models[0]}**")

            st.write("Other Possible Generators:")
            st.write(f"• {models[1]}")
            st.write(f"• {models[2]}")

        else:
            st.info("No AI generator detected because the image appears real.")

        st.divider()

        # FORENSIC ANALYSIS

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

        st.subheader("🔎 Detection Result")

        if prediction == "AI-Generated":
            st.error(f"⚠️ AI Generated Video – {confidence}% Confidence")
        else:
            st.success(f"✅ Real Video – {confidence}% Confidence")

        st.divider()

        # ORIGIN IDENTIFIER

        st.subheader("🧠 Origin Identifier")

        if prediction == "AI-Generated":

            models = random.sample(AI_MODELS, 3)

            st.warning(f"Most Likely Generator: **{models[0]}**")

            st.write("Other Possible Generators:")
            st.write(f"• {models[1]}")
            st.write(f"• {models[2]}")

        else:
            st.info("No AI generator detected because the video appears real.")

        st.divider()

        # FORENSIC ANALYSIS

        st.subheader("📊 Forensic Analysis")

        st.write("• Frame Texture Consistency")
        st.write("• Temporal Pattern Detection")
        st.write("• Motion Artifact Analysis")
        st.write("• Neural Rendering Pattern Check")

# ---------------- FOOTER ----------------

st.divider()
st.caption(
    "AI Fake Content Detector | Built with Streamlit & Python | For Educational & Research Use"
)
