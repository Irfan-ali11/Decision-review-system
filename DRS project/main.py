import tkinter
from PIL import Image,ImageTk    #pip install pillow
import cv2    #pip install opencv-python
from functools import partial
import time 
import imutils
import threading #contineous running program prevent to stop


def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("racingpending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # 2. Wait for 1 second
    time.sleep(1.5)

    # 3. Display sponsor image
    photo = cv2.cvtColor(cv2.imread("racingwait.png"),cv2.COLOR_BGR2RGB)
    frame = ImageTk.PhotoImage(image=Image.fromarray(photo))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 second
    time.sleep(2.5)
    # 5. Display out/notout image
    if decision == 'red':
        decisionImg = "racingredwin.png"
    else:
        decisionImg = "racingorangewin.png"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 4. Wait for 3 second
    time.sleep(3)
    frame = cv2.cvtColor(cv2.imread("racingdecision.png"), cv2.COLOR_BGR2RGB)
    frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    


stream = cv2.VideoCapture("cutclip.mp4")
def play(speed):
    print(f"You clicked on play. Speed is {speed}")

    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = ImageTk.PhotoImage(image = Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

  
    


def out():
    thread = threading.Thread(target=pending, args=("red",))
    thread.daemon = 1
    thread.start()
    print("Red player win")

def notout():
    thread = threading.Thread(target=pending, args=("orange",))
    thread.daemon = 1
    thread.start()
    print("Orange palyer win")



SET_WIDTH=650
SET_HEIGHT=368
window=tkinter.Tk()
cv_img = cv2.cvtColor(cv2.imread("racingdecision.png"), cv2.COLOR_BGR2RGB)
window.title("Racing DR System ")
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo=ImageTk.PhotoImage(image=Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0,anchor=tkinter.NW,image=photo)
canvas.pack()

# Buttons to control playback
btn1 = tkinter.Button(window, text="<< Previous (fast)", width=50,command=partial(play,-25))
btn1.pack()

btn2 = tkinter.Button(window, text="<< Previous (slow)", width=50,command=partial(play,-2))
btn2.pack()

btn3 = tkinter.Button(window, text="Next (slow) >>", width=50,command=partial(play,2))
btn3.pack()

btn4 = tkinter.Button(window, text="Next (fast) >>", width=50,command=partial(play,25))
btn4.pack()

btn5 = tkinter.Button(window, text="Red palyer win", width=50,command=out)
btn5.pack()

btn6 = tkinter.Button(window, text="Orange playr win", width=50,command=notout)
btn6.pack()
window.mainloop()