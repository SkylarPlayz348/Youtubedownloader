from moviepy.video.io.VideoFileClip import VideoFileClip
import os


def convert(file):
    os.system("cls")
    mp4_file = r"./Videos/"+file+".mp4"
    mp3_file = r"./Audio/"+file+".mp3"

    videoclip = VideoFileClip(mp4_file)

    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)

    audioclip.close()
    videoclip.close()
    input("Press Enter to Quit")