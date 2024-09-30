from flask import Flask,render_template,request
from pytube import YouTube
import os
from moviepy.editor import *
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('yt.html')

@app.route("/my_form",methods=["POST"])
def user():
    g=request.form['type']
    if g=="video":
        f=request.form['radio']
        if f=="144p":
            data="download successfully"
            if request.method=="POST":
                link=request.form['fname']
                print(link)
                youtubeObject = YouTube(link)
                youtubeObject = youtubeObject.streams.filter(res="144p").first()
                try:
                    youtubeObject.download()
                    return render_template('yt.html',data=data)
                except:
                    return
        elif f=="240p":
            data="download successfully"
            if request.method=="POST":
                link=request.form['fname']
                print(link)
                youtubeObject = YouTube(link)
                youtubeObject = youtubeObject.streams.filter(res="240p").first()
                try:
                    youtubeObject.download()
                    return render_template('yt.html',data=data)
                except:
                    return
        elif f=="360p":
            data="download successfully"
            if request.method=="POST":
                link=request.form['fname']
                print(link)
                youtubeObject = YouTube(link)
                youtubeObject = youtubeObject.streams.filter(res="360p").first()
                try:
                    youtubeObject.download()
                    return render_template('yt.html',data=data)
                except:
                    return
        elif f=="480p":
            data="download successfully"
            if request.method=="POST":
                link=request.form['fname']
                print(link)
                youtubeObject = YouTube(link)
                youtubeObject = youtubeObject.streams.filter(res="480p").first()
                try:
                    youtubeObject.download()
                    return render_template('yt.html',data=data)
                except:
                    return
        elif f=="720p":
            data="download successfully"
            if request.method=="POST":
                link=request.form['fname']
                print(link)
                youtubeObject = YouTube(link)
                youtubeObject = youtubeObject.streams.filter(res="720p").first()
                try:
                    youtubeObject.download()
                    return render_template('yt.html',data=data)
                except:
                    youtubeObject = YouTube(link)
                    youtubeObject = youtubeObject.streams.get_highest_resolution()
                    youtubeObject.download()
                    return
        elif f=="1080p":
            data="download successfully"
            if request.method=="POST":
                link=request.form['fname']
                print(link)
                youtubeObject = YouTube(link)
                youtubeObject = youtubeObject.streams.filter(res="1080p").first()
                try:
                    youtubeObject.download()
                    return render_template('yt.html',data=data)
                except:
                    youtubeObject = YouTube(link)
                    youtubeObject = youtubeObject.streams.get_highest_resolution()
                    youtubeObject.download()
                    return
        else:
            data="download successfully"
            if request.method=="POST":
                link=request.form['fname']
                print(link)
                youtubeObject = YouTube(link)
                youtubeObject = youtubeObject.streams.get_highest_resolution()
                try:
                    youtubeObject.download()
                    return render_template('yt.html',data=data)
                except:
                    youtubeObject = YouTube(link)
                    youtubeObject = youtubeObject.streams.get_highest_resolution()
                    youtubeObject.download()
                    return
    elif g=="audio":
        data="download successfully"
        if request.method=="POST":
            link=request.form['fname']
            youtubeObject = YouTube(link)
            for i in range(1):
                youtubeObject=youtubeObject.streams.get_audio_only()
                youtubeObject.download()
                g=os.path.basename(f"{youtubeObject.title}.mp4")
                ba,ex=os.path.splitext(g)
                n=ba+'.mp3'
                os.rename(g,n)
                return render_template('yt.html',data=data)
            
            #except:
             #   return render_template('yt.html',data=data)
    else:
        return render_template('yt.html',data=data)
if __name__ == "__main__":
    app.run(debug=True)
