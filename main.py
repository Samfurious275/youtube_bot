import downloader
import uploader
import logging
import schedule
import time

logging.basicConfig(filename='logs/bot.log', level=logging.INFO)

def job():
    logging.info("Starting downloader...")
    downloader.download_videos_from_csv()

    logging.info("Starting uploader...")
    uploader.upload_videos()

    logging.info("Cleaning up downloaded videos...")
    uploader.cleanup_downloads()

    logging.info("Process completed.")

# 🔁 Run once immediately on startup
logging.info("Running job immediately on startup...")
job()

# 🕒 Schedule daily at 8:00 AM and 7:00 PM (peak times)
schedule.every().day.at("08:00").do(job)   # Morning
schedule.every().day.at("19:00").do(job)   # Evening

logging.info("Scheduler started. Waiting for scheduled times...")

# Keep checking for scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(60)
