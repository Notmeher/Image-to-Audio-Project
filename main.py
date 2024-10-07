import cv2
import os
from PIL import Image
from datetime import datetime
from image_understanding import get_response
from tts_op import text_to_speech

def image_to_audio(image):
    output_folder = "D:/Client File/image_to_audio_project/image_to_audio_project/"
    os.makedirs(output_folder, exist_ok=True)
    try:
        response = get_response(image)
        print("=========================================\n")
        print('Caption: ', response)
        print("=========================================\n")
        
        # Replace colons with hyphens to avoid invalid filename error
        current_time = datetime.now().strftime("%H-%M-%S")
        audio_filename = f"speech__{current_time}.wav"
        audio_path = os.path.join(output_folder, audio_filename)
        text_to_speech(response, audio_path)
        
        print("=========================================\n")
        print("Audio file generated successfully at:", audio_path)
        print("=========================================")
        return True
    except Exception as e:
        print("=========================================\n")
        print("Audio file generation failed.")
        print("Exception: ", e)
        print("=========================================")
        return False

# Sample usage
image_path = "D:/Client File/image_to_audio_project/image_to_audio_project/images.jpeg"
# When you read the image using cv2, then save it using cv2. After saving, you have to pass the image path to Image.open().
image = Image.open(image_path)
image_to_audio(image)
