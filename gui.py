import customtkinter as ctk
import os 
import csv

ctk.set_appearnce_mode("dark")
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
                            
label = ctk.CTkLabel(self, text = "Login")
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both',expand=True)

label = ctk.CTkLabel(master=frame,text="main login")
label.pack(pady=12,padx=10)

user_entry = ctk.CTkEntry(master=frame, text = "Login Here")
user_entry.pack(pady=20)

button = ctk.CTkButton(master=frame,text='Login' ,command=login)
button.pack(pady=12,padx=10)

checkbox = ctk.CTKCheckBox(master=frame,text='Remember Me')
checkbox.pack(pady=12,padx=10)

app.mainloop()