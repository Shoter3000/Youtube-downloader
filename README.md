# Youtube Downloader

The following program is a Python program that allows users to download videos and audio files from YouTube. It utilizes various Python libraries like `pytube`, `moviepy`, `eyed3`, and `tkinter`. The script provides options for downloading individual videos, audio files, or entire playlists from YouTube.

## Dependencies

Before running the program, ensure you have the following dependencies installed:

- `pytube`: A lightweight and easy-to-use library for downloading YouTube videos.
- `moviepy`: A library for video editing, including audio extraction and modification.
- `eyed3`: A library for working with audio file metadata.
- `tkinter`: A standard Python interface for creating graphical user interfaces (GUIs).

You can install these dependencies using `pip`:

```
pip install pytube moviepy eyed3
```

## Script Explanation

The script starts by importing the necessary libraries and creating some global variables. The main functionalities are divided into several functions, each handling a specific task.

1. **Download Video Function (`download_file`):**
   This function downloads a video from the given URL using the `pytube` library. It then moves the downloaded video to the selected directory using the `shutil` library.

2. **Download Audio Function (`download_file_mp3`):**
   This function downloads the audio-only version of a video from the given URL. It converts the video to MP3 format using the `moviepy` library and saves the converted audio file to the selected directory. If the user chooses to include author metadata, it fetches the video's author and sets it as the artist's name in the MP3 file using the `eyed3` library.

3. **Download Playlist Function (`download_playlist`):**
   This function downloads all the videos in a playlist. It loops through the videos in the playlist, downloads the audio-only version, converts them to MP3 format, and moves them to a folder named after the playlist. Similar to the previous function, it also provides the option to include author metadata for each audio file.

4. **Include Author Metadata Function (`include_author_metadata`):**
   This function asks the user whether they want to include author metadata for audio files. It returns a boolean value based on the user's choice.

5. **Validate YouTube URL Function (`valid_youtube_url`):**
   This function checks whether the provided URL is a valid YouTube video or playlist URL using regular expressions. It returns a boolean value indicating whether the URL is valid and whether it corresponds to a video or playlist.

6. **Main Execution:**
   The script starts by prompting the user to input the YouTube URL and the location where the downloaded files will be saved. It then asks the user to select one of the three options: Download Video, Download Audio, or Download Playlist. Based on the user's selection, the respective function is called to perform the download.

## How to Use

1. Run the script.
2. Input the YouTube URL when prompted.
3. Select the location where the downloaded files will be saved using the file dialog.
4. Choose one of the three options: Download Video, Download Audio, or Download Playlist.
5. If downloading audio or a playlist, the script will prompt whether to include author metadata for the audio files.
6. The download progress will be displayed for each video or audio file.
7. Once the download is complete, the script will print "Download complete" or "Download complete!!!" depending on the chosen option.

**Note:** The script is limited to the functionalities provided by the `pytube`, `moviepy`, and `eyed3` libraries. If there are any changes to YouTube's website structure or API, the script might require updates to function correctly.

Remember to comply with YouTube's terms of service and respect copyright rules when using this script. Only download content for which you have the necessary permissions or rights.
