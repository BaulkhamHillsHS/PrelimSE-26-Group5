import customtkinter as ctk
import os 
import csv

class MainPage(ctk.CTk):
    def __init__(self):
        super().__init__
        self.title("Maxeth Streaming Client")
        self.geometry("600x400")
        self.build_ui()