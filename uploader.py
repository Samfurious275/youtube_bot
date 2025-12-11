# uploader.py

import os
import time
import random
from instagrapi import Client

# ⚙️ Configuration
DOWNLOAD_DIR = "downloads/"  # Folder where videos are saved
MAX_UPLOADS_PER_RUN = 6      # Maximum number of reels to upload at once
MIN_DELAY = 5                # Minimum delay in seconds
MAX_DELAY = 15               # Maximum delay in seconds


def load_instagram_session():
    """
    Load Instagram session using saved session.json file
    """
    cl = Client()  # No proxy needed
    session_file = "session.json"

    try:
        if os.path.exists(session_file):
            cl.load_settings(session_file)
            cl.login("your_instagram_username", "dummy_password")  # Uses cached session
            print("✅ Logged in using saved session")
        else:
            raise FileNotFoundError("Session file not found. Please run save_session.py first.")
    except Exception as e:
        print(f"[ERROR] Failed to load session: {e}")
        exit(1)

    return cl


def upload_videos():
    """
    Upload up to 6 videos from downloads folder
    """
    # Initialize Instagram client
    cl = load_instagram_session()

    # Get list of video files, limit to 6
    files = sorted([f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(".mp4")])[:MAX_UPLOADS_PER_RUN]

    if not files:
        print("[INFO] No videos found to upload.")
        return

    # Start uploading
    for idx, file in enumerate(files, start=1):
        path = os.path.join(DOWNLOAD_DIR, file)
        caption = "Auto-uploaded reel #shorts #viral #fyp"  # You can customize this

        try:
            print(f"[INFO] Uploading {idx}/{len(files)}: {file}")
            cl.video_upload(path, caption)
            print(f"[✅] Uploaded: {file}")

            # Add random delay to mimic human behavior
            delay = random.randint(MIN_DELAY, MAX_DELAY)
            print(f"[💤] Waiting {delay} seconds before next upload...\n")
            time.sleep(delay)

        except Exception as e:
            print(f"[❌] Failed to upload {file}: {str(e)}")

    print("[🎉] Batch upload completed.")


def cleanup_downloads():
    """
    Delete uploaded MP4 and JPG files
    """
    for file in os.listdir(DOWNLOAD_DIR):
        if file.endswith(".mp4") or file.endswith(".jpg"):
            os.remove(os.path.join(DOWNLOAD_DIR, file))
    print("[🧹] Download folder cleaned.")
