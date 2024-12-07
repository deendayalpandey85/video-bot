# Video Bot

## Description

**Video Bot** is a Python-based bot that automatically downloads videos from Instagram and TikTok, then uploads them to a server using the provided APIs. The bot supports monitoring a local directory for new videos, downloading them, and uploading to a server using pre-signed URLs and API requests.

## Features

- Download Instagram videos using the `instaloader` library.
- Download TikTok videos using the `TikTokApi` library.
- Upload videos to the server using the provided APIs from SocialVerse.
- Monitor a specified directory for new `.mp4` files and automatically upload them.
- Automatically delete local files after successful upload to the server.
- Concurrent video downloads and uploads using `asyncio`.

## Requirements

To run this project, you need to have Python 3.6+ installed. The following libraries are used in this project:

- `instaloader`
- `TikTokApi`
- `requests`
- `asyncio`
- `watchdog`
- `tqdm`

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
Setup
Clone the repository:

git clone https://github.com/deendayalpandey85/video-bot.git
cd video-bot
Install dependencies:

pip install -r requirements.txt
Update the main.py file with your Flic-Token. Replace the placeholder with your token:

FLIC_TOKEN = "<your_flic_token>"
Make sure you have a valid Instagram and TikTok post URL for downloading videos.

Run the bot:

python main.py
File Structure
video-bot/
├── main.py                # Main script to run the bot
├── directory_monitor.py   # Directory monitoring for new video files
├── insta_downloader.py    # Instagram video downloader script
├── tiktok_downloader.py   # TikTok video downloader script
├── server_uploader.py    # API methods to upload videos to the server
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation (this file)
Project Workflow
The bot monitors a local videos/ directory.
When a new .mp4 file is detected, the bot uploads it to the server.
The bot fetches the upload URL using the SocialVerse API.
After a successful upload, the video is deleted from the local machine.
