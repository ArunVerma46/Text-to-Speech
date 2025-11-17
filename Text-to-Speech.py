import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
from gtts import gTTS
import os


# -----------------------------
# THEME COLORS
# -----------------------------
dark_bg = "#111111"
dark_fg = "#ffffff"
light_bg = "#ffffff"
light_fg = "#000000"

current_theme = "dark"


# -----------------------------
# WINDOW SETUP
# -----------------------------
root = tk.Tk()
root.title("AI TEXT ➜ VOICE CONVERTER")
root.geometry("800x500")
root.configure(bg=dark_bg)


# -----------------------------
# TOGGLE THEME FUNCTION
# -----------------------------
def toggle_theme():
    global current_theme

    if current_theme == "dark":
        current_theme = "light"
        root.configure(bg=light_bg)
        text_box.configure(bg=light_bg, fg=light_fg, insertbackground=light_fg)
        status_label.configure(bg=light_bg, fg=light_fg)
        theme_btn.configure(text="☀ Dark Mode")
    else:
        current_theme = "dark"
        root.configure(bg=dark_bg)
        text_box.configure(bg=dark_bg, fg=dark_fg, insertbackground=dark_fg)
        status_label.configure(bg=dark_bg, fg=dark_fg)
        theme_btn.configure(text="☾ Light Mode")


# -----------------------------
# SPEAK TEXT (OFFLINE)
# -----------------------------
def speak_offline():
    text = text_box.get("1.0", tk.END).strip()
    if text:
        temp_engine = pyttsx3.init()   # recreate engine – prevents freeze
        temp_engine.setProperty("rate", 175)
        temp_engine.say(text)
        temp_engine.runAndWait()
        temp_engine.stop()


# -----------------------------
# SAVE AS MP3 (AI VOICE USING gTTS)
# -----------------------------
def save_mp3():
    text = text_box.get("1.0", tk.END).strip()
    if text:
        save_path = filedialog.asksaveasfilename(
            defaultextension=".mp3",
            filetypes=[("MP3 File", "*.mp3")],
            title="Save MP3 File"
        )

        if save_path:
            tts = gTTS(text=text, lang='en')
            tts.save(save_path)
            status_label.config(text="✔ MP3 Saved Successfully!")


# -----------------------------
# PLAY MP3
# -----------------------------
def play_mp3():
    file_path = filedialog.askopenfilename(
        filetypes=[("MP3 File", "*.mp3")],
        title="Select MP3 to Play"
    )

    if file_path:
        os.system(f'start "" "{file_path}"')  # Windows default audio player
        status_label.config(text="▶ Playing MP3...")


# -----------------------------
# TITLE LABEL
# -----------------------------
title = tk.Label(root, text="AI TEXT ➜ VOICE CONVERTER",
                 font=("Arial", 20, "bold"),
                 bg=dark_bg, fg=dark_fg)
title.pack(pady=10)


# -----------------------------
# TEXT BOX
# -----------------------------
text_box = tk.Text(root, height=12, font=("Arial", 14),
                   bg=dark_bg, fg=dark_fg, insertbackground="white")
text_box.pack(fill="both", padx=20, pady=10, expand=True)


# -----------------------------
# BUTTON FRAME
# -----------------------------
btn_frame = tk.Frame(root, bg=root["bg"])
btn_frame.pack(pady=10)

speak_btn = tk.Button(btn_frame, text="Speak (Offline)", width=18,
                      command=speak_offline)
speak_btn.grid(row=0, column=0, padx=10)

save_btn = tk.Button(btn_frame, text="Save as MP3 (AI Voice)", width=20,
                     command=save_mp3)
save_btn.grid(row=0, column=1, padx=10)

play_btn = tk.Button(btn_frame, text="Play MP3", width=15,
                     command=play_mp3)
play_btn.grid(row=0, column=2, padx=10)


# -----------------------------
# THEME BUTTON
# -----------------------------
theme_btn = tk.Button(root, text="☾ Light Mode", width=15, command=toggle_theme)
theme_btn.pack(pady=5)


# -----------------------------
# STATUS LABEL
# -----------------------------
status_label = tk.Label(root, text="", bg=dark_bg, fg=dark_fg, font=("Arial", 12))
status_label.pack()


root.mainloop()
