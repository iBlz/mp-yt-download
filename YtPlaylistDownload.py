import time
import os
from pytube import Playlist

os.system("clear")
print("Example : https://www.youtube.com/playlist?list=PLTkhVYRazJcWqWpOxJQTnFSuysb6E_6Rk")
print("WARNING : If there is a emoji or a special symbol in title of a video it will not be renamed! ")
type = input("Enter Playlist : ")
print("")
p = Playlist('' + type)
print(f'Downloading: {p.title}')
for video in p.videos:
    video.streams.first().download()
print("")
print("Downloaded!")
print("")
print("Renaming Files...")
os.system('rename "s/ /_/g" *')
print("Convering MP4 to MP3...")
os.system('for i in *.mp4; do ffmpeg -i "$i" "${i%.*}.mp3"; done')
print("Copying & Deleting Files...")
os.system("mkdir MP3")
os.system("mkdir MP4")
os.system("cp *.mp3 MP3")
os.system("cp *.mp4 MP4")
os.system("rm *.mp3")
os.system("rm *.mp4")
print("")
print("DONE!")
