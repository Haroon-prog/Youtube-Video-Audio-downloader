import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading, os, re
from pytubefix import YouTube

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_var.set(folder)

def on_progress(stream, chunk, bytes_remaining):
    total = stream.filesize
    done = total - bytes_remaining
    percent = int(done / total * 100)
    progress["value"] = percent
    status_var.set(f"{percent}%")
    root.update_idletasks()

def fetch_title():
    url = url_var.get().strip()
    if not url:
        messagebox.showwarning("Error", "Enter YouTube URL")
        return
    try:
        yt = YouTube(url)
        safe_title = re.sub(r'[\\/*?:"<>|]', "", yt.title)
        title_var.set(safe_title)
    except Exception as e:
        title_var.set("Couldn't fetch title")

def download_video():
    try:
        url = url_var.get().strip()
        if not url:
            messagebox.showwarning("Error", "Enter YouTube URL")
            return
        yt = YouTube(url, on_progress_callback=on_progress)

        if audio_only_var.get():
            stream = yt.streams.filter(only_audio=True).first()
            ext, folder = "mp3", "audios"
        else:
            stream = yt.streams.filter(progressive=True).order_by("resolution").desc().first()
            ext, folder = "mp4", "videos"

        if not stream:
            raise Exception("No stream found")

        title = re.sub(r'[\\/*?:"<>|]', "", yt.title)
        filename = f"{title}.{ext}"
        path = os.path.join(folder_var.get(), folder)
        os.makedirs(path, exist_ok=True)

        stream.download(output_path=path, filename=filename)
        status_var.set("Done")
        messagebox.showinfo("Success", f"Saved to: {os.path.join(path, filename)}")
    except Exception as e:
        status_var.set("Failed")
        messagebox.showerror("Error", str(e))
    finally:
        btn.config(state="normal")

def start_thread():
    btn.config(state="disabled")
    progress["value"] = 0
    status_var.set("Starting...")
    t = threading.Thread(target=download_video, daemon=True)
    t.start()

BG_COLOR = "#1a1a2e"
PRIMARY_COLOR = "#4cc9f0"
HOVER_COLOR = "#3a86ff"
TEXT_COLOR = "#ffffff"

root = tk.Tk()
root.title("Youtube-Video-Audio-downloader")
root.geometry("600x420")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

url_var = tk.StringVar()
folder_var = tk.StringVar(value=os.getcwd())
audio_only_var = tk.BooleanVar()
status_var = tk.StringVar(value="Idle")
title_var = tk.StringVar(value="🎬 Video Title will appear here...")

style = ttk.Style()
style.theme_use("clam")
style.configure("TProgressbar", troughcolor=BG_COLOR, background=PRIMARY_COLOR, thickness=20)

def style_button(widget, bg=PRIMARY_COLOR, fg=TEXT_COLOR):
    widget.config(bg=bg, fg=fg, relief="flat",activebackground=HOVER_COLOR, activeforeground=TEXT_COLOR,font=("Segoe UI", 10, "bold"))

# URL
tk.Label(root, text="YouTube URL:", bg=BG_COLOR, fg=TEXT_COLOR, font=("Segoe UI", 11, "bold")).pack(pady=5)
url_frame = tk.Frame(root, bg=BG_COLOR)
url_frame.pack(pady=5)
tk.Entry(url_frame, textvariable=url_var, width=45, font=("Segoe UI", 10)).pack(side="left", padx=5)
fetch_btn = tk.Button(url_frame, text="Get Title", command=fetch_title, width=10)
fetch_btn.pack(side="left")
style_button(fetch_btn)

# Video Title Display
title_label = tk.Label(root, textvariable=title_var, wraplength=500, justify="center", bg=BG_COLOR, fg=PRIMARY_COLOR, font=("Segoe UI", 11, "italic"))
title_label.pack(pady=10)

# Folder
tk.Label(root, text="Download Folder:", bg=BG_COLOR, fg=TEXT_COLOR, font=("Segoe UI", 11, "bold")).pack(pady=5)
folder_frame = tk.Frame(root, bg=BG_COLOR)
folder_frame.pack(pady=5)
tk.Entry(folder_frame, textvariable=folder_var, width=40, font=("Segoe UI", 10)).pack(side="left", padx=5)
browse_btn = tk.Button(folder_frame, text="Browse", command=browse_folder, width=8)
browse_btn.pack(side="left")
style_button(browse_btn)

# Audio Only
tk.Checkbutton(root, text="Audio Only", variable=audio_only_var,bg=BG_COLOR, fg=TEXT_COLOR, selectcolor=BG_COLOR,font=("Segoe UI", 10, "bold")).pack(pady=10)

# Download Button
btn = tk.Button(root, text="Download", command=start_thread, width=15, height=2)
btn.pack(pady=10)
style_button(btn)

# Progress Bar
progress = ttk.Progressbar(root, length=450, mode="determinate", style="TProgressbar")
progress.pack(pady=15)

# Status
tk.Label(root, textvariable=status_var, bg=BG_COLOR, fg=PRIMARY_COLOR, font=("Segoe UI", 12, "bold")).pack()

root.mainloop()