import tkinter as tk
from tkinter import filedialog
import pygame

from config import AppConfig
from updater_service import UpdaterService

app_config = AppConfig()
updater_service = UpdaterService()


def play_background_music():
    pygame.mixer.music.load("sounds/mandragora.mp3")
    pygame.mixer.music.play(-1)  # -1 plays the music in a loop
    pygame.mixer.music.set_volume(1)


def browse_folder(ev: tk.StringVar):
    folder_path = filedialog.askdirectory()
    ev.set(folder_path)
    app_config.set_setting("WOW_ADDONS_FOLDER", folder_path)


def process_folder(ev: tk.StringVar):
    folder_path = ev.get()
    # Add your code to process the folder_path as needed
    print("Processing folder:", folder_path)
    updater_service.update_elvui(folder_path)


def program():
    if not app_config.load_configuration():
        raise "Config file could not be loaded"
    wow_addons_folder = app_config.get_setting("WOW_ADDONS_FOLDER")

    if not wow_addons_folder:
        print("Please save a folder for wow addons")

    # pygame.mixer.init()
    root = tk.Tk()
    root.title("Elvui updater")
    root.geometry("300x250")

    # root.iconbitmap("icon.ico")
    # play_background_music()
    # background_image = tk.PhotoImage(
    #     file="images/background.png")  # Replace "your_image.png" with the path to your image
    # background_label = tk.Label(root, image=background_image)
    # background_label.place(relwidth=1, relheight=1)

    # Add a frame for padding to the left
    padding_frame = tk.Frame(root, width=20)
    padding_frame.grid(row=0, column=0, rowspan=2, sticky="w")

    # Create and place a label
    label = tk.Label(root, text="Enter your wow addon folder path:", anchor="w")
    label.grid(row=0, column=0, pady=10, sticky="w")
    # Create and place an entry widget with left alignment and set it to disabled
    entry_var = tk.StringVar(value=wow_addons_folder)
    entry = tk.Entry(root, textvariable=entry_var, width=40, state="disabled")
    entry.grid(row=0, column=1, pady=10, sticky="w")

    # Create and place a button to browse for the folder with left alignment
    browse_button = tk.Button(root, text="...", command=lambda: browse_folder(entry_var))
    browse_button.grid(row=0, column=2, pady=10, padx=(0, 10), sticky="w")

    # Create and place a button to perform an action with the entered folder directory with left alignment
    process_button = tk.Button(root, text="Process Folder", command=lambda: process_folder(entry_var))
    process_button.grid(row=1, column=2, pady=10, sticky="w")

    root.mainloop()


if __name__ == "__main__":
    program()
