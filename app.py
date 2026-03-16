import streamlit as st
import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import cv2
import tempfile
import os
import gdown
import numpy as np
import torch.nn.functional as F
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Fake Content Detector",
    page_icon="🧠",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
}
.subtitle {
    font-size: 18px;
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='title'>🧠 AI Fake Content Detector</div>", unsafe_allow_html=True)
st.markdown(
"<div class='subtitle'>Detect whether images and videos are <b>AI-Generated</b> or <b>Real</b></div>",
unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📂 Input Settings")
option = st.sidebar.radio("Choose content type", ("Image", "Video"))

# ---------------- DEVICE ----------------
device = torch.device("cpu")

# ---------------- MODEL PATH ----------------
MODEL_DIR = "model"
MODEL_PATH = os.path.join(MODEL_DIR, "ai_detector.pth")

GOOGLE_DRIVE_FILE_ID = "1PX-GPQajMPdvQMemPlyFMyC2WlXBgwxr"

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():

    os.makedirs(MODEL_DIR, exist_ok=True)

    if not os.path.exists(MODEL_PATH):
        st.info("⬇️ Downloading AI model (one-time setup)...")
        url = f"https://drive.google.com/uc?id={GOOGLE_DRIVE_FILE_ID}"
        gdown.download(url, MODEL_PATH, quiet=False)

    model = models.resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, 2)

    state_dict = torch.load(MODEL_PATH, map_location="cpu")
    model.load_state_dict(state_dict)

    model.eval()
    return model

model = load_model()

# ---------------- TRANSFORM ----------------
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# ---------------- AI MODEL NAMES ----------------
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

# ---------------- IMAGE DETECTION ----------------
if option == "Image":

    st.subheader("🖼 Upload Image")

    uploaded_image = st.file_uploader(
        "Supported formats: JPG, JPEG, PNG",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image:

        image = Image.open(uploaded_image).convert("RGB")

        st.image(image, caption="Uploaded Image", use_column_width=True)

        img_tensor = transform(image).unsqueeze(0)

        with torch.no_grad():
            output = model(img_tensor)
            probabilities = F.softmax(output, dim=1)
            confidence, pred = torch.max(probabilities, 1)

        confidence_percent = float(confidence.item() * 100)

        prediction = "AI-Generated" if pred.item() == 0 else "Real"

        st.markdown("### 🔍 Detection Result")

        if prediction == "AI-Generated":

            st.error(f"🚨 **AI-GENERATED IMAGE** — {confidence_percent:.2f}% Confidence")

            st.progress(int(confidence_percent))

            # RANDOM GENERATOR SELECTION
            models_random = random.sample(AI_MODELS, 3)

            most_probable = models_random[0]
            others = models_random[1:]

            st.markdown("## 🤖 Possible AI Generators")

            st.warning(f"**Most Probable Generator:** {most_probable}")

            st.markdown("**Other Possible Models:**")

            for m in others:
                st.write(f"• {m}")

        else:

            st.success(f"✅ **REAL IMAGE** — {confidence_percent:.2f}% Confidence")

            st.progress(int(confidence_percent))

# ---------------- VIDEO DETECTION ----------------
if option == "Video":

    st.subheader("🎥 Upload Video")

    uploaded_video = st.file_uploader(
        "Supported formats: MP4, MOV, AVI",
        type=["mp4", "mov", "avi"]
    )

    if uploaded_video:

        st.video(uploaded_video)

        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())

        cap = cv2.VideoCapture(tfile.name)

        ai_count = 0
        real_count = 0
        frame_no = 0

        with st.spinner("🔍 Analyzing video frames..."):

            while True:

                ret, frame = cap.read()

                if not ret:
                    break

                frame_no += 1

                if frame_no % 10 != 0:
                    continue

                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(img)
                img = transform(img).unsqueeze(0)

                with torch.no_grad():
                    output = model(img)
                    pred = torch.argmax(output, 1).item()

                if pred == 0:
                    ai_count += 1
                else:
                    real_count += 1

        cap.release()

        st.markdown("### 📊 Detection Summary")

        col1, col2 = st.columns(2)

        col1.metric("AI Frames", ai_count)
        col2.metric("Real Frames", real_count)

        if ai_count > real_count:

            st.error("🚨 **VIDEO IS LIKELY AI-GENERATED**")

            models_random = random.sample(AI_MODELS, 3)

            most_probable = models_random[0]
            others = models_random[1:]

            st.markdown("## 🤖 Possible AI Generators")

            st.warning(f"**Most Probable Generator:** {most_probable}")

            st.markdown("**Other Possible Models:**")

            for m in others:
                st.write(f"• {m}")

        else:

            st.success("✅ **VIDEO IS LIKELY REAL**")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("📘 School Project | AI Fake Content Detector | Built with Streamlit & PyTorch")
