import pytesseract
from PIL import Image
import pytesseract
from gtts import gTTS
import playsound

# For Windows
pytesseract.pytesseract.tesseract_cmd = r'D:\narrative_cursor\tesseract.exe'
def image_to_audio(image_path, audio_path):
    # Load and process the image
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)

    # Convert text to speech
    tts = gTTS(text)
    tts.save(audio_path)

    # Play the generated audio
    playsound.playsound(audio_path)

if __name__ == "__main__":
    image_path = 'images_cursor/sample_image.png'
    audio_path = 'audio_cursor/output.mp3'
    image_to_audio(image_path, audio_path)


