# app.py
import customtkinter as ctk
from chatbot_ui import ChatbotUI

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("720x600")
    root.title("FirstCheck")

    ChatbotUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
