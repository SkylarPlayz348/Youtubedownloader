from pytube import Playlist
from time import sleep
import os
import platform

if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")
def download_playlist(link):
    youtubeObject = Playlist(link)
    try:
            print("Downloading Playlist: "+youtubeObject.title)
            for video in youtubeObject.videos:
                
                print("Downloading: "+video.title+" by "+video.author)
                video.streams.get_highest_resolution().download(max_retries=5,skip_existing=True,output_path="./Playlists/"+youtubeObject.title)
                sleep(3)
    except Exception as e:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        print("Error occured while downloading")
        print(e)
        input("Press Enter to Quit")
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("\nDowloaded\n")
    input("Press Enter To Quit")
