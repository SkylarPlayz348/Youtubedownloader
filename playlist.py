from pytube import Playlist
from time import sleep
import os

os.system("color 02")
def download_playlist(link):
    youtubeObject = Playlist(link)
    try:
            print("Downloading Playlist: "+youtubeObject.title)
            for video in youtubeObject.videos:
                
                print("Downloading: "+video.title+" by "+video.author)
                video.streams.get_highest_resolution().download(max_retries=5,skip_existing=True,output_path="./Playlists/"+youtubeObject.title)
                sleep(3)
    except Exception as e:
        os.system("cls")
        os.system("color 04")
        print("Error occured while downloading")
        print(e)
        input("Press Enter to Quit")
    os.system("cls")
    print("\nDowloaded\n")
    input("Press Enter To Quit")