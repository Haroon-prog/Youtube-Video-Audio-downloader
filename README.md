# YouTube Video/Audio Downloader
A modern graphical application for downloading YouTube videos and audio, built with Python and Tkinter.

## Features
- User-Friendly Interface: Clean, dark-themed GUI with intuitive controls

- Dual Download Options: Download videos (MP4) or audio-only (MP3)

- Title Fetching: Automatically retrieves and displays video title from URL

- Progress Tracking: Real-time progress bar with percentage indicator

- Folder Selection: Choose custom download directory with browse functionality

- Background Processing: Non-blocking downloads using threading

- Cross-Platform: Works on Windows, macOS, and Linux

## Requirements
Python 3.6+

### Required packages:

1. pytubefix

2. tkinter (usually included with Python installations)

## Installation
1. Clone or download this repository

2. Install the required dependencies:

```bash
pip install pytubefix
```

## Usage
Run the application:

```bash
python main.py
```
Enter a YouTube URL in the input field

Click "Get Title" to fetch and display the video title

Select download directory (optional - defaults to current directory)

Check "Audio Only" for MP3 download (uncheck for MP4 video)

Click "Download" to begin

Monitor progress via the progress bar and status indicator

Receive confirmation when download completes

## Example
Run WELCOME TO YOUTUBE VIDEO/AUDIO DOWNLOADER PROGRAM !😃😉 Enter the video url(link) you want to download⬇️ https://www.youtube.com/shorts/sxmTTS4qros Do you want Video or Audio ? video

video downloaded!
check videos folder

## Directory Structure
Downloads are organized in subfolders:

Videos are saved in /videos/ folder

Audio files are saved in /audios/ folder

## Notes
File names are automatically sanitized to remove invalid characters

The application creates necessary folders if they don't exist

Download may take time depending on video length and internet speed