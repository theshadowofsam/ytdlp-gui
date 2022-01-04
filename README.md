# ytdlp-gui
A tkinter based GUI that uses a yt-dlp script  
Downloads yt-dlp format 250 (high enough quality) as webm and converts to mp3 using FFmpeg
## Dependencies  
**[youtube-dlp](https://github.com/yt-dlp/yt-dlp#installation)**  
**[FFmpeg](https://www.ffmpeg.org/download.html)**

## Usage  
Python 3.10 and above  
dlw.py is just a graphical interface  
  
dlp.py is the actual download script. It can be called standalone on a command line -OR- 
with a space separated list of youtube links such as "python3 dlp.py https://www.youtube.com/watch?v=-0Ao4t_fe0I https://www.youtube.com/watch?v=vmOvRY8XACw"  
  
downloading the webm usually doesnt take too long as long as your internet is usable and yt-dlp is up to date  
FFmpeg takes a while to extract long videos to mp3  
in my testing it took a minute or two for a 3 hour video to be converted
