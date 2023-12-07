from pynput import mouse
import pygame
import os
import keyboard
import threading


# Initialize pygame mixer
pygame.mixer.init()

# Get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load a sound file from the same directory as the script
sound_file_path = os.path.join(script_dir, 'keysounds.mp3')  # Replace 'soundfile.mp3' with your actual sound file name
sound = pygame.mixer.Sound(sound_file_path)

# Function to play the sound asynchronously
def play_sound():
    sound.play()

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y})")
        threading.Thread(target=play_sound).start()

def on_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        print(f"Key pressed: {event.name}")
        threading.Thread(target=play_sound).start()

# Create listeners for mouse events and key events
mouse_listener = mouse.Listener(on_click=on_click)
keyboard.hook(on_key)

# Start the listeners in the background
mouse_listener.start()

# Wait for the listeners to finish (Ctrl+C to stop the script)
try:
    mouse_listener.join()
except KeyboardInterrupt:
    pass
