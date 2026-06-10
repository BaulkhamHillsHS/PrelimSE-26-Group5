import customtkinter as ctk
import os 
import csv

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("MAXeth Streaming Services")

def login():
    username = "test"
    password = "test2"
    
    new_window = ctk.CTkTopLevel(app)
    new_window.title("new window")
    new_window.geometry("350x150")
    
label = ctk.CTkLabel(app, text = "Login")
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both',expand=True)

label = ctk.CTkLabel(master=frame,text="main login")
label.pack(pady=12,padx=10)

user_entry = ctk.CTkEntry(master=frame, text = "Login Here")
user_entry.pack(pady=20)

loginbutton = ctk.CTkButton(master=frame,text='Login' ,command=login)
loginbutton.pack(pady=12,padx=10)

checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me')
checkbox.pack(pady=12,padx=10)

def searchbar():

textbox = ctk.CTkTextbox(
    master=app,
    width=400,
    height=200,
    corner_radius=10,
    border_width=2
)
textbox.pack(pady=20, padx=20, fill="both", expand=True)


app.mainloop()