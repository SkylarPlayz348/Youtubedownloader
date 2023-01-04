from pytube import YouTube
import os
import platform

def download_video(link):
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    youtubeObject = YouTube(link)
    author = youtubeObject.author
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
            print("Downloading: "+youtubeObject.title+" by "+author)
            youtubeObject.download(output_path="./Videos")
    except Exception as e:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        os.system("color 04")
        print("Error occured while downloading")
        print(e)
        input("Press Enter to Quit")
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("\nDowloaded\n")
    input("Press Enter To Quit")
