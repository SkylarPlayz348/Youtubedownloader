from moviepy.video.io.VideoFileClip import VideoFileClip
from pytube import YouTube
import os
import shutil
import platform

def convert(file):
    os.system("cls")
    print("Converting to mp3\n")
    mp4_file = r"./Temp/"+file+".mp4"
    mp3_file = r"./Audio/"+file+".mp3"

    videoclip = VideoFileClip(mp4_file)

    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)

    audioclip.close()
    videoclip.close()
    shutil.rmtree("./Temp")
    input("Press Enter to Quit")



def mp3(link):
    os.system("cls")
    
    youtubeObject = YouTube(link)
    author = youtubeObject.author
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
            print("Downloading: "+youtubeObject.title+" by "+author)
            youtubeObject.download(output_path="./Temp", filename=youtubeObject.title+" by "+author+".mp4")
    except Exception as e:
        os.system("cls")
        os.system("color 04")
        print("Error occured while downloading")
        print(e)
        input("Press Enter to Quit")
    convert(youtubeObject.title+" by "+author)
