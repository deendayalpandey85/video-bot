from insta_downloader import download_instagram_video
from tiktok_downloader import download_tiktok_video
from directory_monitor import start_monitoring
import asyncio

async def main():
    FLIC_TOKEN = "flic_e02d365b7a966a37ce2a4348779ceef2dc5c486b2d650a38472786fc4f979af3"

    # Download videos from Instagram and TikTok
    download_instagram_video("https://www.instagram.com/p/DAODfg4SQbY/?igsh=NTc4MTIwNjQ2YQ==", "videos")
    download_tiktok_video("https://www.tiktok.com/@username/video/<video_id>", "videos/tiktok_video.mp4")

    # Start monitoring the videos directory for new .mp4 files
    start_monitoring("videos/", FLIC_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
