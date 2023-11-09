"""
How to use : python ytdownloader.py "http://www.youtube.com/watchxxxxx"
"""

from pytube import YouTube
from sys import argv
import os

# pytube library used to access youtube videos
# argv[1] is the link of the video because argv[0] is the name of the python program
# for example \test1> python ytdownloader.py text1 text 2 txt3
# [0] ytdownloader.py
# [1] text1
# [2] text
# [2] 2
# [3] txt3

link = argv[1]
yt = YouTube(link)
dl_path = os.getcwd()  # save in same dir

# Print video information
print("Title: ", yt.title)
print("View: ", yt.views)

# Select resolution
yd = yt.streams.get_highest_resolution()

# Download in current directory
yd.download(dl_path)
