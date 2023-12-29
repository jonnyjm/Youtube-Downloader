from tkinter import filedialog
import customtkinter
from urllib.request import urlopen
import yt_dlp
from PIL import Image, ImageTk

search_complete = False
frame = None
def search():
    global search_complete
    
    ydl = yt_dlp.YoutubeDL()
    try:
        global frame
        yt_vid = ydl.extract_info(link.get(), download=False) # extracts info from URL

        if search_complete:
            frame.destroy()

        search_complete = True
        status.configure(text=" " + yt_vid.get('title'))
        img = Image.open(urlopen(yt_vid.get("thumbnail")))
        thumbnail_img = ImageTk.PhotoImage(img.resize((300, 200), Image.Resampling.LANCZOS))
        frame = customtkinter.CTkFrame(root,width=800, height=600, border_width=1, border_color="white")
        frame.pack(pady=10, padx=10)
        
        customtkinter.CTkLabel(frame, image=thumbnail_img, text="").place(relx=0.33, rely=0.05)
        type_box = customtkinter.CTkComboBox(frame, values=["Video Download (mp4)","Audio Downlaod (m4a)"], justify='center', width= 200, height=30, button_color="red", border_color="white", border_width=1, corner_radius=2, font=("Futura",13), text_color="white", button_hover_color="black")
        type_box.place(relx=0.4, rely=0.5)

        quality_box = customtkinter.CTkComboBox(frame, values=["High Quality","Low Quality"], justify='center', width= 200, height=30, button_color="red", border_color="white", border_width=1, corner_radius=2, font=("Futura",13), text_color="white", button_hover_color="black")
        quality_box.place(relx=0.4, rely=0.58)

        download_btn = customtkinter.CTkButton(frame, text="Download", command= lambda: downloadVid(type_box.get(), quality_box.get()),fg_color="red", text_color="white", hover_color="black", font=("Futura",15))
        download_btn.place(relx=0.435, rely=0.7)

    except yt_dlp.DownloadError: # throws error if URL is not found or is invalid
        status.configure(text="Invalid URL...")
        if (search_complete):
            frame.destroy()
            search_complete = False
        return None

    search_complete = True



def downloadVid(download_type, download_quality):

    download_loc = filedialog.askdirectory()

    if (download_type[0] == "V"):  # video download
        if (download_quality[0] == "H"): # high quality
            ydl_opts = {
                'format': 'best',  
                'outtmpl': f'{download_loc}/%(title)s.%(ext)s',
            }
        else:
            ydl_opts = {
                'format': '18',  
                'outtmpl': f'{download_loc}/%(title)s.%(ext)s',
            }
    else:
        if (download_quality[0] == "H"):
            ydl_opts = {
                'format': '140' ,  
                'outtmpl': f'{download_loc}/%(title)s.%(ext)s',
            }
        else:
            ydl_opts = {
                'format': '139',  
                'outtmpl': f'{download_loc}/%(title)s.%(ext)s',
            }
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    ydl.download([link.get()])

        
 
        
root = customtkinter.CTk()
root.geometry("1080x720")
root.minsize(1080,720)
root.title("Youtube Downloader")
root.iconphoto(False,ImageTk.PhotoImage(Image.open("Images/youtube_icon.ico")))

yt_logo = ImageTk.PhotoImage(Image.open("Images/youtube_icon.ico").resize((100,100), Image.Resampling.LANCZOS))
customtkinter.CTkLabel(root, image= yt_logo, text='  Youtube Video Downloader', compound="left",font=("Futura", 20, "bold"),text_color="white").pack(pady=5)

link = customtkinter.CTkEntry(root, placeholder_text="Enter Youtube Video URL",width= 400, height=30, justify="center")
link.pack(pady=5) 
search_btn = customtkinter.CTkButton(root, text="Search", command=search, fg_color="red", text_color="white", hover_color="black", font=("Futura",15))
search_btn.pack(pady=10)

status = customtkinter.CTkLabel(root, text="", font=("Futura",15, 'bold'),text_color="white")
status.pack()

# Keeps window open
root.mainloop()

