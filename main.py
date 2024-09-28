from pytube import YouTube, Playlist
from pytube.cli import on_progress
from moviepy.editor import VideoFileClip, AudioFileClip
import shutil
from pathlib import Path
import re
import eyed3
import os
from tkinter import filedialog, Tk

var1 = 0

root = Tk()
root.withdraw()

def download_video(video_url, download_path):
    try:
        yt = YouTube(video_url, on_progress_callback=on_progress)
        streams = yt.streams.filter(progressive=True)
        stream_list = list(enumerate([f"{stream.resolution} - {stream.mime_type}" for stream in streams]))
        
        print("Available resolutions:")
        for i, stream in stream_list:
            print(f"{i}. {stream}")
        
        resolution_choice = int(input("Enter the number of the desired resolution: "))
        chosen_stream = streams[resolution_choice]
        
        mp4_video = chosen_stream.download()
        vid_clip = VideoFileClip(mp4_video)
        vid_clip.close()
        shutil.move(mp4_video, download_path)
        print("\rDownload complete!  ")
    except Exception as e:
        print(f"Error downloading video: {e}")

def download_audio(video_url, download_path, include_metadata):
    try:
        mp3_audio = YouTube(video_url, on_progress_callback=on_progress).streams.filter(only_audio=True).first().download()
        audio_clip = AudioFileClip(mp3_audio)
        full_file_name = os.path.basename(mp3_audio)
        file_name = Path(full_file_name).stem
        mp3_converted = f'{file_name}.mp3'
        audio_clip.write_audiofile(mp3_converted)
        
        if include_metadata:
            add_metadata(mp3_converted, video_url, file_name)
        
        shutil.move(mp3_converted, download_path)
        audio_clip.close()
        os.remove(full_file_name)
        print("Download complete!!!")
    except Exception as e:
        print(f"Error downloading audio: {e}")

def add_metadata(file_path, video_url, file_name):
    try:
        channel_name = YouTube(video_url).author.replace(" - Topic", "")
        audio_file = eyed3.load(file_path)
        audio_file.tag.artist = channel_name
        audio_file.tag.title = file_name
        audio_file.tag.save()
    except Exception as e:
        print(f"Error adding metadata: {e}")

def download_playlist(playlist_url, download_path, include_metadata):
    try:
        playlist = Playlist(playlist_url)
        playlist_name = playlist.title
        main_dir = os.path.join(download_path, playlist_name)
        
        if not os.path.isdir(main_dir):
            os.makedirs(main_dir)
            print("Download folder for the playlist has been created!")
        else:
            overwrite = input("Do you want to overwrite existing files? (y/n): ").lower()
            if overwrite not in ["y", "yes"]:
                return
        
        for video in playlist.videos:
            video.streams.filter(only_audio=True).first().download(main_dir)
            for file in os.listdir(main_dir):
                if re.search('mp4', file):
                    mp4_path = os.path.join(main_dir, file)
                    mp3_path = os.path.join(main_dir, os.path.splitext(file)[0] + '.mp3')
                    with AudioFileClip(mp4_path) as new_file:
                        new_file.write_audiofile(mp3_path)
                    os.remove(mp4_path)
                    
                    if include_metadata:
                        full_file_name = os.path.basename(mp3_path)
                        file_name = Path(full_file_name).stem
                        add_metadata(mp3_path, video.watch_url, file_name)
                    
        print("Download complete!!!")
    except Exception as e:
        print(f"Error downloading playlist: {e}")

def include_author_metadata():
    return input("Do you want to include author metadata for audio files? (Y/N): ").lower() == 'y'

def main():
    print("*********************YouTube Downloader************************\n")
    get_link = input("Enter the URL of the video or playlist: ")
    root.iconbitmap("icon_logo.ico")
    user_path = filedialog.askdirectory(initialdir="/", title="Select the location where the files will be SAVED!")
    print(f"Files will be saved in {user_path}\n")
    
    download_option = input("Select an option:\n1. Download Video\n2. Download Audio\n3. Download Playlist\n\nEnter the number: ")
    print("")
    
    if download_option == "1":
        download_video(get_link, user_path)
    elif download_option == "2":
        var1 = include_author_metadata()
        if var1:
            print("Author metadata will be included for audio files.\n")
        download_audio(get_link, user_path, var1)
    elif download_option == "3":
        var1 = include_author_metadata()
        if var1:
            print("Author metadata will be included for playlist videos.\n")
        download_playlist(get_link, user_path, var1)
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
