import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageDraw, ImageFont
import imageio


#THE FRONTEND UI
def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    user_input = simpledialog.askstring("Input", "Enter your text:")
    frame_duration = simpledialog.askfloat("Speed", "Enter the frame duration in seconds (e.g., 0.5):")
    font_size = simpledialog.askinteger("Font Size", "Enter the font size (e.g., 24):")
    root.destroy()
    return user_input, frame_duration, font_size



def create_frames(text, font_size):
    words = text.split()
    frames = []
    width, height = 400, 200  # Dimensions for the GIF
    for word in words:
        image = Image.new('RGB', (width, height), color = 'white')
        draw = ImageDraw.Draw(image)
        draw.font = ImageFont.truetype("arial.ttf", font_size)
        # Fixed position for the text
        draw.text((width // 2, (height + font_size) // 2), word, align='center', anchor="ms",  fill='black', font=draw.font)
        frames.append(image)
    return frames



#EXPORTING THE ACTUAL GIF
def save_gif(frames, path, frame_duration):
    with imageio.get_writer(path, mode='I', duration=200*frame_duration) as writer:
        for frame in frames:
            writer.append_data(frame)



#JUST THE MAIN FILE PIECING IT ALL TOGETHER
def main():
    text, frame_duration, font_size = get_user_input()
    if text:
        frames = create_frames(text, font_size)
        save_gif(frames, 'output.gif', frame_duration)
        print("GIF created successfully.")

if __name__ == "__main__":
    main()
