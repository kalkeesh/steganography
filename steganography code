from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from stegano import exifHeader as stg
import tkinter.font as font
# decoding the file
def Decode():
    Screen.destroy()
    DecScreen = Tk()
    DecScreen.title("Decode- SECRET")
    DecScreen.geometry("600x600+600+600")
    DecScreen.config = PhotoImage(file="C:\\Users\\srini\\Downloads\\cyber-products-tech-fp1170x650.png")
    label = Label(DecScreen, image= DecScreen.config)
    label.place(x=0, y=0)


    def OpenFile():
        global FileOpen
        FileOpen = StringVar()
        FileOpen = askopenfilename(initialdir="/Desktop", title="Select the File",
                                   filetypes=(("only jpeg files", "*jpg"), ("all type of files", "*.*")))

    def Decoder():
        myFont = font.Font(size=15)
        Message = stg.reveal(FileOpen)
        label3 = Label(text=Message)
        label3['font'] = myFont
        label3.place(relx=0.2, rely=0.3)

    myFont = font.Font(size=15)
    SelectButton = Button(text="Select the file", command=OpenFile,fg='black', bg='red')
    SelectButton['font'] = myFont
    SelectButton.place(relx=0.1, rely=0.4)
    myFont = font.Font(size=25)
    DecodeButton = Button(text="Decode", command=Decoder,fg='black', bg='yellow')
    DecodeButton['font'] = myFont
    DecodeButton.place(relx=0.4, rely=0.5)
# encoding the file
def Encode():
    Screen.destroy()
    EncScreen = Tk()
    EncScreen.title("Encode- YOUR SECRET MESSAGE")
    EncScreen.geometry("600x600+600+600")
    EncScreen.config = PhotoImage(file="C:\\Users\\srini\\Downloads\\960x0.png")
    label = Label(EncScreen, image=EncScreen.config)
    label.place(x=0, y=0)
    myFont = font.Font(size=15)
    label = Label(text="Confidential Message")
    label['font'] = myFont
    label.place(relx=0.1, rely=0.2)
    myFont = font.Font(size=15)
    entry = Entry()
    entry['font'] = myFont
    entry.place(relx=0.5, rely=0.2)
    myFont = font.Font(size=15)
    label1 = Label(text="Name of the File")
    label1['font'] = myFont
    label1.place(relx=0.1, rely=0.3)
    SaveEntry = Entry()
    SaveEntry.place(relx=0.5, rely=0.3)

    def OpenFile():
        global FileOpen
        FileOpen = StringVar()
        FileOpen = askopenfilename(initialdir="/Desktop", title="SelectFile",
                                   filetypes=(("only jpeg files", "*jpg"), ("all type of files", "*.*")))

        myFont = font.Font(size=15)
        label2 = Label(text=FileOpen)
        label2['font'] = myFont
        label2.place(relx=0.5, rely=0.3)

    def Encoder():
        Response = messagebox.askyesno("PopUp", "Do you want to encode the image?")
        if Response == 1:
            stg.hide(FileOpen, SaveEntry.get() + ".jpg", entry.get())
            messagebox.showinfo("Pop Up", "Successfully Encoded")
        else:
            messagebox.showwarning("Pop Up", "Unsuccessful, please try again")

    myFont = font.Font(size=15)
    SelectButton = Button(text="Select the file", command=OpenFile,fg='black', bg='red')
    SelectButton['font'] = myFont
    SelectButton.place(relx=0.1, rely=0.4)
    myFont = font.Font(size=20)
    EncodeButton = Button(text="Encode", command=Encoder,fg='white', bg='black')
    EncodeButton['font'] = myFont
    EncodeButton.place(relx=0.4, rely=0.5)
# Initializing the screen
Screen = Tk()
Screen.title("Image Steganography by - KSK  ")
Screen.geometry("600x600+600+600")
bg_image = PhotoImage(file="C:\\Users\\srini\\Downloads\\post-image_file-Recent-Security-Technologies-for-IoT-Industry.png")
label = Label( Screen, image = bg_image)
label.place(x = 0, y = 0)
# creating buttons
myFont = font.Font(size=25)
EncodeButton = Button(Screen,text="Encode", command=Encode,fg='black', bg='red')
EncodeButton['font'] = myFont
EncodeButton.pack(side=LEFT, padx=25, pady=20)
DecodeButton = Button(Screen,text="Decode", command=Decode,fg='red', bg='yellow')
DecodeButton.pack(side=RIGHT, padx=15, pady=20)
DecodeButton['font'] = myFont


mainloop()
