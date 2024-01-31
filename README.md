# Narrative_cursor
import os
import pyttsx3
from PIL import ImageGrab
import pytesseract
import cv2
import time
import keyboard
import pygetwindow as gw

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Configure the text-to-speech engine
engine.setProperty('rate', 200)  # Speed of speech

# Set the path to Tesseract OCR executable (you may need to change this)
tesseract_path = r'C:\Users\USER\AI_ML_DL Programs & Codes'
pytesseract.pytesseract.tesseract_cmd = os.path.join(tesseract_path, 'tesseract.exe')

# Set the path to the "NC_images" folder
nc_images_path = os.path.join(tesseract_path, 'NC_images')

# Function to perform OCR on the selected region and read the text aloud
def read_text(selected_region):
    text = pytesseract.image_to_string(selected_region)
    print("Detected Text: ", text)
    engine.say(text)
    engine.runAndWait()

# Function to capture a specific region in the active window and call the read_text function
def capture_and_read_specific_region():
    # Ensure the "NC_images" folder exists
    if not os.path.exists(nc_images_path):
        os.makedirs(nc_images_path)

    # Pause for a moment to switch to the desired window
    time.sleep(3)  # Adjust this time as needed

    # Get the active window
    active_window = gw.getActiveWindow()

    # Define the specific region coordinates
    region_left = 600
    region_top = active_window.height - 52 - 850  # 52 pixels above the bottom edge
    region_width = 720
    region_height = 890

    # Set the bounding box to capture the specific region
    selected_region = (active_window.left + region_left,
                       active_window.top + region_top,
                       active_window.left + region_left + region_width,
                       active_window.top + region_top + region_height)

    # Save the screenshot in the "NC_images" folder with a unique name
    screenshot_path = os.path.join(nc_images_path, f"screenshot_{len(os.listdir(nc_images_path)) + 1}.png")
    screenshot = ImageGrab.grab(bbox=selected_region)
    screenshot.save(screenshot_path)

    # Read the screenshot image
    screenshot = cv2.imread(screenshot_path)

    # Perform OCR on the selected region
    read_text(screenshot)

# Example usage
if __name__ == "__main__":
    print("Narrative Cursor - Text to Speech")

    input("Press Enter to start capturing and reading the specific region in the active window:")

    while True:
        # Simulate pressing Enter every second (adjust as needed)
        keyboard.press_and_release("enter")
        time.sleep(1)
        capture_and_read_specific_region()
