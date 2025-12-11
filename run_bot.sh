#!/bin/bash

# Set the working directory
cd /home/samridr123/youtube_bot || { echo "Directory not found"; exit 1; }

# Activate virtual environment (if used)
source venv/bin/activate

# Run the bot
python3 main.py >> logs/bot_run.log 2>&1

# Deactivate virtual environment
deactivate
