from moviepy.video.io.VideoFileClip import VideoFileClip
from pytube import YouTube
import os
import shutil
import platform

def convert(file):
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    if not os.path.exists("./Audio"):
        os.mkdir("./Audio")
    print("Converting to mp3\n")
    mp4_file = r"./Temp/"+file+".mp4"
    mp3_file = r"./Audio/"+file+".mp3"

    videoclip = VideoFileClip(mp4_file)

    audioclip = videoclip.audio
    try:
        audioclip.write_audiofile(mp3_file)
    except Exception as e:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        os.system("color 04")
        print("Error occured while Converting")
        print(e)
        input("Press Enter to Quit")
    audioclip.close()
    videoclip.close()
    shutil.rmtree("./Temp")
    input("Press Enter to Quit")



def mp3(link):
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    
    youtubeObject = YouTube(link)
    author = youtubeObject.author
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
            print("Downloading: "+youtubeObject.title+" by "+author)
            youtubeObject.download(output_path="./Temp", filename=youtubeObject.title+" by "+author+".mp4")
    except Exception as e:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        os.system("color 04")
        print("Error occured while downloading")
        print(e)
        input("Press Enter to Quit")
    convert(youtubeObject.title+" by "+author)
