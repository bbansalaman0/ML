import pytube
url = 'https://www.youtube.com/watch?v=lTxn2BuqyzU'

youtube = pytube.YouTube(url)

streams = youtube.streams.all()
for i in streams:
    print(i)