from tkinter import *

# Window
window = Tk()
window.geometry('800x500')
window.title('Typing Speed Checker')
window.config(bg="#F3FDE8")
left_frame = Frame(window, width=880, height=300, bg="#FFE5E5")
left_frame.place(relx=0.5, rely=0.75, anchor=CENTER)
window.resizable(False,False)
eg = 'Hello'
def validate():
    global eg
    input_txt = None

# HighScore
highscore = Label(text='Your Best HighScore: ', bg= '#F3FDE8', fg='#102C57').place(relx=0.5, rely=0.2, anchor=CENTER)

# Text to be Typed
text = StringVar(value=eg)

user_text = StringVar()
user_text.trace('w', validate)

my_text = Entry(textvariable=user_text, show=' ')
my_text.place(relx=0.5, rely=0.7, anchor=CENTER)
my_text.focus_force()

print(user_text)

window.mainloop()