# downloader.py

import os
from config import DOWNLOAD_DIR
import pandas as pd
from tqdm import tqdm
import yt_dlp

def download_videos_from_csv():
    df = pd.read_csv('data/links.csv')
    links = df['link'].tolist()

    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    ydl_opts = {
        'format': 'mp4',
        'outtmpl': f'{DOWNLOAD_DIR}/reel_%(autonumber)s.mp4',
        'quiet': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)
