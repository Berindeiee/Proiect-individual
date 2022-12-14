import os
from PIL import ImageTk,Image
from tkinter import Tk, Frame, Canvas
from tkinter import *
from tkinter import font
from tkinter import messagebox

import customtkinter


def get_culoare():
    if customtkinter.get_appearance_mode() == "Light":
        return 'gray92'
    else:
        return 'gray14'


def bttn1(fereastra, text, bcolor, cmd):
    fcolor = get_culoare()

    def on_enter(e):
        mybutton.configure(fg_color=bcolor)
        mybutton.configure(text_color=get_culoare())
        mybutton.configure(bg_color=get_culoare())

    def on_leave(e):
        mybutton.configure(fg_color=get_culoare())
        mybutton.configure(text_color=bcolor)
        mybutton.configure(bg_color=get_culoare())

    mybutton = customtkinter.CTkButton(fereastra, text=text,
                                       text_color=bcolor,
                                       # hover_color=bcolor,
                                       fg_color=fcolor,
                                       command=cmd,
                                       corner_radius=8,
                                       )
    mybutton.bind("<Enter>", on_enter)
    mybutton.bind("<Leave>", on_leave)
    mybutton.pack(pady=1, padx=1)
    return mybutton


# Implementing event on register button

def logg(fereastra):
    width = 900
    height = 600

    def login_event():
        print("Login pressed - username:", username_entry.get(), "password:", password_entry.get())

        fereastra.login_frame.grid_forget()  # remove login frame
        fereastra.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame

    def back_event():
        main_frame.grid_forget()  # remove main frame
        login_frame.grid(row=0, column=0, sticky="ns")  # show login frame

    login = customtkinter.CTkToplevel(fereastra)
    login.title("CustomTkinter example_background_image.py")
    login.geometry(f"{900}x{600}")
    login.resizable(False, False)
    light_image = Image.open("GPU.png")
    # load and create background image
    # current_path = os.path.dirname(os.path.realpath(__file__))
    bg_image = customtkinter.CTkImage(light_image=Image.open("bg_gradient.jpg"),
                                      dark_image=Image.open("bg_gradient.jpg"),
                                      size=(width, height))
    bg_image_label = customtkinter.CTkLabel(login, image=bg_image)
    bg_image_label.grid(row=0, column=0)

    # create login frame
    login_frame = customtkinter.CTkFrame(login, corner_radius=0)
    login_frame.grid(row=0, column=0, sticky="ns")
    login_label = customtkinter.CTkLabel(login_frame, text="CustomTkinter\nLogin Page",
                                         font=customtkinter.CTkFont(size=20, weight="bold"))
    login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
    username_entry = customtkinter.CTkEntry(login_frame, width=200, placeholder_text="username")
    username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
    password_entry = customtkinter.CTkEntry(login_frame, width=200, show="*", placeholder_text="password")
    password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
    login_button = customtkinter.CTkButton(login_frame, text="Login", command=login_event, width=200)
    login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

    # create main frame
    main_frame = customtkinter.CTkFrame(login, corner_radius=0)
    main_frame.grid_columnconfigure(0, weight=1)
    main_label = customtkinter.CTkLabel(main_frame, text="CustomTkinter\nMain Page",
                                        font=customtkinter.CTkFont(size=20, weight="bold"))
    main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
    back_button = customtkinter.CTkButton(main_frame, text="Back", command=back_event, width=200)
    back_button.grid(row=1, column=0, padx=30, pady=(15, 15))
