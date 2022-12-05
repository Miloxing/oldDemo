import youtube_dl


def down(data,name):
    ydl_opts = {
        'nooverwrites': True,
        'ignoreerrors': True,
        'retries': True,
        'outtmpl': name,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([data])