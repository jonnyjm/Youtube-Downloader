import tkinter
import customtkinter
from urllib.request import urlopen
import yt_dlp
from PIL import Image, ImageTk

search_complete = False

def search():
    global search_complete
    ydl = yt_dlp.YoutubeDL()
    try:
        global frame
        yt_vid = ydl.extract_info(link.get(), download=False) # extracts info from URL

        if search_complete:
            frame.destroy()

        test.configure(text=yt_vid.get('title'))
        img = Image.open(urlopen(yt_vid.get("thumbnail")))
        thumbnail_img = ImageTk.PhotoImage(img.resize((300, int(img.height * (300/img.width))), Image.Resampling.LANCZOS))
        frame = customtkinter.CTkFrame(root,width=800, height=600, border_width=1, border_color="white")
        frame.pack(pady=10, padx=10)
        customtkinter.CTkLabel(frame, image=thumbnail_img, text="").place(relx=0.3, rely=0.05)
        search_complete = True

    except yt_dlp.DownloadError: # throws error if URL is not found or is invalid
        test.configure(text="Invalid URL...")
        if (search_complete):
            frame.destroy()
            search_complete = False
        
root = customtkinter.CTk()
root.geometry("1080x720")
root.minsize(1080,720)
root.title("Youtube Downloader")
root.iconphoto(False,ImageTk.PhotoImage(Image.open("Images/youtube_icon.ico")))

yt_logo = ImageTk.PhotoImage(Image.open("Images/youtube_icon.ico").resize((100,100), Image.Resampling.LANCZOS))
customtkinter.CTkLabel(root, image= yt_logo, text='  Youtube Video Downloader', compound="left",font=("Futura", 20, "bold")).pack(pady=5)

link = customtkinter.CTkEntry(root, placeholder_text="Enter Youtube Video URL",width= 400, height=30, justify="center")
link.pack(pady=5) 
search_btn = customtkinter.CTkButton(root, text="Search", command=search, fg_color="red", text_color="white", hover_color="black", font=("Futura",15))
search_btn.pack(pady=10)

test = customtkinter.CTkLabel(root, text="", font=("Futura",15, 'bold'))
test.pack()

# Keeps window open
root.mainloop()

