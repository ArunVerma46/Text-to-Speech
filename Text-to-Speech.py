import tkinter as tk
from tkinter import filedialog
import pyttsx3
from gtts import gTTS
from PIL import Image, ImageTk
import os

# ------------------------------------------------
# WINDOW SETUP
# ------------------------------------------------
root = tk.Tk()
root.title("My_Dark_UI")
root.geometry("1000x600")
root.configure(bg="#000000")
root.resizable(False, False)


# ------------------------------------------------
# LOAD PNG FRAMES
# ------------------------------------------------
outer_img = Image.open("C:\\Users\\Welcome\\Desktop\\New folder (3)\\solo_frame_outer.png")
outer_img = outer_img.resize((1000, 600))
outer_tk = ImageTk.PhotoImage(outer_img)

inner_img = Image.open("C:\\Users\\Welcome\\Desktop\\New folder (3)\\solo_frame_inner_glass.png")
inner_img = inner_img.resize((1000, 600))
inner_tk = ImageTk.PhotoImage(inner_img)


# ------------------------------------------------
# CANVAS FOR BACKGROUND
# ------------------------------------------------
canvas = tk.Canvas(root, width=1000, height=600, highlightthickness=0, bg="#000")
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, image=outer_tk, anchor="nw")
canvas.create_image(0, 0, image=inner_tk, anchor="nw")


# ------------------------------------------------
# TEXT BOX (Glass Panel Center)
# ------------------------------------------------
text_box = tk.Text(root,
                   font=("Consolas", 16),
                   bg="#0b0014",
                   fg="#d8c8ff",
                   insertbackground="#b57dff",
                   bd=0,
                   highlightthickness=2,
                   highlightbackground="#a55bff")
text_box.place(x=180, y=130, width=640, height=260)


# ------------------------------------------------
# TEXT TO SPEECH FUNCTIONS
# ------------------------------------------------
def speak_offline():
    text = text_box.get("1.0", tk.END).strip()
    if text:
        engine = pyttsx3.init()
        engine.setProperty("rate", 175)
        engine.say(text)
        engine.runAndWait()
        engine.stop()

def save_mp3():
    text = text_box.get("1.0", tk.END).strip()
    if text:
        path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                            filetypes=[("MP3 File", "*.mp3")])
        if path:
            gTTS(text=text, lang="en").save(path)
            status_label.config(text="✔ MP3 Saved!", fg="#b57dff")

def play_mp3():
    path = filedialog.askopenfilename(filetypes=[("MP3 File", "*.mp3")])
    if path:
        os.system(f'start "" "{path}"')
        status_label.config(text="▶ Playing...", fg="#b57dff")


# ------------------------------------------------
# NEON BUTTON FUNCTION
# ------------------------------------------------
def make_neon_button(text, cmd, x, y):
    btn = tk.Button(root,
                    text=text,
                    font=("Bahnschrift SemiBold", 13),
                    fg="#e8dafa",
                    bg="#300066",
                    activebackground="#5900b3",
                    activeforeground="#fff",
                    bd=0,
                    highlightthickness=2,
                    highlightbackground="#b57dff",
                    command=cmd)

    btn.place(x=x, y=y, width=200, height=45)

    return btn


# ------------------------------------------------
# BUTTONS (Under Panel)
# ------------------------------------------------
make_neon_button("Speak (Offline)", speak_offline, 140, 430)
make_neon_button("Save as MP3 (AI Voice)", save_mp3, 400, 430)
make_neon_button("Play MP3", play_mp3, 660, 430)


# ------------------------------------------------
# STATUS LABEL
# ------------------------------------------------
status_label = tk.Label(root,
                        text="",
                        font=("Arial", 12),
                        fg="#d8c8ff",
                        bg="#000000")
status_label.place(x=400, y=500)


root.mainloop()

