#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title QuickOpenDownloadedWordOrPDF
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.description Open the latest downloaded word or pdf file.
# @raycast.author Jiatong Ou

import os
import glob
import platform
import subprocess

# Set the directory where the downloaded files are stored
DOWNLOAD_DIR = 'path/to/the/download/directory'

# Find the newest document in the directory
word_files = glob.glob(os.path.join(DOWNLOAD_DIR, '*.docx'))
pdf_files = glob.glob(os.path.join(DOWNLOAD_DIR, '*.pdf'))
files = word_files + pdf_files

if not files:
    print("No Word or PDF files found in directory:", DOWNLOAD_DIR)
    exit(1)

newest_file = max(files, key=os.path.getctime)

# Open the file using the appropriate command for the file type and platform
if newest_file.endswith('.pdf'):
    if platform.system() == 'Darwin':
        # For macOS, use the 'open' command to open the file
        subprocess.call(['open', newest_file])
    else:
        # For other platforms, use the 'xdg-open' command to open the file
        subprocess.call(['xdg-open', newest_file])
elif newest_file.endswith('.docx'):
    if platform.system() == 'Darwin':
        # For macOS, use the 'open' command with the 'TextEdit' app to open the file
        subprocess.call(['open', '-a', 'TextEdit', newest_file])
    else:
        # For other platforms, there is no universal command to open Word documents
        print("Sorry, I don't know how to open Word documents on this platform.")
else:
    # This should never happen, but just in case...
    print("Unknown file type:", newest_file)
    exit(1)
