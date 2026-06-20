import customtkinter as ctk
import os 
import csv
import tkinter.messagebox as tkmb
import PIL
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x550")
app.title("MAXeth Streaming Service")

viewing_history = "history.csv"
watchlist = []
movies = [
    {"Title": "The Matrix", "genre": "Sci-Fi", "type": "Movie", "rating": "MA-15"},
    {"Title": "Inception", "genre": "Sci-Fi", "type": "Movie", "rating": "M"},
    {"Title": "The Dark Knight", "genre": "Action", "type": "Movie", "rating": "M"},
    {"Title": "Interstellar", "genre": "Sci-Fi", "type": "Movie", "rating": "M"},
    {"Title": "Titanic", "genre": "Romance", "type": "Movie", "rating": "M"},
    {"Title": "Jurassic Park", "genre": "Adventure", "type": "Movie", "rating": "PG"},
    {"Title": "Avengers: Endgame", "genre": "Action", "type": "Movie", "rating": "M"},
    {"Title": "Toy Story", "genre": "Animation", "type": "Movie", "rating": "G"},
    {"Title": "The Shawshank Redemption", "genre": "Drama", "type": "Movie", "rating": "MA-15"},
    {"Title": "Spider-Man: Into the Spider-Verse", "genre": "Animation", "type": "Movie", "rating": "PG"}
]

if not os.path.exists(viewing_history):
    with open(viewing_history, "w", newline="") as f:
        csv.writer(f).writerow(["movies"])

def add_to_viewing_history(movies):
    with open(viewing_history, "a", newline="") as f:
        csv.writer(f).writerow([movies])

def get_viewing_history():
    with open(viewing_history, "r") as f:
        reader = csv.reader(f)
        next(reader)
        return[row[0] for row in reader]
    
class AccountCredentials:
    def __init__(self, name, email, password, subscription_plan, profiles=None):
        self.name = name
        self.email = email
        self.password = password
        self.subscription_plan = subscription_plan
        self.profiles = profiles if profiles else []
    
    def check_password(self, attempt):
        return self.password == attempt
    
    def save_to_csv(self, filename="accounts.csv"):
        file_exists = os.path.exists(filename)
        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["name", "email", "password", "subscription_plan", "profiles"])
            writer.writerow([self.name, self.email, self.password, self.subscription_plan, ";".join(self.profiles)])
    
test_account = AccountCredentials(
    name="MrDunne",
    email="ryan.dunne9@det.nsw.gov.au",
    password="Baulko11!!",
    subscription_plan="Premium",
    profiles=["Profile 1"]
)
test_account.save_to_csv()

def create_profile(): 
    new_window2 = ctk.CTkToplevel(app) #creates new window for profile creation
    new_window2.title("MAXeth Profile Creation")
    new_window2.geometry("600x600")

    ctk.CTkLabel(new_window2, text="Create your profile", font=("Arial", 24, "bold")).pack(pady=20)

    username = ctk.CTkEntry(new_window2, placeholder_text="Create a username")
    username.pack(pady=15) #Profile does not need a password due to already logging in to an account

    age_options = [str(i) for i in range(5,101)]
    age = ctk.CTkComboBox(new_window2, values=age_options, width=150)
    age.set("Select Age")
    age.pack(pady=10)

    def create():
        new_window2.destroy()
        open_window_login()

    create_button = ctk.CTkButton(new_window2, text="Create", command=create)
    create_button.pack(pady=10)

def profile():
    new_window1 = ctk.CTkToplevel(app)
    new_window1.title("MAXeth Profile Selection")
    new_window1.geometry("1920x1080")    
    
    profile_window = ctk.CTkFrame(new_window1)
    profile_window.pack(pady=20,padx=40, fill='both',expand='True')

    def create1():
        new_window1.destroy()
        create_profile()

    def profile1():
        new_window1.destroy()
        open_window_login()

    ctk.CTkLabel(profile_window, text="Choose your profile", font=("Arial", 24, "bold")).pack(pady=20)
    create_button = ctk.CTkButton(profile_window, text="Create a profile", width=200, height=90, command=create1)
    create_button.pack(pady=20,padx=20)
    user_profile = ctk.CTkButton(profile_window, text = "Profile 1", width = 200, height=90, command=profile1)
    user_profile.pack(pady=20,padx=20)
    
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
    
    def add_movie():
        movie = add_entry.get().strip()
        if movie and movie not in watchlist:
            watchlist.append(movie)
            add_entry.delete(0, "end")
            watchlist_box.delete("1.0", "end")
            for item in watchlist:
                watchlist_box.insert("end", f"{item}\n")
                
    def remove_movie():
        movie = add_entry.get().strip()
        if movie in watchlist:
            watchlist.remove(movie)
            add_entry.delete(0, "end")
            if watchlist:
                for item in watchlist:
                    watchlist_box.insert("end", f"{item}\n")
            else:
                watchlist_box.insert("end", "Your Watchlist is currently empty.")
    
    ctk.CTkButton(watchlist_window, text="Add", command=add_movie).pack(pady=5)
    ctk.CTkButton(watchlist_window, text="Remove", command=remove_movie).pack(pady=5)
    
def open_subscription():
    sub_window = ctk.CTkToplevel(app)
    sub_window.title("Subscription Management")
    sub_window.geometry("400x500")
    
    ctk.CTkLabel(sub_window, text="My Subscription", font=("Arial", 20, "bold")).pack(pady=20)
    
    ctk.CTkLabel(sub_window, text="Current Plan:", font=("Arial",14)).pack(pady=5)
    current_plan_label = ctk.CTkLabel(sub_window, text=test_account.subscription_plan, font=("Arial",12))
    current_plan_label.pack(pady=5)
    
    ctk.CTkLabel(sub_window, text="Change Plan:", font=("Arial",14)).pack(pady=10)
    plan_options = ctk.CTkOptionMenu(sub_window, values=["Basic", "Standard", "Premium"])
    plan_options.pack(pady=5)
    
    def change_plan():
        new_plan = plan_options.get()
        test_account.subscription_plan = new_plan
        current_plan_label.configure(text=new_plan)
        tkmb.showinfo("Plan Updated", f"Your plan has been changed to {new_plan}")
    
    ctk.CTkButton(sub_window, text="Confirm Change", command=change_plan).pack(pady=10)

def viewing_report():
    report_window = ctk.CTkToplevel(app)
    report_window.title("Viewing Report")
    report_window.geometry("400x500")
    report_window.after(10, report_window.lift)
    
    ctk.CTkLabel(report_window, text="Viewing Report", font=("Arial", 20, "bold")).pack(pady=20)
    
    report_box = ctk.CTkTextbox(report_window, width=350, height=300)
    report_box.pack(pady=10, padx=10)
    
    def save_report():
        history = get_viewing_history()
        with open("viewing_report.txt", "w") as f:
            f.write("MAXeth Streaming Service - Viewing report\n")
            f.write("Watch History\n")
            if history:
                for movie in history:
                    f.write(f"- {movie}\n")
            else:
                f.write("No History\n")
        tkmb.showinfo("saved", "report saved as viewing_report.txt")
    
    ctk.CTkButton(report_window, text="Save Report", command=save_report).pack(pady=10)
    
def play_content(movie_name):
    play_window = ctk.CTkToplevel(app)
    play_window.title(movie_name)
    play_window.geometry("500x400")
    
    ctk.CTkLabel(play_window, text=movie_name, font=("Arial", 20, "bold")).pack(pady=20)
    ctk.CTkLabel(play_window, text="🎬", font=("Arial", 80)).pack(pady=20)
    ctk.CTkLabel(play_window, text="Now Playing...").pack(pady=5)
    
    add_to_viewing_history(movie_name)

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
    ctk.CTkButton(new_window, text="Viewing Report", command=viewing_report).pack(pady=10)
    
    movie_buttons_frame = ctk.CTkFrame(new_window)
    movie_buttons_frame.pack(pady=10, padx=10, fill='x')
    
    def display_movies(filtered_list):
        for widget in movie_buttons_frame.winfo_children():
            widget.destroy()
        for movie in filtered_list:
            ctk.CTkButton(movie_buttons_frame, text=movie["Title"], command=lambda m=movie: play_content(m["Title"])).pack(pady=2)
    
    def filter_movies():
        genre = genre_options.get()
        content_type = type_options.get()
        rating = rating_options.get()
        
        filtered = movies
        if genre != "All":
            filtered = [m for m in filtered if m["genre"] == genre]
        if content_type != "All":
            filtered = [m for m in filtered if m["type"] == content_type]
        if rating != "All":
            filtered = [m for m in filtered if m["rating"] == rating]
        display_movies(filtered)
        
    ctk.CTkButton(filterborder, text="Filter", command=filter_movies).pack(side="left", padx=5)
    display_movies(movies)

def new_account():
    new_window3 = ctk.CTkToplevel(app) #creates new window for profile creation
    new_window3.title("MAXeth Account Creation")
    new_window3.geometry("600x600")

    ctk.CTkLabel(new_window3, text="Sign up to MAXeth", font=("Arial", 24, "bold")).pack(pady=20)

    acc_username = ctk.CTkEntry(new_window3, placeholder_text="Create a username")
    acc_username.pack(pady=15)

    acc_password = ctk.CTkEntry(new_window3, placeholder_text="Create a password")
    acc_password.pack(pady=15)

    confirm_password = ctk.CTkEntry(new_window3, placeholder_text="Confirm your password")
    confirm_password.pack(pady=15)

    def signup():
        if acc_password.get() != confirm_password.get():
            tkmb.showerror(title="Passwords don't match")
        else:
            tkmb.showinfo(title="Account created")
            new_window3.destroy()
            app.mainloop()

    create_button = ctk.CTkButton(new_window3, text="Create", command=signup)
    create_button.pack(pady=10)
def login(): #Function for the login page
    if user_entry.get() == test_account.name and test_account.check_password(user_pass.get()):
        tkmb.showinfo(title="Login Successful",message="You have logged in successfully")
        app.withdraw() # Hides the login window
        profile() #Calls profile function
    elif user_entry.get() == test_account.name and not test_account.check_password(user_pass.get()):
        tkmb.showwarning(title='Wrong password',message='Please check your password')
    elif user_entry.get() != test_account.name and test_account.check_password(user_pass.get()):
        tkmb.showwarning(title='Wrong username',message='Please check your username')
    else:
        tkmb.showerror(title="Login failed",message="Invalid Username and password")
    

label = ctk.CTkLabel(app, text = "Login")
logo_image = ctk.CTkImage(light_image=Image.open("maxethlogo.png"), dark_image=Image.open("maxethlogo.png"), size=(100,100))
logo_label = ctk.CTkLabel(app, image=logo_image, text="")
logo_label.pack(pady=10)
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

new = ctk.CTkLabel(app, text = "Don't have an account? Sign Up!")
new.pack(pady=20)

signup_button = ctk.CTkButton(app, text="Sign Up", command=new_account)
signup_button.pack(pady=12,padx=10)



app.mainloop()