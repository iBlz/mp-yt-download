import time
import os
from pytube import Playlist

os.system("clear")
print("Example : https://www.youtube.com/playlist?list=PLTkhVYRazJcWqWpOxJQTnFSuysb6E_6Rk")
print("WARNING : If there is a emoji or a special symbol in title of a video it will not be renamed! ")
bruh = input("Enter Playlist : ")
print("")
p = Playlist('' + bruh)
print(f'Downloading: {p.title}')
for video in p.videos:
    video.streams.filter(only_audio=True, subtype='webm').first().download('')
print("")
print("Downloaded!")
print("")
print("Renaming Files...")
os.system('rename "s/ /_/g" *')
print("Convering WEBM to MP3...")
os.system('for i in *.webm; do ffmpeg -i "$i" "${i%.*}.mp3"; done')
print("Copying & Deleting Files...")
os.system("mkdir MP3")
os.system("cp *.mp3 MP3")
os.system("rm *.mp3")
os.system("rm *.webm")
print("")
print("DONE!")
