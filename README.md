# Youtubedownloader

# Note
This is my first full python script I(Sky) am bound to mess up somewhere or do practices that are bad so if you're better at python go ahead to contribute(look below for information).

### (UPDATE): 
I am no longer actively working on this project so if you want to pick it up go ahead but please credit me if you do.

### (Update II)
Looks like pytube(what is used for getting the video) isn't maintained anymore so it wont work

## Installing(Windows Only)
- Go over to releases and install the zip file

### NOTE
Do not remove the exe from the folder unless you want it to create the Videos/Playlists/Audio folders in another folder

## Installing(MacOS/Linux)
Due to Movie.py(what I use to get the audio) needing ffmpeg this is not compatible with UNIX systems ATM. If on a MacOS I recommend something like virtualbox(free and not partnered with Microsoft) or parrells(paid and partnered with Micorsoft) to run this

## Contributing
---
### Reguirements
- Python v3.10.8+(Coded with Python v3.11.1)

### Note
- If your running this on MacOS or Linux all times I write python do python3
---
- Download a copy of the main branch
- Create a virtual enviornment(python -m venv) called 'downloader' as its in the .gitignore file
- Activate the enviornment
- install the requirements.txt by 'pip install -r requirements.txt'
- Submit a pull request

## TODO
- Allow to download more than one video/playlist at a time
- Playlist audio only downloading
- Use GUI instead of CLI
- Add animated download bars
- Use my own package for downloading instead of [pytube](https://github.com/pytube/pytube)
- Remove the temp files once folder is being used in Audio, Videos, and Playlists
