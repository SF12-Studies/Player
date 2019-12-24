from tkinter import *
import subprocess
from pygame import mixer
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
from tkinter import messagebox
import os
from pygame import error
import json
import pafy
import time

start = time.time()

mixer.init()



def setvolume():
    slider = vol.get() / 100
    jsonvol = vol.get()
    mixer.music.set_volume(slider)
    filenamejsonvol = 'data/settings/main.json'

    def writevol():
        with open(filenamejsonvol, 'r') as voljson:
            data = json.load(voljson)
            data['vol'] = jsonvol

        os.remove(filenamejsonvol)
        with open(filenamejsonvol, 'w') as f:
            json.dump(data, f, indent=4)

    vol.bind('<ButtonRelease-1>', lambda x: writevol())


def volpl():
    vol.place(x=830, y=430)
    spkico.place_forget()


def volleave():
    vol.place_forget()
    spkico.place(x=850, y=455)


def Start():
    try:
        x = filename1
        gui.title(x + '   ▶    Playing')
        inf = replaybut.cget('image')
        print(inf)
        if inf == 'pyimage7':
            mixer.music.play(loops=1)
            buttonPlay.config(command=StartAl)
        elif inf == 'pyimage14':
            mixer.music.play(loops=1)
            buttonPlay.config(command=StartAl)
        elif inf == 'pyimage16':
            mixer.music.play(loops=306090)
            buttonPlay.config(command=StartAl)
        elif inf == 'pyimage16':
            mixer.music.play(loops=306090)
    except NameError:
        try:
            global filename2
            filenamejsonre = 'data/settings/main.json'
            with open(filenamejsonre, 'r') as f:
                 data = json.load(f)
                 load = data['recent']
            mixer.music.load(load)
            filename2 = os.path.splitext(os.path.basename(load))[0]
            x = filename2
            gui.title(x + '   ▶    Playing')
            inf = replaybut.cget('image')
            if inf == 'pyimage7':
                mixer.music.play(loops=1)
                buttonPlay.config(command=StartAl)
            elif inf == 'pyimage14':
                mixer.music.play(loops=1)
                buttonPlay.config(command=StartAl)
            elif inf == 'pyimage16':
                mixer.music.play(loops=306090)
                buttonPlay.config(command=StartAl)
            elif inf == 'pyimage16':
                mixer.music.play(loops=306090)
        except error:
            pass


def StartAl():
    x = filename1
    try:
        gui.title(x + ' ▶    Playing')
        mixer.music.unpause()
    except error:
        try:
            x = filename2
            gui.title(x + ' ▶    Playing')
            mixer.music.unpause()
        except error:
            pass


def Pause():
    gui.title('Alpha Player')
    mixer.music.pause()


def Load():
    global filename1
    load = filedialog.askopenfilename(title="Select file", filetypes=[("Sound Files", "*.mp3 *.wav *.ogg *.oga")])
    filename1 = os.path.splitext(os.path.basename(load))[0]
    mixer.music.load(load)
    buttonPlay.config(command=Start)
    filenamejson = 'data/settings/main.json'
    if load == '':
        pass
    else:
        with open(filenamejson, 'r') as f:
            data = json.load(f)
            data['recent'] = load

        os.remove(filenamejson)
        with open(filenamejson, 'w') as f:
            json.dump(data, f, indent=4)


def LoadVid():
    file = filedialog.askopenfilename(title="Select file", filetypes=[("Video Files", "*.mp4 *.mov *.mkv *.avi *.3gp *.mpg *.mpeg")])


def ReplayOff():
    mixer.music.play(loops=1)
    replaybut.configure(command=ReplayOn, image=photoReplayOn)
    filenamejson = 'data/settings/main.json'
    with open(filenamejson, 'r') as f:
        data = json.load(f)
        data['replay'] = "off"

    os.remove(filenamejson)
    with open(filenamejson, 'w') as f:
        json.dump(data, f, indent=4)


def ReplayOn():
    mixer.music.play(loops=306090)
    replaybut.configure(command=ReplayOff, image=photoReplayOff)
    filenamejson = 'data/settings/main.json'
    with open(filenamejson, 'r') as f:
        data = json.load(f)
        data['replay'] = "on"

    os.remove(filenamejson)
    with open(filenamejson, 'w') as f:
        json.dump(data, f, indent=4)


filenamemain = 'data/settings/main.json'
with open(filenamemain, 'r') as o:
    dataREP = json.load(o)
    dataREP = dataREP['replay']
with open(filenamemain, 'r') as v:
    VOLJSON = json.load(v)
    VOL = VOLJSON['vol']


def ColText():
    with open(filenamejson, 'r') as f:
        data = json.load(f)
        data = data['theme']
    if data == 'LightBg':
        string = '#dadee7'
        return string
    elif data == 'DarkBg':
        string = '#090909'
        return string
    else:
        print('JSON Error. 404.')


def ColTop():
    with open(filenamejson, 'r') as f:
        data = json.load(f)
        data = data['theme']
    if data == 'LightBg':
        string = '#dadee7'
        return string
    elif data == 'DarkBg':
        string = '#050505'
        return string
    else:
        print('JSON Error. 404.')


def ColBot():
    with open(filenamejson, 'r') as f:
        data = json.load(f)
        data = data['theme']
    if data == 'LightBg':
        string = '#dadee7'
        return string
    elif data == 'DarkBg':
        string = '#070707'
        return string
    else:
        print('JSON Error. 404.')


def settings():
    def LightCol():
        DoLBut.config(image = photoImgDkThOff, command=DarkCol)
        spkico.config(image = photoLoadSPK)
        buttonLoadM.config(image=photoLoadM)
        buttonLoadV.config(image=photoLoadV)
        buttonPlay.config(image=photoImg)
        buttonPause.config(image=photoPause)
        buttonLoadM.config(bg='#dadee7')
        buttonLoadV.config(bg='#dadee7')
        buttonPlay.config(bg='#dadee7')
        buttonPause.config(bg='#dadee7')
        background_label.config(bg = 'white')
        filenamejson = 'data/settings/settings.json'
        with open(filenamejson, 'r') as f:
            data = json.load(f)
            data['theme'] = "LightBg"

        os.remove(filenamejson)
        with open(filenamejson, 'w') as f:
            json.dump(data, f, indent=4)

    def DarkCol():
        DoLBut.config(image = photoImgDkThOn, command=LightCol)
        spkico.config(image = photoLoadSPKDark)
        buttonLoadM.config(image=photoLoadMDark)
        buttonLoadV.config(image=photoLoadVDark)
        buttonPlay.config(image=photoImgdark)
        buttonPause.config(image=photoPausedark)
        buttonLoadM.config(bg='#050505')
        buttonLoadV.config(bg='#050505')
        buttonPlay.config(bg='#070707')
        buttonPause.config(bg='#070707')
        background_label.config(bg='black')
        filenamejson = 'data/settings/settings.json'
        with open(filenamejson, 'r') as f:
            data = json.load(f)
            data['theme'] = "DarkBg"

        os.remove(filenamejson)
        with open(filenamejson, 'w') as f:
            json.dump(data, f, indent=4)

    guiset = Toplevel()
    guiset.iconbitmap('data/img/icon/settings.ico')
    guiset.geometry('230x250')
    guiset.title('Settings')
    guiset.config(bg='#010014')

    TextTheme = Label(guiset, text='Dark Theme', bg='#010014', fg='silver', font=('Arial', 10, 'bold'))
    DoLBut = Button(guiset, bd = 0, highlightthickness = 0, image = photoImgDkThOff, command=DarkCol)
    TextTheme.place(y=40, x=20)
    DoLBut.place(x=130, y=25)
    with open(filenamejson, 'r') as rr:
        data = json.load(rr)
        data = data['theme']
    if data == 'DarkBg':
        DarkCol()
    elif data == 'LightBg':
        pass


def about():
    guiab = Toplevel()
    guiab.config(bg='#010014')
    guiab.title('About')

    Ban = Label(guiab, bg='#010014', image = photoBan2)
    Ban.pack()

    text = Label(guiab, fg = '#0ea5ff', text="\nThis Player is an audio & video player.\nThe features are 'loop', in-app volume changing¹, high bit-rate²\naudio playing & 'Recent' for when the user forgets to select a file,\nthey can play the most recent one available. It supports mp3, wav, ogg & oga for audio.\n\n\n¹ This is seperate from the system volume.\n² Depends on what the original file bit-rate are.\n\nArtwork by SF12\n\n Credit\n_____\nPython Software Foundation\npygame\n\n\nVersion: 0.1.2    ", bg='#010014')
    text.pack()


def Menu():
    guimen = Toplevel()
    guimen.config(bg='#aeaeae')
    guimen.wm_overrideredirect(1)

    def setopen():
        guimen.destroy()
        settings()

    def aboutopen():
        about()
        guimen.destroy()

    def video():
        print("")

    setbut = Button(guimen, text='Preferences', command=setopen, bg='#aeaeae', relief = 'flat')
    playvid = Button(guimen, text='Video', command=lambda: video(), bg='#aeaeae', relief = 'flat')
    aboutbut = Button(guimen, text='About', command=aboutopen, bg='#aeaeae', relief = 'flat')
    quitbut = Button(guimen, text='Quit', command=gui.destroy, bg='#aeaeae', relief = 'flat')
    setbut.pack()
    playvid.pack()
    aboutbut.pack()
    quitbut.pack()
    setbut.bind('<Enter>', lambda x: setbut.config(bg='#0b00e4'))
    playvid.bind('<Enter>', lambda x: playvid.config(bg='#0b00e4'))
    aboutbut.bind('<Enter>', lambda x: aboutbut.config(bg='#0b00e4'))
    quitbut.bind('<Enter>', lambda x: quitbut.config(bg='#0b00e4'))
    setbut.bind('<Leave>', lambda x: setbut.config(bg='#aeaeae'))
    playvid.bind('<Leave>', lambda x: playvid.config(bg='#aeaeae'))
    aboutbut.bind('<Leave>', lambda x: aboutbut.config(bg='#aeaeae'))
    quitbut.bind('<Leave>', lambda x: quitbut.config(bg='#aeaeae'))
    gui.bind('<Button-1>', lambda x: guimen.destroy())


gui = Tk()
gui.geometry("900x550")
gui.title("Player")

filenamejson = 'data/settings/settings.json'
with open(filenamejson, 'r') as f:
    data = json.load(f)
    data = data['theme']
    if data == 'DarkBg':
        color = 'black'
    elif data == 'LightBg':
        color = 'white'
    print(data)
background_label = Label(gui, bg=color)
background_label.place(relwidth=1, relheight=1)

Squ = Label(gui)

img = Image.open('data/img/icon/play.png')
img = img.resize((50, 50))
photoImg = ImageTk.PhotoImage(img)

img = Image.open('data/img/icon/DkThOn.png')
img = img.resize((90, 56))
photoImgDkThOn = ImageTk.PhotoImage(img)

img = Image.open('data/img/icon/DkThOff.png')
img = img.resize((90, 56))
photoImgDkThOff = ImageTk.PhotoImage(img)

img = Image.open('data/img/icon/playdark.png')
img = img.resize((50, 50))
photoImgdark = ImageTk.PhotoImage(img)

img = Image.open('data/img/icon/pause.png')
img = img.resize((50, 50))
photoPause = ImageTk.PhotoImage(img)

img = Image.open('data/img/icon/pausedark.png')
img = img.resize((50, 50))
photoPausedark = ImageTk.PhotoImage(img)

img = Image.open('data/img/icon/loadmusic.png')
img = img.resize((40, 40))
photoLoadM = ImageTk.PhotoImage(img)

img = Image.open('data/img/icon/loadmusicdark.png')
img = img.resize((40, 40))
photoLoadMDark = ImageTk.PhotoImage(img)

img = Image.open('data/img/icon/loadvideo.png')
img = img.resize((40, 40))
photoLoadV = ImageTk.PhotoImage(img)

img = Image.open('data/img/icon/loadvideodark.png')
img = img.resize((40, 40))
photoLoadVDark = ImageTk.PhotoImage(img)

img = Image.open('data/img/icon/speaker.ico')
img = img.resize((30, 30))
photoLoadSPK = ImageTk.PhotoImage(img)

img = Image.open('data/img/icon/speakerDark.ico')
img = img.resize((30, 30))
photoLoadSPKDark = ImageTk.PhotoImage(img)

img = Image.open('data/img/icon/replayoff.png')
img = img.resize((20, 20))
photoReplayOff = ImageTk.PhotoImage(img)

img = Image.open('data/img/icon/replayon.png')
img = img.resize((20, 20))
photoReplayOn = ImageTk.PhotoImage(img)

img = Image.open('data/img/icon/replayondark.png')
img = img.resize((20, 20))
photoReplayOnDark = ImageTk.PhotoImage(img)

buttonLoadM = Button(gui, bg=ColTop(), fg='#dadee7', border=0)
buttonLoadM.config(image=photoLoadM, command=Load)
buttonLoadM.pack(ipadx=1)
buttonLoadM.place(y=45, x=25)

buttonLoadV = Button(gui, bg=ColTop(), fg='#dadee7', border=0)
buttonLoadV.config(image=photoLoadV, command=LoadVid)
buttonLoadV.pack(ipadx=1)
buttonLoadV.place(y=45, x=840)

buttonPlay = Button(gui, bg=ColBot(), fg='#dadee7', border=0, command=Start)
buttonPlay.config(image=photoImg)
buttonPlay.pack(ipadx=1)
buttonPlay.place(y=445, x=340)

buttonPause = Button(gui, bg=ColBot(), fg='#dadee7', border=0)
buttonPause.config(image=photoPause, command=Pause)
buttonPause.pack(ipadx=1)
buttonPause.place(y=445, x=510)

vol = Scale(gui, bg='#001014', fg='#4200ff', orient='vertical', resolution=5, relief='solid', sliderrelief = 'solid'
            , highlightthickness=0.5, font=('Tahoma', 12, ''), troughcolor='black', highlightcolor = 'grey',
              command=lambda x: setvolume())
vol.set(VOL)

# timeslider = Scale(gui, bg='#11171a', fg='NavyBlue'
#            , highlightthickness=0.5, font=('Century Gothic', 12, 'bold'), command=lambda x: settime(),
#                   orient='horizontal', resolution=1, showvalue=NO)
# timeslider.place(x=415, y=350)

spkico = Button(gui, bd=0, highlightthickness=0, command = volpl)
spkico.config(image=photoLoadSPK)
spkico.place(x=850, y=455)

replaybut = Button(gui, image=photoReplayOn, command=ReplayOn, bd=0.5, bg=ColTop())
replaybut.place(x=50, y=465)

gui.bind("<Button-3>", lambda x: Menu())

vol.bind("<Leave>", lambda x: volleave())

with open(filenamejson, 'r') as f:
    data = json.load(f)
    data = data['theme']

if dataREP == 'on':
    if data == 'DarkBg':
        replaybut.config(command=ReplayOn, image=photoReplayOnDark)
    else:
        replaybut.config(command=ReplayOn, image=photoReplayOn)
if dataREP == 'off':
    replaybut.config(command=ReplayOff, image=photoReplayOff)

if data == 'DarkBg':
    spkico.config(image = photoLoadSPKDark)
    buttonLoadM.config(image=photoLoadMDark)
    buttonLoadV.config(image=photoLoadVDark)
    buttonPlay.config(image=photoImgdark)
    buttonPause.config(image=photoPausedark)
else:
    pass

end = time.time()
elapsed = end - start
print(elapsed)

# gui.bind("<ButtonRelease-1>", dnd_start(source=))

gui.mainloop()
