import os

# YouTube Stream Key
YOUTUBE_RTMP = "rtmp://a.rtmp.youtube.com/live2/YOUR_STREAM_KEY"

# Video File (Looped) & Radio Stream
VIDEO_FILE = "video.mp4"  # Replace with your video file
RADIO_STREAM = "https://your-radio-stream.com/live"  # Replace with your radio URL

# FFmpeg Command to Mix Video & Radio Stream
cmd = f"ffmpeg -re -stream_loop -1 -i '{VIDEO_FILE}' -re -i '{RADIO_STREAM}' \
       -c:v libx264 -preset veryfast -b:v 4500k -maxrate 4500k -bufsize 9000k \
       -c:a aac -b:a 128k -ar 44100 -f flv {YOUTUBE_RTMP}"

# Run FFmpeg Command
os.system(cmd)
