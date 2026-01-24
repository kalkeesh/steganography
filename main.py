from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from stegano import exifHeader as stg
import tkinter.font as font
from PIL import Image, ImageTk
import requests
from io import BytesIO
from datetime import datetime
import uuid


# ---------------- IMAGE LOADER ---------------- #
def load_image_from_url(url, width=600, height=400):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    pil_image = Image.open(BytesIO(response.content))
    pil_image = pil_image.resize((width, height))
    return ImageTk.PhotoImage(pil_image)


# ---------------- DECODE SCREEN ---------------- #
def Decode():
    Screen.destroy()
    DecScreen = Tk()
    DecScreen.title("Decode - Secret Message")
    DecScreen.geometry("600x600")

    bg_img = load_image_from_url(
        "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600"
    )
    bg_label = Label(DecScreen, image=bg_img)
    bg_label.image = bg_img
    bg_label.place(x=0, y=0)

    file_path = StringVar()

    def OpenFile():
        file_path.set(
            askopenfilename(
                title="Select Encoded Image",
                filetypes=(("JPEG files", "*.jpg"),)
            )
        )

    def Decoder():
        if not file_path.get():
            messagebox.showerror("Error", "Please select an image")
            return

        try:
            message = stg.reveal(file_path.get())
            Label(
                DecScreen,
                text=f"{message}",
                font=("Arial", 14),
                bg="white",
                wraplength=400
            ).place(relx=0.1, rely=0.4)
        except Exception:
            messagebox.showerror("Error", "No hidden message found")

    Button(
        DecScreen, text="Select Image", bg="red", fg="white",
        command=OpenFile, font=("Arial", 14)
    ).place(relx=0.1, rely=0.3)

    Button(
        DecScreen, text="Decode", bg="yellow", fg="black",
        command=Decoder, font=("Arial", 18)
    ).place(relx=0.4, rely=0.5)


# ---------------- ENCODE SCREEN ---------------- #
def Encode():
    Screen.destroy()
    EncScreen = Tk()
    EncScreen.title("Encode - Hide Your Secret")
    EncScreen.geometry("600x600")

    bg_img = load_image_from_url(
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=600"
    )
    bg_label = Label(EncScreen, image=bg_img)
    bg_label.image = bg_img
    bg_label.place(x=0, y=0)

    Label(EncScreen, text="Secret Message", font=("Arial", 14)).place(relx=0.1, rely=0.2)
    message_entry = Entry(EncScreen, width=30, font=("Arial", 14))
    message_entry.place(relx=0.4, rely=0.2)

    file_path = StringVar()

    def OpenFile():
        file_path.set(
            askopenfilename(
                title="Select Image",
                filetypes=(("JPEG files", "*.jpg"),)
            )
        )

    def Encoder():
        if not file_path.get() or not message_entry.get():
            messagebox.showerror("Error", "Missing image or message")
            return

        unique_name = f"encoded_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}.jpg"

        try:
            stg.hide(file_path.get(), unique_name, message_entry.get())
            messagebox.showinfo("Success", f"Image saved as:\n{unique_name}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    Button(
        EncScreen, text="Select Image", bg="red", fg="white",
        command=OpenFile, font=("Arial", 14)
    ).place(relx=0.1, rely=0.4)

    Button(
        EncScreen, text="Encode", bg="black", fg="white",
        command=Encoder, font=("Arial", 18)
    ).place(relx=0.4, rely=0.5)


# ---------------- MAIN SCREEN ---------------- #
Screen = Tk()
Screen.title("Image Steganography - KSK")
Screen.geometry("600x600")

bg_img = load_image_from_url(
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=600"
)
bg_label = Label(Screen, image=bg_img)
bg_label.image = bg_img
bg_label.place(x=0, y=0)

Button(
    Screen, text="Encode", bg="red", fg="white",
    command=Encode, font=("Arial", 22)
).pack(side=LEFT, padx=30, pady=20)

Button(
    Screen, text="Decode", bg="yellow", fg="black",
    command=Decode, font=("Arial", 22)
).pack(side=RIGHT, padx=30, pady=20)

mainloop()
