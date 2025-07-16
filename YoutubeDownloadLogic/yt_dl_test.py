import os
import yt_dlp
import re 
import concurrent.futures
# yt-dlp-2024.10.7 old version

def fetch_video_status(entry):
    """Fetch status of individual video entry (parallelized)."""
    if entry:
        return f"Video: {entry.get('title', 'Unknown')} - Status: Success"
    return "Invalid Entry - Status: Failed"


# Clean illegal characters for Windows filenames
def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name)


def get_video_info(url):
    """Fetch video details without downloading."""
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'socket_timeout': 10,  # Handle slow responses
        'concurrent_fragment_downloads': 1,  # Prevent throttling
        'sleep_interval': 2,
        'force-ipv4': True,
        'extract_flat': True,  # Prevents fetching full metadata
        'force_generic_extractor': True  # Uses webpage data instead of API
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            if 'entries' in info:  # Playlist detected
                video_entries = info['entries']
                print(f"\nPlaylist Detected: {info.get('title', 'Unknown Playlist')} - {len(video_entries)} videos")

                # **Parallel Processing for Speed**
                with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
                    results = executor.map(fetch_video_status, video_entries)
                    for result in results:
                        print(result)  # Print as each finishes
            else:  # Single video
                print(f"Video: {info.get('title', 'Unknown')} - Status: Success")
        except yt_dlp.utils.DownloadError:
            print(f"Error retrieving info for: {url}")

    return info

def download_audio(url, base_output_path="E://"):
    """Downloads audio from a YouTube video using yt-dlp and embeds metadata."""

    info = get_video_info(url)
    if not info:
        print("Failed to retrieve video info. Exiting.")
        return
    
    print("\nVideo Information:")
    print(f"Title: {info.get('title', 'Unknown')}")
    print(f"Uploader: {info.get('uploader', 'Unknown')}")
    print(f"Duration: {info.get('duration', 'Unknown')} seconds")
    print(f"View Count: {info.get('view_count', 'Unknown')}")
    print(f"Likes: {info.get('like_count', 'Unknown')}")
    print(f"Description: {info.get('description', 'No description')[:200]}...")

    # confirm = input("\nProceed with download? (y/n): ").strip().lower()
    # if confirm != 'y':
    #     print("Download canceled.")
    #     return
    
    
    # Determine the folder name (Playlist title or "Unknown Playlist" for single videos)
    playlist_name = info.get('title', 'Unknown Playlist').strip()
    playlist_folder = os.path.join(base_output_path, playlist_name)
    # Ensure the folder exists
    os.makedirs(playlist_folder, exist_ok=True)


    # # Determine the folder name
    # playlist_name = sanitize_filename(info.get('title', 'Unknown Playlist').strip())
    # playlist_folder = os.path.join(base_output_path, playlist_name)

    # Ensure the folder exists
    os.makedirs(playlist_folder, exist_ok=True)
    

    ydl_opts = {
        'outtmpl': f'{playlist_folder}/%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'extract_audio': True,
        'audio-format': 'mp3',
        'audio-quality': '0',
        'addmetadata': True,
        
        'socket_timeout': 10,  # Handle slow responses
        'concurrent_fragment_downloads': 1,  # Prevent throttling
        'sleep_interval': 2,
        'max_sleep_interval': 8,
        'force-ipv4': True,
        'ignoreerrors': True,  # Skip failed downloads and continue
        # 'extract_flat': True,  # Prevents fetching full metadata
        # 'force_generic_extractor': True,  # Uses webpage data instead of API
        'postprocessors': [
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'},
            {'key': 'FFmpegMetadata'},
            {'key': 'EmbedThumbnail'}
        ],
        # 'writeinfojson': True,
        # 'writedescription': True,
        'writethumbnail': True,  # Save thumbnail if available
        'writecomments': True,
        # 'writesubtitles': True,
        # 'subtitleslangs': ['all'],
        # 'embedsubtitles': True,
        'embedthumbnail': True,
        'noplaylist': False,
        'writeplaylistmetafiles': True,
        'quiet': False,
        # 'extractor_args': {'youtube': {'player_client': 'web'}}
    }

    status = "Success"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print(f"Download complete! Files saved in: {playlist_folder}")
        except Exception as e:
            print(f"Download error: {e}")  # Logs the issue but doesn't stop execution
        finally:
            print(f"Processed Download: {playlist_name}")

if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL or Playlist URL: ")
    download_audio(video_url)
    print("Audio download complete!")
