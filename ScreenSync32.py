#Before Starting Program Type

# pip3 install pyautogui
#pip3 install opencv-python
#pip3 install numpy

#in CMD
from multiprocessing import*
import cv2
import numpy as np
from time import sleep
import pyautogui
import shutil
from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile as save_as
from tkinter import Tk
from PIL import Image, ImageTk
import os


#Main function to record screen
def record_screen_v():
    SCREEN_SIZE = tuple(pyautogui.size())
    # this defines the codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # User can change fps
    fps = 9.0
    # create the video write object
    out = cv2.VideoWriter("output.avi", fourcc, fps, (SCREEN_SIZE))
    # the time you want to record in seconds
    record_seconds = 100000
    for i in range(int(record_seconds * fps)):
        # takes screenshot
        img = pyautogui.screenshot()
        # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
        # convert image colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # write the frame
        out.write(frame)
        # if the user clicks the button stop recording, it exits
        if (open("cache","r").read() == "stop"):
            open("cache","w").write("")
            break
    cv2.destroyAllWindows()
    out.release()

#This function start the recording
def rec():
    if ("__cache__" in os.listdir()):
        open("__cache__","w").write("")
    else:
        open("__cache__","a").write("")
    while(0<1):
        y=open("__cache__","r").read()
        if (y == "do"):
            record_screen_v()
        else:
            sleep(2)

#function for releasing recorded video
def main_l():
    def rls():
        t = save_as()
        l="output.avi"
        if (t != None):
            t = t.name+".avi"
            shutil.copy(l,t)
            p3.place(x=150,y=1000)
            messagebox.showinfo("File saved","Your file has been saved")
    
    #checking the presence of cache file in file system
    if ("cache" in os.listdir()):
        open("cache","w").write("")
    else:
        open("cache","a").write("")

    
    #For start recording, this function writes "" in cache file, due to which the main.py file starts recording the screen
    def ply():
        open("__cache__","w").write("do")
        open("cache","w").write("")
        p2.place(x=70,y=80)
        p1.place(x=150,y=1000)
    
    #For stop recording, this function writes "stop" in cache file, due to which the main.py file stop recording the screen
    def stp():
        open("__cache__","w").write("")
        open("cache","w").write("stop")
        p1.place(x=70,y=80)
        p3.place(x=45,y=170)
        p2.place(x=150,y=1000)

    t= Tk()
    t.title("ScreenSync32")
    icon_image = Image.open("logo.png")
    icon_photo = ImageTk.PhotoImage(icon_image)
    t.iconphoto(True, icon_photo)
    t.geometry("300x550")
    t.resizable(0,0)
    Label(t, background="#77B0AA", height=5, width=500).place(x=0,y=0)
    Label(t, text="SCREENSYNC32", background="#77B0AA" ,foreground="#135D66",activebackground="white", activeforeground="black",font=('Open San', 25, 'bold')).place(x=13,y=10)
    Label(t, background="#cae0de", height=35, width=500).place(x=0,y=60)
    p1= Button(t, text="Start Recording",font=('ariel',15) , command=ply, background="#86A789",foreground="#4F6F52", activebackground="white", activeforeground="black")
    p2= Button(t, text="Stop Recording", font=('ariel',15) , command=stp, background="#FA7070",foreground="#DF2E38", activebackground="white", activeforeground="black")
    p3= Button(t, text="Save Your Recording",  font=('ariel',15) , command=rls, background="#135D66",foreground="#E3FEF7", activebackground="white", activeforeground="black")
    p1.place(x=70,y=80)
    p2.place(x=1500,y=1000)
    t.mainloop()

if __name__ == '__main__':
    t= Process(target=main_l)
    t2=Process(target=rec)
    t.start()
    t2.start()
    t.join()
