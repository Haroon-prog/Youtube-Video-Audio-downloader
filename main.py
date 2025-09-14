from pytubefix import YouTube
import os 


#"https://pytube3.readthedocs.io/en/latest/user/quickstart.html#"       #--------> pytube docs 

print("\t\tWELCOME TO YOUTUBE VIDEO/AUDIO DOWNLOADER PROGRAM !😃😉")
url = str(input("Enter the video url(link) you want to download⬇️\n"))
selection=str(input("Do you want Video or Audio ?\n"))

#yt=YouTube("https://www.youtube.com/shorts/sxmTTS4qros")        #for testing
yt=YouTube(url)



print("video title: " , yt.title)
print("video thumbnail: ", yt.thumbnail_url)


#print(yt.streams.filter(progressive=True))    #audio + video
#st=yt.streams.filter(only_audio=True)     #audio only
#st.first().download()    #first from the streams will be dwl

#yt.streams.filter(progressive=True).get_highest_resolution().download()      # audio + video  + highest resolution (max 720p)

def video_audio_dwl(yt):
    stream_to_dwl=yt.streams.filter(progressive=True)
    return stream_to_dwl.get_highest_resolution().download("downloads/videos")

def audio_dwl(yt):
    st = yt.streams.filter(only_audio=True)
    return  st.first().download("downloads/audios")


if selection.lower()=="video":
    os.makedirs("downloads/videos", exist_ok=True)
    video_audio_dwl(yt)
    print("video downloaded!  \n check downloads/videos folder")
elif selection.lower()=="audio":
    os.makedirs("downloads/audios", exist_ok=True)
    audio_dwl(yt)
    print("Audio downloaded! \n check downloads/audios folder")