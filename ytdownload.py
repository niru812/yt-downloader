from pytube import YouTube as yt
from tkinter import *
import os


ui= Tk()
ui.title("YT Downloader")
ui.resizable(0,0)
ui.geometry("700x400")
n=1

def get_link():
    try:
        yt(text.get())
        error.place_forget()
        sel1.config(state='normal')
        sel2.config(state='normal')
    except:
        error.place(x=210,y=69)
    return text.get()

def uniquify(path):
    base, ext= os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = base + f" ({str(counter)})" + ext
        counter += 1
    return path

def start():
    link=text.get()
    vdo= yt(link)
    choice1=v.get()
    global n
    if choice1==1:
        stream=vdo.streams.get_audio_only()
        out_file=stream.download(output_path=r"D:\ytdownloaded")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        try:
            os.rename(out_file, new_file)
        except FileExistsError:
            new_file=uniquify(new_file)
            os.rename(out_file, new_file)
    elif choice1==2:
        quality=res.get()
        vdostream=vdo.streams.get_by_resolution(quality)
        out_file=vdostream.download(output_path=r"D:\ytdownloaded")
        base, ext = os.path.splitext(out_file)
        new_file = base + f" {quality}" + ext
        try:
            os.rename(out_file, new_file)
        except FileExistsError:
            new_file=uniquify(new_file)
            os.rename(out_file, new_file)
       
def mp3():
    try:
        drop.destroy()
    except NameError:
        pass

def mp4():
    link=get_link()
    vdo=yt(link)
    resoln=[]
    for stream in vdo.streams.filter(subtype="mp4",progressive="True"):
        if stream.resolution is None:
            continue
        else:
            resoln.append(int(stream.resolution[:-1]))
    resoln= sorted(set(resoln))
    resoln= [str(i) + 'p' for i in resoln]
    global res
    res= StringVar()
    res.set("Choose video resolution:")
    global drop
    drop=OptionMenu(ui,res,*resoln)
    drop.place(x=250,y=140)

url= Label(ui,text="Enter Video URL : ").place(x=110,y=50)
text=StringVar()
e1= Entry(ui,textvariable=text,width=60)
e1.place(x=210,y=50)
getlink=Button(ui,text="Enter",command=get_link,width=5)
getlink.place(x=600,y=45)
error= Label(ui,text="Please enter a valid youtube url",fg="red",font=('Aral',8))


v =IntVar()
select= Label(ui,text="Select output format:").place(x=110,y=90)
sel1=Radiobutton(ui, 
               text="mp3", 
               variable=v, 
               value=1,
               command=mp3,state='disabled')
sel1.place(x=250,y=90)
sel2=Radiobutton(ui, 
               text="mp4", 
               variable=v, 
               value=2,
               command=mp4,state='disabled')
sel2.place(x=320,y=90)

download= Button(ui,text="Download",command=start,width=20)
download.place(x=263,y=200)

ui.mainloop()

