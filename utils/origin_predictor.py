import numpy as np
import cv2

def predict_origin(pil_image):
    image = np.array(pil_image)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Frequency analysis
    fft = np.fft.fft2(gray)
    magnitude = np.abs(fft)
    avg_frequency = np.mean(magnitude)

    # Texture variance
    texture_score = np.var(gray)

    # Weighted scoring
    diffusion_score = (avg_frequency * 0.6) + (texture_score * 0.4)

    if diffusion_score > 5000:
        return {
            "label": "Likely Diffusion-Based Model",
            "confidence": 0.82
        }
    else:
        return {
            "label": "Likely GAN-Based Generator",
            "confidence": 0.68
        }