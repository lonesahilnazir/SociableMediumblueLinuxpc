from pytube import YouTube
from pydub import AudioSegment

# Function to download YouTube video and convert to MP3
def download_youtube_audio(url):
    # Download the video
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()

    # Convert to MP3
    audio = AudioSegment.from_file(out_file)
    mp3_file = out_file.rsplit('.', 1)[0] + '.mp3'
    audio.export(mp3_file, format='mp3')

    print(f"Downloaded and converted: {mp3_file}")

# Example usage
video_url = 'https://www.youtube.com/watch?v=59KeWIzn-Jo'
download_youtube_audio(video_url)

# https://www.youtube.com/watch?v=59KeWIzn-Jo&feature=youtu.be