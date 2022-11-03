from pytube import YouTube
from sys import argv

targetDir = argv[2]  # capture the directory where we want to save the video to
link = argv[1]  # capture the URL of the YouTube video we want to save
yt = YouTube(link)  # capture the YouTube video data from the link we provided

print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()  # grab the highest resolution of the video.
yd.download(targetDir)  # download the YT video to the specified target directory.
