"""
Change import based on what is breaking or working
"""

# from pytube import YouTube
# from pytubefix import YouTube

# youtubeObject = YouTube('https://www.youtube.com/watch?v=DASMWPUFFP4')

# youtubeObject = youtubeObject.streams.get_highest_resolution()

# youtubeObject.download()


"""
Worked on March 12, 2025
- no meta data
"""
# import yt_dlp

# def download_audio(url, output_path="."):
#     """Downloads audio from a YouTube video using yt-dlp.

#     Args:
#         url (str): The URL of the YouTube video.
#         output_path (str): The directory to save the audio file.
#     """
#     ydl_opts = {
#         'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save as video title
#         'format': 'bestaudio/best',  # Get the best available audio format
#         'extract_audio': True,  # Extract only audio
#         'audio-format': 'mp3',  # Convert to MP3
#         'noplaylist': True,  # Download only a single video, not a playlist
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',  # Set audio quality
#         }],
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])

# if __name__ == '__main__':
#     video_url = input("Enter the YouTube video URL: ")
#     download_audio(video_url)
#     print("Audio download complete!")

"""
Works stores some meta data like basic title and such
"""
# import yt_dlp

# def download_audio(url, output_path="."):
#     """Downloads audio from a YouTube video using yt-dlp and embeds metadata.

#     Args:
#         url (str): The URL of the YouTube video.
#         output_path (str): The directory to save the audio file.
#     """
#     ydl_opts = {
#         'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save as video title
#         'format': 'bestaudio/best',  # Get the best available audio format
#         'extract_audio': True,  # Extract only audio
#         'audio-format': 'mp3',  # Convert to MP3
#         'noplaylist': True,  # Download only a single video, not a playlist
#         'postprocessors': [
#             {
#                 'key': 'FFmpegExtractAudio',
#                 'preferredcodec': 'mp3',
#                 'preferredquality': '192',  # Set audio quality
#             },
#             {
#                 'key': 'FFmpegMetadata',  # Embed metadata into MP3
#             }
#         ],
#         'addmetadata': True,  # Ensure metadata is included
#         'writethumbnail': True,  # Save thumbnail if available
#         'embedthumbnail': True,  # Embed thumbnail into MP3
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])

# if __name__ == '__main__':
#     video_url = input("Enter the YouTube video URL: ")
#     download_audio(video_url)
#     print("Audio download complete with metadata embedded!")


import yt_dlp
        # 'outtmpl': f'{output_path}/%(playlist_title)s/%(uploader)s - %(title)s.%(ext)s',  

def download_audio(url, output_path="E:\\"):
    """Downloads audio from a YouTube video using yt-dlp and embeds all available metadata."""

    ydl_opts = {
        # File Naming - Includes Channel and Playlist Info
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  
        
        # Best Available Audio
        'format': 'bestaudio/best',  # Get the best available audio format
        'extract_audio': True,  # Extract only audio
        'audio-format': 'mp3',  # Convert to MP3
        'audio-quality': '0',  # Highest quality (320kbps)

        # Metadata and Thumbnails
        'addmetadata': True,  # Ensure metadata is included
        # 'writethumbnail': True,  # Download thumbnail if available
        'embedthumbnail': True,  # Embed thumbnail into MP3
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',  # Adjust as needed
            },
            {
                'key': 'FFmpegMetadata',  # Embed metadata into MP3
            },
            {
                'key': 'EmbedThumbnail',  # Embed thumbnail in MP3
            }
        ],

        # Additional Metadata
        'writeinfojson': True,  # Save full metadata JSON file
        'writedescription': True,  # Save video description as a .description file
        'writeannotations': True,  # Save annotations
        'writecomments': True,  # Save all comments (if available)
        'writesubtitles': True,  # Download subtitles (if available)
        'subtitleslangs': ['all'],  # Get all subtitle languages
        'embedsubtitles': True,  # Embed subtitles (if available)

        # Playlist & Channel Info
        'noplaylist': False,  # Allow playlist downloading
        'writeplaylistmetafiles': True,  # Save playlist metadata if downloading a playlist
        'merge_output_format': 'mp3',  # Merge playlist items into MP3 if needed

        # Download Behavior
        'quiet': False,  # Show progress
        'progress_hooks': [lambda d: print(d['status']) if d['status'] == 'finished' else None],  # Hook for download status
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL or Playlist URL: ")
    download_audio(video_url)
    print("Audio download complete with full metadata, channel, and playlist info!")


# import yt_dlp
# import concurrent.futures
# import os

# def download_audio(video_url, output_path):
#     """Downloads audio from a YouTube video into the specified folder."""
#     ydl_opts = {
#         'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save in playlist folder
#         'format': 'bestaudio/best',
#         'audio-quality': '0',  # Highest quality (320kbps)
#         'addmetadata': True,  # Ensure metadata is included
#         'embedthumbnail': True,  # Embed thumbnail into MP3
#         'extract_audio': True,
#         'writecomments': True,  # Save all comments (if available)
#         'audio-format': 'mp3',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([video_url])

# def download_playlist(playlist_url, max_threads=4, base_output_path="."):
#     """Extracts playlist info, creates a folder, and downloads all songs in it."""
#     ydl_opts = {'quiet': True, 'extract_flat': True, 'force_generic_extractor': True}

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         playlist_info = ydl.extract_info(playlist_url, download=False)

#     if 'entries' in playlist_info:
#         video_urls = [entry['url'] for entry in playlist_info['entries'] if entry]
#         playlist_title = playlist_info.get('title', 'Playlist')  # Get playlist name
#         playlist_folder = os.path.join(base_output_path, playlist_title)

#         os.makedirs(playlist_folder, exist_ok=True)  # Create folder if not exists

#         print(f"Downloading {len(video_urls)} videos into '{playlist_folder}'...")

#         with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
#             executor.map(lambda url: download_audio(url, playlist_folder), video_urls)
#     else:
#         print("Failed to retrieve playlist videos.")

# if __name__ == '__main__':
#     playlist_url = input("Enter the YouTube playlist URL: ")
#     download_playlist(playlist_url, max_threads=16)
#     print("All downloads complete!")


"""
Ideas to see terminal print outs in the window instead of just the terminal
"""
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
# from PyQt6.QtCore import QTextStream

# class OutputRedirector:
#     def __init__(self, text_edit):
#         self.text_edit = text_edit

#     def write(self, text):
#         self.text_edit.append(text.strip())  # Append text to QTextEdit

#     def flush(self):
#         pass  # Needed for compatibility with sys.stdout

# class PrintWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Terminal Output Redirect")
#         self.setGeometry(100, 100, 500, 300)

#         # Layout and Widgets
#         self.layout = QVBoxLayout()
#         self.text_edit = QTextEdit(self)
#         self.text_edit.setReadOnly(True)  # Prevent user editing
#         self.print_button = QPushButton("Print Something", self)
#         self.print_button.clicked.connect(self.print_message)

#         # Add widgets to layout
#         self.layout.addWidget(self.text_edit)
#         self.layout.addWidget(self.print_button)
#         self.setLayout(self.layout)

#         # Redirect stdout to QTextEdit
#         sys.stdout = OutputRedirector(self.text_edit)

#     def print_message(self):
#         print("This is redirected terminal output!")  # Goes to QTextEdit

# # Run the app
# app = QApplication(sys.argv)
# window = PrintWindow()
# window.show()
# sys.exit(app.exec())
