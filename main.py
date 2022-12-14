import os
import random
from Functii import *
from PIL import ImageTk, Image
import customtkinter
import smtplib
from email.message import EmailMessage
import ssl
from email.mime.text import MIMEText
from string import Template
from CPU import *
import string

a = CPU("Intel Core i7 5470H", "Intel", "2000", "120", "C1", "1145", "2016", "DA", "4.2GHz")
print(a)
ok = 1
score = 60
limit = 0
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
#customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

def log(fereastra):
    width = 900
    height = 600
    def login_event():
        print("Login pressed - username:", username_entry.get(), "password:", password_entry.get())

        login_frame.grid_forget()  # remove login frame
        main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame

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
def trimite_email(catre, numar):
    email_sender = "build.pc.318@gmail.com"
    email_password = 'atydpcqtkqwtnjat'
    email_receiver = catre

    subiect = "Mesaj de verificare email"
    htm = """\
    <div>
  <div><!-- [if mso]>
    <noscript>
        <xml>
            <o:OfficeDocumentSettings>
                <o:AllowPNG/>
                <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
        </xml>
    </noscript>
    <![endif]--> <!-- [if lte mso 11]>
    <style type="text/css">
        .mj-outlook-group-fix { width:100% !important; }
    </style>
    <![endif]--></div>
</div>
<style>@media screen and (max-width: 359px) {
  body {
    margin: 10px !important;
  }
  #logo-line {
    width: 300px !important;
    height: 5px !important;
  }
  #logo-and-promo-text td {
    display: block !important;
    padding: 0 0 8px 0 !important;
  }
}
@media screen and (min-width: 360px) and (max-width: 374px) {
  body {
    margin: 10px !important;
  }
  #logo-line {
    width: 340px !important;
    height: 5px !important;
  }
  #logo-and-promo-text td {
    display: block !important;
    padding: 0 0 8px 0 !important;
  }
}
@media only screen and (min-width: 375px) and (max-width: 413px) {
  body {
    margin: 10px !important;
  }
  #logo-line {
    width: 355px !important;
    height: 5px !important;
  }
  #logo-and-promo-text td {
    display: block !important;
    padding: 0 0 8px 0 !important;
  }
}
@media only screen and (min-width: 414px) and (max-width: 479px) {
  body {
    margin: 10px !important;
  }
  #logo-line {
    width: 394px !important;
    height: 5px !important;
  }
  #logo-and-promo-text td {
    display: block !important;
    padding: 0 0 8px 0 !important;
  }
}
@media only screen and (min-width: 480px) and (max-width: 567px) {
  #logo-line {
    width: 440px !important;
    height: 5px !important;
  }
}
@media only screen and (min-width: 568px) and (max-width: 639px) {
  #logo-line {
    width: 528px !important;
    height: 5px !important;
  }
}
.button:hover {
  background-color: #2f82fb !important;
  color: #ffffff !important;
}
.button:active {
  background-color: #2872e0 !important;
  color: #ffffff !important;
}
.button.main:hover {
  background-color: #3c8cfc !important;
}
.button.main:active {
  background-color: #2872e0 !important;
}</style>
<div>
  <table style="border-spacing: 0px; margin: 0px; border-collapse: separate; border: 0px; max-width: 600px; font-family: Arial, Helvetica, 'sans-serif'; height: 334px;" border="0" cellspacing="0" cellpadding="0" align="left" bgcolor="#ffffff">
    <tbody>
      <tr style="height: 43px;">
        <td style="border-collapse: separate; margin: 0px; padding: 0px; font-family: Arial, Helvetica, 'sans-serif'; height: 43px; width: 600px;" align="left">
          <table id="logo-and-promo-text" style="border-spacing: 0px; border: 0px none; border-collapse: separate; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 501px; height: 104px;" border="0" cellspacing="0" cellpadding="0" align="left">
            <tbody>
              <tr>
                <td style="border-collapse: separate; padding: 0px 20px 0px 0px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 306px;">
                  <img style="height: 83px; display: inline-block; vertical-align: middle; padding: 0px;" src="https://share1.cloudhq-mkt3.net/a5d1450971468e.png" alt="Desktop" width="306" height="43" border="0">
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 16px; margin: 0px; font-size: 12px; line-height: 14px; color: #212121; font-weight: bold; vertical-align: middle; font-family: Arial, Helvetica, 'sans-serif'; width: 159px;" valign="middle">The way you can build your pc 
                  <img src="https://cdn.tiny.cloud/1/744os35bk6lfhnyx14onzpqa8er3gs4s21opocmie2wxar65/tinymce/4.9.11-104/plugins/emoticons/img/smiley-cool.gif" alt="cool">
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
      <tr style="height: 10px;">
        <td style="border-collapse: separate; padding: 0px; margin: 0px; line-height: 5px; font-family: Arial, Helvetica, 'sans-serif'; height: 10px; width: 600px;">
          <img id="logo-line" style="width: 600px; height: 5px; padding: 0px;" src="https://static.g2a.com/_/mail/g2a-line.png" width="600" height="5" border="0">
        </td>
      </tr>
      <tr style="height: 172px;">
        <td id="template-content" style="border-collapse: separate; padding: 30px 0px 0px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; height: 172px; width: 600px;" align="left" valign="top">
          <h1 style="font-size: 20px; color: #000000; padding: 0; margin: 0 0 10px; font-weight: bold; line-height: 30px;">Email verification</h1>
          <div class="body-1" style="color: #000000; font-size: 16px; line-height: 24px; font-weight: normal; margin-bottom: 30px;">Email verification code is: $numar</div>
          <div class="body-1" style="color: #000000; font-size: 16px; line-height: 24px; font-weight: normal; margin-bottom: 30px;">Best wishes, 
            <br>Build.pc318
          </div>
        </td>
      </tr>
      <tr style="height: 40px;">
        <td style="border-collapse: separate; margin: 0px; font-size: 14px; height: 40px; vertical-align: middle; border-top: 1px solid #e0e0e0; padding: 10px 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 600px;" align="left" valign="middle" height="40">This email has been generated automatically. 
          <br>
          <strong>Please do not reply to it.</strong>
        </td>
      </tr>
      <tr style="height: 27px;">
        <td style="border-collapse: separate; margin: 0px; border-top: 1px solid #e0e0e0; padding: 16px 0px; font-family: Arial, Helvetica, 'sans-serif'; height: 27px; width: 600px;" align="left">
          <table style="border-spacing: 0px; border: 0px none; border-collapse: separate; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 438px; height: 35px;" border="0" cellspacing="0" cellpadding="0" align="left">
            <tbody>
              <tr style="height: 72px;">
                <td style="border-collapse: separate; padding: 0px; margin: 0px; font-size: 12px; line-height: 24px; color: #888888; font-family: Arial, Helvetica, 'sans-serif'; width: 42.3854px; height: 72px;">Find us on:</td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 46.6042px; height: 72px;">
                  <a href="https://github.com/Berindeiee/Proiect-individual">
                    <img src="https://share1.cloudhq-mkt3.net/2fd99bd42c6346.png" alt="" width="46" height="46">
                  </a> 
                  <br>
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 46.6042px; height: 72px;">
                  <br>
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 46.6042px; height: 72px;">
                  <br>
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 46.6042px; height: 72px;">
                  <br>
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 46.6042px; height: 72px;">
                  <br>
                </td>
                <td style="border-collapse: separate; padding: 0px 0px 0px 20px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; width: 42.5938px; height: 72px;">&nbsp;</td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
      <tr style="height: 16px;">
        <td style="border-collapse: separate; padding: 0px 0px 16px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; height: 16px; width: 600px;" align="left">&nbsp;</td>
      </tr>
      <tr style="height: 10px;">
        <td style="border-collapse: separate; padding: 0px 0px 16px; margin: 0px; border-bottom: 1px solid #e0e0e0; font-family: Arial, Helvetica, 'sans-serif'; height: 10px; width: 600px;" align="left">&nbsp;</td>
      </tr>
      <tr style="height: 16px;">
        <td style="border-collapse: separate; padding: 15px 0px 0px; margin: 0px; font-family: Arial, Helvetica, 'sans-serif'; height: 16px; width: 600px;" align="left">&nbsp;</td>
      </tr>
    </tbody>
  </table>
  <img src="https://ea.pstmrk.it/open/v3_bItdwZZHrGrP7pe-SzHJ2_aBDsAhpRrbjrnfudf2Ksz8-uVLih00eg7Iqlsc5_waqkJwsN4inacdLtPn-qYiuT8QXnn14oLzvr25iQrpeNyJP92Ovw2V9pldJvUx5TpJLCqV1w9xHk9cE_PXmTlbrzC15Xa6h1F-Qof5tKMc5khLPFkDS3YsxmHoAZM_9eyDkcZ-F94gtp5XeFFIHDyYzYMHMIpfSjQ7mLaRcRsQCCkPkrW4eN7PWIzYHC0bY_GqyEfKaL7oCqeKhfNvCFoQtfWDgi7-SQdOrkZv63cn-8Nsvx4Rn3_q1ujdK3mgB2dA1IEiphGk8W39Mf9YoKYisNxQiEqQp1BqHglHpJ1lSZz_P4KIH-z4c0M9QEjenS1ESi6jVv21FR81pRpSDmA22A" alt="" width="1" height="1" border="0">
</div>
    """
    html = Template(htm).safe_substitute(numar=numar)
    body = MIMEText(html, 'html')
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subiect
    em.set_content(body)
    context = ssl.create_default_context()
    em.attach(html)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        try:
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        except:
            exceptie = Toplevel(registration_screen)
            exceptie.title("Failed")
            exceptie.resizable(False, False)
            exceptie.geometry("300x150")
            customtkinter.CTkLabel(exceptie, text="Sending faild" + "\n" + " the email does not work",
                                   text_color="red").pack(padx=10, pady=10)
            customtkinter.CTkButton(exceptie, text="OK", command=exceptie.destroy).pack(padx=1, pady=1)

# Designing window for registration
def register():
    global registration_screen
    registration_screen = customtkinter.CTkToplevel(main_screen)
    registration_screen.geometry(f"{400}x{800}")
    registration_screen.title("Registration")
    global username
    global password
    global email
    global password_r

    global username_entry
    global password_entry
    global password_r_entry
    global email_entry
    global cod
    global cod_introdus_entry
    global trimis
    global inregistrare

    username = StringVar()
    password = StringVar()
    password_r = StringVar()
    email = StringVar()

    customtkinter.CTkLabel(registration_screen, text="Please enter informations", font=("Roboto", 20),
                           # text_color="black",
                           fg_color=("#B8A11D"),
                           corner_radius=8
                           ).pack(pady=5, padx=10)
    customtkinter.CTkLabel(registration_screen, text="Username*", font=("Roboto", 15),
                           # text_color="black"
                           ).pack(pady=1, padx=10)

    username_entry = customtkinter.CTkEntry(registration_screen, placeholder_text="numele de utilizator",
                                            textvariable=username)
    username_entry.pack(pady=1, padx=10)

    customtkinter.CTkLabel(registration_screen, text="Email*", font=("Roboto", 15),
                           # text_color="black"
                           ).pack(pady=1, padx=10)
    email_entry = customtkinter.CTkEntry(registration_screen, placeholder_text="emailul dumneavoastra",
                                         textvariable=email)
    email_entry.pack(pady=1, padx=10)

    customtkinter.CTkLabel(registration_screen, text="Password*", font=("Roboto", 15),
                           # text_color="black"
                           ).pack(pady=1, padx=10)
    password_entry = customtkinter.CTkEntry(registration_screen, placeholder_text="parola", show="😄",
                                            textvariable=password)
    password_entry.pack(pady=1, padx=10)

    customtkinter.CTkLabel(registration_screen, text="Re-enter Password*", font=("Roboto", 15),
                           # text_color="black"
                           ).pack(pady=1, padx=10)
    password_r_entry = customtkinter.CTkEntry(registration_screen, placeholder_text="reintroduceti parola", show="😄",
                                              textvariable=password_r)
    password_r_entry.pack(pady=1, padx=10)

    email_image = customtkinter.CTkImage(light_image=Image.open("email_l.png"),
                                         dark_image=Image.open("email_d.png"),
                                         size=(30, 30))
    global cod

    trimis = customtkinter.CTkButton(registration_screen, image=email_image, text="Send verfication email",
                                     corner_radius=8,
                                     # text_color="black",
                                     compound="right",
                                     command=lambda: timer(registration_screen)
                                     )
    trimis.pack(padx=5, pady=20)

    inregistrare = customtkinter.CTkButton(registration_screen, image=email_image, text="Sign up",
                                           corner_radius=8,
                                           # text_color="black",
                                           compound="right",
                                           command=register_user,
                                           state="disabled"
                                           )
    inregistrare.pack(pady=1, padx=10)


def timer(fer):
    global cod
    cod = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    if email.get():
        inregistrare.configure(state="normal")
        trimis.configure(state="disabled")
        # aici se apeleaza functia pentru a trimitye codul de verificare
        trimite_email(email.get(), cod)

        global ok
        if ok == 1:
            global cod_introdus_entry
            global cod_introdus
            cod_introdus = StringVar()
            cod_label = customtkinter.CTkLabel(fer, text="Code*", font=("Roboto", 15),
                                               #text_color="black"
                                               )
            cod_label.pack(pady=1, padx=10)
            cod_introdus_entry = customtkinter.CTkEntry(fer, placeholder_text="dfs", width=100,
                                                        textvariable=cod_introdus)
            cod_introdus_entry.pack(pady=1, padx=10)

        def update():
            global score
            score = score - 1
            ScoreL.configure(text="You have " + str(score) + " seconds left to enter the code")
            if score > limit:
                # schedule next update 1 second later
                fer.after(1000, update)
            else:
                global ok
                inregistrare.configure(state="disabled")
                ScoreL.destroy()
                cod_introdus_entry.destroy()
                cod_label.destroy()
                ok = 1
                score = 120
                trimis.configure(state="normal")

        if ok == 1:
            ScoreL = customtkinter.CTkLabel(fer, text="You have " + str(score) + " seconds left to enter the code",
                                            #text_color="black"
                                            )
            ScoreL.pack(pady=1, padx=10)
            ok = 0
        fer.after(1000, update)  # start the update 1 second later


# Designing window for login
# def log():

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    heading = customtkinter.CTkLabel(login_screen, text="LOGIN", text_color="black")
    heading.pack(pady=10, padx=1)

    global username_verify
    global password_verify
    global login_button

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    customtkinter.CTkLabel(login_screen, text="Username *", height=1, anchor=NW, font=("Poppins", 14)).pack(pady=1,
                                                                                                            padx=1)
    username_login_entry = customtkinter.CTkEntry(login_screen, textvariable=username_verify)
    username_login_entry.pack(pady=1, padx=1)

    customtkinter.CTkLabel(login_screen, text="Password *", height=1, anchor=NW, font=("Poppins", 14)).pack(pady=1,
                                                                                                            padx=1)
    username_login_entry = customtkinter.CTkEntry(login_screen, textvariable=password_verify)
    username_login_entry.pack(pady=1, padx=1)

    Label(login_screen, text="Password * ").place(x=10, y=95)
    password_login_entry = Entry(login_screen, width=25, justify='left', show='*', font=("", 15), highlightthickness=1
                                 , textvariable=password_verify)
    password_login_entry.place(x=14, y=130)

    login_button = customtkinter.CTkButton(login_screen, text="Login", width=10, height=1, command=login_verify)
    login_button.pack(pady=11, padx=1)


# Implementing event on register button
# def validare_email(email):

def register_user():
    username_info = username.get()
    password_info = password.get()
    password_r_info = password_r.get()
    email_info = email.get()
    cod_introdus_info = cod_introdus.get()
    if os.path.isfile('./' + username_info) == 1:
        exceptie = Toplevel(registration_screen)
        exceptie.title("Failed")
        exceptie.resizable(False, False)

        exceptie.geometry("300x150")
        customtkinter.CTkLabel(exceptie, text="Sign up faild" + "\n" + " username already exist",
                               text_color="red").pack(padx=10, pady=10)
        customtkinter.CTkButton(exceptie, text="OK", command=exceptie.destroy).pack(padx=1, pady=1)
    elif password_info != password_r_info:
        exceptie = Toplevel(registration_screen)
        exceptie.title("Failed")
        exceptie.resizable(False, False)

        exceptie.geometry("300x150")
        customtkinter.CTkLabel(exceptie, text="Registration faild" + "\n" + " password do not match",
                               text_color="red").pack(padx=10, pady=10)
        customtkinter.CTkButton(exceptie, text="OK", command=exceptie.destroy).pack(padx=1, pady=1)
    elif cod != cod_introdus_info:
        exceptie = Toplevel(registration_screen)
        exceptie.title("Failed")
        exceptie.resizable(False, False)

        exceptie.geometry("300x150")
        customtkinter.CTkLabel(exceptie, text="Registration faild" + "\n" + " the code is wrong",
                               text_color="red").pack(padx=10, pady=10)
        customtkinter.CTkButton(exceptie, text="OK", command=exceptie.destroy).pack(padx=1, pady=1)
    elif password_info == password_r_info:  # verificare reintroducere parola
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info + "\n")
        file.write(email_info + "\n")
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)
        password_r_entry.delete(0, END)
        email_entry.delete(0, END)
        exceptie = Toplevel(registration_screen)
        exceptie.title("Sign up succes")
        exceptie.resizable(False, False)
        exceptie.geometry("200x95")
        customtkinter.CTkLabel(exceptie, text="Registration succecs" + "\n" + " now you can sign up",
                               text_color="green").pack(padx=10, pady=10)
        customtkinter.CTkButton(exceptie, text="OK", command=lambda: destroy_registeration(exceptie)).pack(padx=1,
                                                                                                           pady=1)


def destroy_registeration(exceptie):
    exceptie.destroy()
    registration_screen.destroy()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def get_culoare():
    if customtkinter.get_appearance_mode() == "Light":
        return 'gray92'
    else:
        return 'gray14'

def actualizare_culoare(mybutton1, mybutton2):
    fcolor = get_culoare()
    bcolor = '#25dae9'
    mybutton1.configure(fg_color=fcolor)
    mybutton1.configure(text_color=bcolor)
    mybutton1.configure(bg_color=fcolor)
    bcolor = '#ffcc66'
    mybutton2.configure(fg_color=fcolor)
    mybutton2.configure(text_color=bcolor)
    mybutton2.configure(bg_color=fcolor)


def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)
    actualizare_culoare(mybutton1,mybutton2)

def change_set_default_color_theme(new_default_color_theme:str):
    customtkinter.set_default_color_theme(new_default_color_theme)
# Designing Main(first) window


def main_account_screen():
    global main_screen
    global mybutton1
    global mybutton2
    global appearance_mode_optionemenu
    global color_them_optionmenu
    main_screen = customtkinter.CTk()
    main_screen.geometry(f"{300}x{250}")
    main_screen.eval('tk::PlaceWindow . center')
    main_screen.title("Make your perfect build")
    customtkinter.CTkLabel(master=main_screen, text="Welcome", font=("", 20)).pack(pady=1, padx=1)
    # Button(text="Login", height="2", width="30", command=login).pack()
    # Label(text="").pack()
    # Button(text="Register", height="2", width="30", command=register).pack()
    mybutton1 = bttn1(main_screen, "S I G N   I N ", '#25dae9', lambda :log(main_screen))
    mybutton2 = bttn1(main_screen, "S I G N   U P ", '#ffcc66', register)

    appearance_mode_optionemenu = customtkinter.CTkOptionMenu(master=main_screen, values=["Dark","Light"],
                                                              command=change_appearance_mode_event)
    appearance_mode_optionemenu.pack(pady=3,padx=5)

    color_them_optionmenu = customtkinter.CTkOptionMenu(master=main_screen, values=["green", "blue","dark-blue"],
                                                              command=change_set_default_color_theme)
    color_them_optionmenu.pack(pady=3,padx=5)

    print(main_screen.cget("fg_color"))


    main_screen.mainloop()


main_account_screen()
