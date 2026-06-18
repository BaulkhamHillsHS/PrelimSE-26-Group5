import customtkinter as ctk
import os 
import csv
import tkinter.messagebox as tkmb
import PIL

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("MAXeth Streaming Service")

def create_profile(): 
    new_window2 = ctk.CTkToplevel(app) #creates new window for profile creation
    new_window2.title("MAXeth Profile Creation")
    new_window2.geometry("600x600")

    ctk.CTkLabel(new_window2, text="Create your profile", font=("Arial", 24, "bold")).pack(pady=20)

    username = ctk.CTkEntry(new_window2, placeholder_text="Create a username")
    username.pack(pady=12,padx=10)

    password = ctk.CTkEntry(new_window2, placeholder_text="Create a password")
    password.pack(pady=12,padx=10)

    create_button = ctk.CTkButton(new_window2, text="Create", command=open_window_login)
    create_button.pack(pady=10)

def profile():
    new_window1 = ctk.CTkToplevel(app)
    new_window1.title("MAXeth Profile Selection")
    new_window1.geometry("1920x1080")    
    
    profile_window = ctk.CTkFrame(new_window1)
    profile_window.pack(pady=20,padx=40, fill='both',expand='True')

    ctk.CTkLabel(profile_window, text="Choose your profile", font=("Arial", 24, "bold")).pack(pady=20)
    create = ctk.CTkButton(profile_window, text="Create a profile",command=create_profile)
    create.pack(pady=20,padx=20)
    
def open_watchlist():
    watchlist_window = ctk.CTkToplevel(app)
    watchlist_window.title("My Watchlist")
    watchlist_window.geometry("400x500")
    ctk.CTkLabel(watchlist_window, text="My Watchlist", font=("Arial", 20, "bold")).pack(pady=20)
    
    watchlist_box = ctk.CTkTextbox(watchlist_window, width = 350, height = 250)
    watchlist_box.pack(pady=10, padx=10)
    watchlist_box.insert("end", "Your watchlist is currently empty.")
    
    add_entry = ctk.CTkEntry(watchlist_window, placeholder_text="Add a movie to your watchlist")
    add_entry.pack(pady=5)
    
    ctk.CTkButton(watchlist_window, text="Add").pack(pady=5)
    ctk.CTkButton(watchlist_window, text="Remove").pack(pady=5)
    
def open_subscription():
    sub_window = ctk.CTkToplevel(app)
    sub_window.title("Subscription Management")
    sub_window.geometry("400x500")
    
    ctk.CTkLabel(sub_window, text="My Subscription", font=("Arial", 20, "bold")).pack(pady=20)
    
    ctk.CTkLabel(sub_window, text="Current Plan:", font=("Arial",14)).pack(pady=5)
    ctk.CTkLabel(sub_window, text="Basic:", font=("Arial",12)).pack(pady=5)
    
    ctk.CTkLabel(sub_window, text="Change Plan:", font=("Arial",14)).pack(pady=10)
    plan_options = ctk.CTkOptionMenu(sub_window, values=["Basic", "Standard", "Premium"])
    plan_options.pack(pady=5)
  

def open_window_login(): # Function which opens a new window after successful login
    new_window = ctk.CTkToplevel(app)
    new_window.title("MAXeth Streaming Service")
    new_window.geometry("1920x1080")
    
    ctk.CTkLabel(new_window, text="MAXeth Streaming Service", font=("Arial", 24, "bold")).pack(pady=20) # Bolded Heading for name of streaming service
    search_bar = ctk.CTkEntry(new_window, placeholder_text="Search Movies...") # Search bar
    search_bar.pack(pady=10)
    
    filterborder = ctk.CTkFrame(new_window)
    filterborder.pack(pady=10, padx=10, fill='x')
    
    ctk.CTkLabel(filterborder, text="Genre:").pack(side="left", padx=5)
    genre_options = ctk.CTkOptionMenu(filterborder, values=["All", "Action", "Comedy"])
    genre_options.pack(side="left", padx=5)
    
    ctk.CTkLabel(filterborder, text="Type:").pack(side="left", padx=5)
    type_options = ctk.CTkOptionMenu(filterborder, values=["All", "Movie", "Series"])
    type_options.pack(side="left", padx=5)
    
    ctk.CTkLabel(filterborder, text="Rating:").pack(side="left", padx=5)
    rating_options = ctk.CTkOptionMenu(filterborder, values=["All", "G", "PG", "PG-13", "MA-15", "R"])
    rating_options.pack(side="left", padx=5)
    
    ctk.CTkButton(new_window, text="My Watchlist", command=open_watchlist).pack(pady=10)
    ctk.CTkButton(new_window, text="Subscription Management", command=open_subscription).pack(pady=10)

    ctk.CTkButton(new_window, text="Movie 1")
    
def login(): #Function for the login page
    username = "test"
    password = "test2"

    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Login Successful",message="You have logged in successfully")
        app.withdraw() # Hides the login window
        profile() #Calls profile function
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