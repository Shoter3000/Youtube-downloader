from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import shutil
from pathlib import Path
import re
from pytube import Playlist
import eyed3
import os
import sys

var1 = 0

def download_file():
    print()
    mp4_video = YouTube(get_link, on_progress_callback=on_progress).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    shutil.move(mp4_video, user_path)
    print("\rDownload complete!  ")

def download_file_mp3():
    mp3_audio = YouTube(get_link, on_progress_callback=on_progress).streams.filter(only_audio=True).first().download()
    audio_clip = AudioFileClip(mp3_audio)
    full_file_name = os.path.basename(mp3_audio)
    file_name = Path(full_file_name).stem
    mp3_converted = f'{file_name}.mp3'
    audio_clip.write_audiofile(mp3_converted)
    if var1 == 1:
        channel_name = YouTube(get_link).author
        substring = " - Topic"
        if substring in channel_name:
            channel_name = channel_name.replace(" - Topic", "")
        audioFile = eyed3.load(mp3_converted)
        audioFile.tag.artist = channel_name
        audioFile.tag.save()
    shutil.move(mp3_converted, user_path)
    audio_clip.close()
    os.remove(full_file_name)
    print("Download complete!!!")

def download_playlist():
    playlist = Playlist(get_link)
    playlsit_name = playlist.title
    main_dir = os.path.join(user_path, playlsit_name)
    download_existing_videos = 0

    if not os.path.isdir(main_dir):
        os.makedirs(main_dir)
        print("Download folder for the playlist has been created!")
    elif os.path.isdir(main_dir):
        overwrite = input("Do you want to overwrite existing files? (y/n): ")
        print("")
        if overwrite.lower() in ["y", "yes"]:
            download_existing_videos = 1

    videos_num = len(playlist.video_urls)
    n = 0
    for url in playlist:
        YouTube(url).streams.filter(only_audio=True).first().download(main_dir)
        for files in os.listdir(main_dir):
            if files.endswith('.mp4'):
                n = n + 1
                print("Downloading...    " + str(n) + "/" + str(videos_num))
        if download_existing_videos == 1:
            for file in os.listdir(main_dir):
                if file.lower().endswith('.mp3'):
                    mp3_base_name = os.path.splitext(file)[0]
                    mp4_path = os.path.join(main_dir, f"{mp3_base_name}.mp4")
                    if os.path.exists(mp4_path):
                        os.remove(mp4_path)
                        print(f"Skipping: {file}")

        for file in os.listdir(main_dir):
            if re.search('mp4', file):
                mp4_path = os.path.join(main_dir, file)
                mp3_path = os.path.join(main_dir, os.path.splitext(file)[0] + '.mp3')
                new_file = AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
                if var1 == 1:
                    full_file_name = os.path.basename(mp3_path)
                    file_name = Path(full_file_name).stem
                    channel_name = YouTube(url).author
                    substring = " - Topic"
                    if substring in channel_name:
                        channel_name = channel_name.replace(" - Topic", "")
                    audioFile = eyed3.load(mp3_path)
                    audioFile.tag.artist = channel_name
                    audioFile.tag.title = file_name
                    audioFile.tag.save()
    print("Download complete!!!")

def include_author_metadata():
    if input("Do you want to include author metadata for audio files? (Y/N): ").lower() == 'y':
        return True
    else:
        return False

print("*********************Youtube Downloader************************")
print("\n")

get_link = input("Enter the URL of the video or playlist: ")

user_path = input("Enter the location where the files will be saved: ")
user_path = os.path.expanduser(user_path)

download_option = input("Select an option:\n1 Download Video\n2 Download Audio\n3 Download Playlist\n\nEnter the number: ")
print("")

if download_option == "1":
    download_file()
elif download_option == "2":
    if include_author_metadata():
        print("Author metadata will be included for audio files.")
        print("")
        var1 = 1
    else:
        print("Author metadata will not be included for audio files.")
        print("")
    download_file_mp3()
elif download_option == "3":
    if include_author_metadata():
        print("Author metadata will be included for playlist videos.")
        print("")
        var1 = 1
    else:
        print("Author metadata will not be included for playlist videos.")
        print("")
    download_playlist()
else:
    print("Invalid option selected.")
