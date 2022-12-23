from pytube import YouTube
import os

os.system("color 02")
def download_video(link):
    youtubeObject = YouTube(link)
    author = youtubeObject.author
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
            print("Downloading: "+youtubeObject.title+" by "+author)
            youtubeObject.download(output_path="./Videos")
    except Exception as e:
        os.system("cls")
        os.system("color 04")
        print("Error occured while downloading")
        print(e)
        input("Press Enter to Quit")
    os.system("cls")
    print("\nDowloaded\n")
    input("Press Enter To Quit")