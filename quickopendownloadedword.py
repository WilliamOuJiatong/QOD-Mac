#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title QuickOpenDownloadedWord
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.description Open the latest downloaded word document.
# @raycast.author Jiatong Ou

import os
import glob
import platform
import subprocess

# Set the directory where the downloaded files are stored
DOWNLOAD_DIR = 'path/to/the/download/directory'

# Find the newest Word document in the directory
files = glob.glob(os.path.join(DOWNLOAD_DIR, '*.docx'))
if not files:
    print("No Word documents found in directory:", DOWNLOAD_DIR)
    exit(1)

newest_file = max(files, key=os.path.getctime)

# Open the file using the appropriate command for the platform
if platform.system() == 'Darwin':
    # For macOS, use the 'open' command with the 'TextEdit' app to open the file
    subprocess.call(['open', '-a', 'TextEdit', newest_file])
else:
    # For other platforms, there is no universal command to open Word documents
    print("Sorry, I don't know how to open Word documents on this platform.")
