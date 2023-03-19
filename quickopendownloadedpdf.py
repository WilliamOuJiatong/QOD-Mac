#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title QuickOpenDownloadedPDF
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.description Open the latestest downloaded pdf document.
# @raycast.author Jiatong Ou

import os
import glob
import platform
import subprocess

# Set the directory where the downloaded files are stored
DOWNLOAD_DIR = 'path/to/the/download/directory'

# Find the newest PDF in the directory
files = glob.glob(os.path.join(DOWNLOAD_DIR, '*.pdf'))
if not files:
    print("No PDF files found in directory:", DOWNLOAD_DIR)
    exit(1)

newest_file = max(files, key=os.path.getctime)

# Open the file using the appropriate command for the platform
if platform.system() == 'Darwin':
    # For macOS, use the 'open' command to open the file
    subprocess.call(['open', newest_file])
else:
    # For other platforms, use the 'xdg-open' command to open the file
    subprocess.call(['xdg-open', newest_file])
