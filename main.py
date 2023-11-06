import tkinter
from tkinter import *
import random

# Window
window = Tk()
window.geometry('650x500')
window.title('Typing Speed Checker')
window.config(bg="#F3FDE8")
left_frame = Frame(window, width=650, height=300, bg="#FFE5E5")
left_frame.place(relx=0.5, rely=0.75, anchor=CENTER)
window.resizable(False,False)

characters = 0
passedSeconds = 0
first_key_press = True
ended = False
high_score_no = 0
wpm = 0
def keyPress(event=None):
    global first_key_press
    try:
        if first_key_press:
            addSecond()
            first_key_press = False
        if event.char.lower() == labelRight.cget('text')[0].lower():
            global characters
            characters += 1

            # Deleting one from the right side.
            labelRight.configure(text=labelRight.cget('text')[1:])
            # Deleting one from the right side.
            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
            #set the next Letter Lavbel
            currentLetterLabel.configure(text=labelRight.cget('text')[0])
            if len(labelLeft.cget('text')) > 4:
                labelLeft.configure(text=labelLeft.cget('text')[1:])

    except IndexError:
        global ended, high_score
        ended = True
        wpm = round((characters / 5)/(passedSeconds/60))
        high_score.configure(text= wpm)

# HighScore
highscore = Label(text='Your Best HighScore: ', bg= '#F3FDE8', fg='#102C57').place(relx=0.5, rely=0.2, anchor=CENTER)

#Display Random Text
def DisplayText():
    # Text List
    random_sentence_list = [
        "The quick brown fox jumps over the lazy dog.",
        "A rainbow appeared in the sky after the rainstorm.",
        "She played the piano beautifully at the concert.",
        "The adventurous explorer trekked through the dense jungle.",
        "I enjoy reading books by the cozy fireplace."
    ]

    # Chosing one of the texts randomly with the choice function
    text = random.choice(random_sentence_list).lower()

    splitPoint = 0

    global labelLeft
    labelLeft = Label(window, text=text[0:splitPoint],bg="#FFE5E5" , fg='grey', font=("Impact", 25))
    labelLeft.place(relx=0.37, rely=0.5, anchor=E)

    # Here is the text which will be written
    global labelRight
    labelRight = Label(window, text=text[splitPoint:],bg="#FFE5E5" ,font=("Impact", 25))
    labelRight.place(relx=0.37, rely=0.5, anchor=W)

    # This label shows the user which letter he now has to press
    global currentLetterLabel
    currentLetterLabel = Label(window, text=text[splitPoint],bg="#FFE5E5" ,fg='grey',font=('Impact', 17))
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

    global high_score
    high_score = Label(window, text=wpm,bg="#F3FDE8", fg='black', font=('Impact', 20))
    high_score.place(relx=0.5, rely=0.26, anchor=N)

    global writeAble
    writeAble = True
    window.bind('<Key>', keyPress)

def addSecond():
    # Add a second to the counter.
    global passedSeconds
    passedSeconds += 1
    # call this function again after one second if the time is not over.
    if ended == False:
        window.after(1000, addSecond)

DisplayText()

window.mainloop()