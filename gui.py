import customtkinter as ctk
import os 
import csv
import tkinter.messagebox as tkmb

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("MAXeth Streaming Service")

def open_window_login(): # Function which opens a new window after successful login
    new_window = ctk.CTkToplevel(app)
    new_window.title("new window")
    new_window.geometry("600x700")
    
    ctk.CTkLabel(new_window, text="MAXeth Streaming Service", font=("Arial", 24, "bold")).pack(pady=20) # Bolded Heading for name of streaming service
    search_bar = ctk.CTkEntry(new_window, placeholder_text="Search Movies...") # Search bar
    search_bar.pack(pady=10)
    
    filterborder = ctk.CTkFrame(new_window)
    filterborder.pack(pady=10, padx=10, fill='x')
    
    ctk.CTkLabel(filterborder, text="Genre:").pack(side="left", padx=5)
    genre_options = ctk.CTkOptionMenu(filterborder, values=["All", "Action", "Comedy"])
    genre_options.pack(side="left", padx=5)
    
    ctk.CTkLabel(filterborder, text="Genre:").pack(side="left", padx=5)
    type_options = ctk.CTkOptionMenu(filterborder, values=["All", "Movie", "Series"])
    type_options.pack(side="left", padx=5)
    
    ctk.CTkLabel(filterborder, text="Genre:").pack(side="left", padx=5)
    rating_options = ctk.CTkOptionMenu(filterborder, values=["All", "G", "PG", "PG-13", "MA-15", "R"])
    rating_options.pack(side="left", padx=5)
    
def login():
    username = "test"
    password = "test2"

    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Login Successful",message="You have logged in successfully")
        app.withdraw() # Hides the login window
        open_window_login() # Calls the new window function
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title='Wrong password',message='Please check your password')
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title='Wrong username',message='Please check your username')
    else:
        tkmb.showerror(title="Login failed",message="Invalid Username and password")
    
label = ctk.CTkLabel(app, text = "Login")
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both',expand=True)

label = ctk.CTkLabel(master=frame,text="Login to MAXeth Streaming Services!")
label.pack(pady=12,padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text = "Username")
user_entry.pack(pady=12,padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text = "Password",show=("*"))
user_pass.pack(pady=12,padx=10)

loginbutton = ctk.CTkButton(master=frame,text='Login' ,command=login)
loginbutton.pack(pady=12,padx=10)

checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me')
checkbox.pack(pady=12,padx=10)


app.mainloop()