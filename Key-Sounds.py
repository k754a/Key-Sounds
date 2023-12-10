from pynput import mouse
import pygame
import os
import keyboard
import threading



pygame.mixer.init()


script_dir = os.path.dirname(os.path.abspath(__file__))


sound_file_path = os.path.join(script_dir, 'keysounds.mp3')  # Replace 'soundfile.mp3' with your actual sound file name
sound = pygame.mixer.Sound(sound_file_path)


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


mouse_listener = mouse.Listener(on_click=on_click)
keyboard.hook(on_key)


mouse_listener.start()


try:
    mouse_listener.join()
except KeyboardInterrupt:
    pass
