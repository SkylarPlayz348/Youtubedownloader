import playlist
import video
import YTaudio
import os
import platform

if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")
def promt(type):
    if type == "1":
        video.download_video(input("Link: "))
    elif type == "2":
        playlist.download_playlist(input("Link: "))
    elif type == "3": 
        YTaudio.mp3(input("Link: "))
    else:
        print('')
type = input("""
    Youtubedownloader

Version: 1.2.0
____________________

1 - Video

2 - Playlist

3 - Video(Audio Only)

Anything Else - Quit

Option: """)
promt(type)
