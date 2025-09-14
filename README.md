🎥 YouTube Video/Audio Downloader

A simple Python program that allows users to download YouTube videos or audio directly to their computer using pytubefix
.


-------------------------------------------------------------------------------
✨ Features

Download video in the highest available resolution (progressive stream, max 720p).

Download audio only from YouTube videos.

Automatically creates organized folders:

downloads/videos/ for video files

downloads/audios/ for audio files

Displays video title and thumbnail URL before downloading.

User-friendly command-line interface.

-------------------------------------------------------------------------------
🛠️ Requirements

Python 3.7+

Install dependencies using:
pip install pytubefix      (run this command in terminal/command prompt to install)

-------------------------------------------------------------------------------

🚀 How to Use

1.Run the program:
python main.py

2.Paste the YouTube URL when prompted.

3.Choose whether you want to download Video or Audio.

4.The file will be saved inside the respective folder.

-------------------------------------------------------------------------------

📂 Folder Structure
yt-video-downloader/
│
├── main.py
├── downloads/
│   ├── videos/
│   └── audios/



-------------------------------------------------------------------------------

⚡ Example Run
WELCOME TO YOUTUBE VIDEO/AUDIO DOWNLOADER PROGRAM !😃😉
Enter the video url(link) you want to download⬇️
https://www.youtube.com/shorts/sxmTTS4qros
Do you want Video or Audio ?
video

video downloaded!  
check downloads/videos folder

-------------------------------------------------------------------------------

Notes:
- The script uses Python's built-in os module, no installation required.
- Audio downloads are saved as .mp4 for now (conversion to .mp3 can be added in future versions).
- Document to refer for further details : "https://pytube3.readthedocs.io/en/latest/user/quickstart.html"


-------------------------------------------------------------------------------

