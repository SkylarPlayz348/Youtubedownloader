import playlist
import video
import YTaudio
import os

os.system("color 02")
def promt(type):
    if type == "1":
        video.download_video(input("Link: "))
    elif type == "2":
        playlist.download_playlist(input("Link: "))
    elif type == "3": 
        YTaudio.convert(input("Filename: "))
    else:
        print('')
type = input("""
    YoutubeToMP4

Version: 1.0.0
____________________

1 - Video

2 - Playlist

3 - Convert To Audio: REQUIRES VIDEO IN Videos FOLDER

Anything Else - Quit

Option: """)
promt(type)