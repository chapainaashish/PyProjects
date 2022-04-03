# Author: Aashish Sharma
# Github: https://github.com/aasis25c

from pytube import YouTube

url = str(input("Enter video url: "))
save_path = "/home/aashishsharma/Downloads/"


try:
    video = YouTube(url)
except:
    print("Connection Error!")

# If exception doesn't arrive
else:
    print(video.title)

    # example url: https://www.youtube.com/watch?v=vDHtypVwbHQ
    input("Press ENTER to download")

    print("Downloading")
    stream = video.streams.filter(file_extension='mp4').get_by_itag(22)
    stream.download(save_path)
    print("Downloaded")
q
