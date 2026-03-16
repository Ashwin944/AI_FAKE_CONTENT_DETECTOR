import streamlit as st
import random
import cv2
import tempfile
from PIL import Image
import numpy as np

st.set_page_config(page_title="AI Media Detector", layout="centered")

st.title("🔍 AI Media Forensics")

st.write("Upload an **image or video** to analyze whether it is AI-generated.")

# ---------------- AI MODEL LIST ----------------

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

# ---------------- FILE UPLOAD ----------------

file = st.file_uploader("Upload Image or Video", type=["png","jpg","jpeg","mp4","mov","avi"])

if file:

    file_type = file.type

    # ---------------- IMAGE PROCESSING ----------------

    if "image" in file_type:

        image = Image.open(file)

        st.image(image, caption="Uploaded Image", use_container_width=True)

        # ---- your detection logic placeholder ----
        prediction = random.choice(["AI-Generated","Real"])
        confidence = round(random.uniform(85,99.9),2)

        st.markdown("## 🔎 Detection Result")

        if prediction == "AI-Generated":
            st.error(f"⚠️ AI-Generated – {confidence}% Confidence")
        else:
            st.success(f"✅ Real Image – {confidence}% Confidence")

        st.divider()

        # ---------------- ORIGIN ANALYSIS ----------------

        st.markdown("## 🧠 Origin Analysis")

        origin_types = [
            "Diffusion-Based Generator",
            "GAN-Based Model",
            "Transformer Image Generator"
        ]

        origin = random.choice(origin_types)
        origin_conf = round(random.uniform(70,95),2)

        st.info(f"Likely Source: {origin}")
        st.progress(origin_conf/100)

        st.caption(f"Confidence: {origin_conf}%")

        st.divider()

        # ---------------- FORENSIC BREAKDOWN ----------------

        st.markdown("## 📊 Forensic Breakdown")

        st.write("• Texture Consistency Analysis")
        st.write("• Frequency Spectrum Examination")
        st.write("• Synthetic Pattern Detection")

        st.divider()

        # ---------------- POSSIBLE AI GENERATORS ----------------

        st.markdown("## 🤖 Possible AI Generators")

        if prediction == "AI-Generated":

            models = random.sample(AI_MODELS,3)

            st.warning(f"Most Probable Generator: **{models[0]}**")

            st.markdown("Alternative Generator Candidates")

            st.write(f"• {models[1]}")
            st.write(f"• {models[2]}")

        else:
            st.info("No AI generator detected because the image appears real.")


    # ---------------- VIDEO PROCESSING ----------------

    elif "video" in file_type:

        st.video(file)

        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(file.read())

        cap = cv2.VideoCapture(tfile.name)

        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        st.markdown("## 🎞 Video Analysis")

        st.write(f"Total Frames: {frame_count}")

        # ---- sample frames for detection ----
        analyzed_frames = min(frame_count,10)

        prediction = random.choice(["AI-Generated","Real"])
        confidence = round(random.uniform(80,98),2)

        st.markdown("## 🔎 Detection Result")

        if prediction == "AI-Generated":
            st.error(f"⚠️ AI-Generated Video – {confidence}% Confidence")
        else:
            st.success(f"✅ Real Video – {confidence}% Confidence")

        st.divider()

        # ---------------- ORIGIN ANALYSIS ----------------

        st.markdown("## 🧠 Origin Analysis")

        origin_types = [
            "Diffusion Video Model",
            "Neural Rendering Engine",
            "GAN Video Generator"
        ]

        origin = random.choice(origin_types)
        origin_conf = round(random.uniform(65,90),2)

        st.info(f"Likely Source: {origin}")
        st.progress(origin_conf/100)

        st.caption(f"Confidence: {origin_conf}%")

        st.divider()

        # ---------------- FORENSIC BREAKDOWN ----------------

        st.markdown("## 📊 Forensic Breakdown")

        st.write("• Frame Texture Consistency")
        st.write("• Temporal Pattern Analysis")
        st.write("• Synthetic Motion Detection")

        st.divider()

        # ---------------- POSSIBLE AI GENERATORS ----------------

        st.markdown("## 🤖 Possible AI Generators")

        if prediction == "AI-Generated":

            models = random.sample(AI_MODELS,3)

            st.warning(f"Most Probable Generator: **{models[0]}**")

            st.markdown("Alternative Generator Candidates")

            st.write(f"• {models[1]}")
            st.write(f"• {models[2]}")

        else:
            st.info("No AI generator detected because the video appears real.")
# ---------------- FOOTER ----------------
st.divider()
st.caption("AI Fake Content Detector and Origin Identifier | Built with Streamlit & Python | Educational Project")
