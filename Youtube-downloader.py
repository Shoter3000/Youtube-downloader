from pytube import YouTube
from moviepy import *
from moviepy.editor import VideoFileClip
import shutil
from pathlib import Path
import re
from pytube import Playlist
import moviepy.editor as mp
import tkinter as tk
import eyed3
import os
from os import path
from tkinter import filedialog
from tkinter import Tk


var1 = 0

# Create an instance of Tkinter
root = Tk()
root.withdraw()

def download_file():
    #download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move to selected directory
    shutil.move(mp4_video, user_path)


def download_file_mp3():
    print

def download_playlist():
    print


def include_author_metadata():
    if input("Do you want to include author metadata for audio files? (Y/N): ").lower() == 'y':
        return True
    else:
        return False

print("*********************Youtube Downloader************************")
print("\n")

#get url
get_link = input("Enter the URL of the video or playlist: ")
print("")

#get path
user_path = filedialog.askdirectory(initialdir="/", title="Select the location where the files will be SAVED!")
print("Files will be saved in "+user_path)
print("")


# Ask user for download option
download_option = input("Select an option:\n1 Download Video\n2 Download Audio\n3 Download Playlist\nEnter the number: ")

# Handle user selection
if download_option == "1":
    download_file()
elif download_option == "2":
    download_file_mp3()
    if include_author_metadata():
        print("Author metadata will be included for audio files.")
        var1 = 1
    else:
        print("Author metadata will not be included for audio files.")
elif download_option == "3":
    download_playlist()
    if include_author_metadata():
        print("Author metadata will be included for playlist videos.")
        var1 = 1
    else:
        print("Author metadata will not be included for playlist videos.")
else:
    print("Invalid option selected.")

