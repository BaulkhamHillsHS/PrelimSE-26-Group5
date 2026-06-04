import customtkinter as ctk
import os 
import csv

class MainPage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Maxeth")

app = MainPage()
app.mainloop()

def login():
    username = "test"
    password = "test2"
    
    new_window = ctk.CTkTopLevel(app)
    new_window.title("new window")
    new_window.geometry("350x150")
    
    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo("title="Login Sucessful", 
        message="You have logged in")
        ctk.CTkLavel(new_window,
                     text="bruh").pack()