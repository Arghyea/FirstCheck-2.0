# chatbot_ui.py

import customtkinter as ctk
from chatbot_logic import ChatbotLogic
import datetime

class ChatbotUI:
    def __init__(self, root):
        self.root = root

        # Sidebar layout
        self.sidebar = ctk.CTkFrame(root, width=200)
        self.sidebar.pack(side="left", fill="y")

        self.main_frame = ctk.CTkFrame(root)
        self.main_frame.pack(side="right", fill="both", expand=True)

        # Chat display
        self.top_bar = ctk.CTkFrame(self.main_frame)
        self.top_bar.pack(fill="x", padx=10, pady=(10, 0))

        self.toggle_button = ctk.CTkButton(
        self.top_bar,
            text="☰",
            width=40,
            height=30,
            command=self.toggle_sidebar
        )
        self.toggle_button.pack(side="left")



        self.chat_display = ctk.CTkTextbox(self.main_frame, font=("Arial", 12), wrap="word")
        self.chat_display.pack(padx=10, pady=(10, 0), fill="both", expand=True)
        self.chat_display.configure(state="disabled")

        # Options frame
        self.options_frame = ctk.CTkFrame(self.main_frame)
        self.options_frame.pack(fill="x", padx=10, pady=(5, 0))

        # Input frame
        self.input_frame = ctk.CTkFrame(self.main_frame)
        self.input_frame.pack(fill="x", padx=10, pady=10)

        self.entry = ctk.CTkEntry(self.input_frame)
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.entry.bind("<Return>", self.process_input)

        self.send_button = ctk.CTkButton(self.input_frame, text="Send", command=self.process_input)
        self.send_button.pack(side="right", padx=(0, 10))

        self.reset_button = ctk.CTkButton(self.input_frame, text="Reset", command=self.clear_chat)
        self.reset_button.pack(side="right", padx=(0, 10))

        # Sidebar controls
        self.new_chat_button = ctk.CTkButton(self.sidebar, text="+ New Chat", command=self.new_chat)
        self.new_chat_button.pack(pady=10, padx=10)

        self.delete_button = ctk.CTkButton(self.sidebar, text="🗑️ Delete Chat", command=self.delete_chat)
        self.delete_button.pack(pady=(0, 10), padx=10)

        self.chat_list_frame = ctk.CTkScrollableFrame(self.sidebar)
        self.chat_list_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # Session tracking
        self.chat_sessions = []
        self.chat_buttons = []
        self.session_titles = []
        self.current_session_index = -1

        self.new_chat()

        # Add toggle button (top-left, absolute position)

        self.sidebar_visible = True
        

    def new_chat(self):
        if self.current_session_index >= 0:
            self.chat_sessions[self.current_session_index] = self.chatbot.history[:]

        now = datetime.datetime.now().strftime("%H:%M")
        self.chat_sessions.append([])
        self.session_titles.append(f"Chat {len(self.chat_sessions)} - {now}")
        self.current_session_index = len(self.chat_sessions) - 1

        self.add_sidebar_button(self.current_session_index)
        self.clear_chat()
        self.chatbot = ChatbotLogic(self)
        self.chatbot.reset()
        self.update_sidebar_highlight()

    def delete_chat(self):
        if self.current_session_index >= 0:
            del self.chat_sessions[self.current_session_index]
            del self.session_titles[self.current_session_index]
            self.chat_buttons[self.current_session_index].destroy()
            del self.chat_buttons[self.current_session_index]

            if self.chat_sessions:
                self.current_session_index = max(0, self.current_session_index - 1)
                self.load_chat_session(self.current_session_index)
            else:
                self.current_session_index = -1
                self.clear_chat()
        self.update_sidebar_highlight()

    def add_sidebar_button(self, index):
        button = ctk.CTkButton(
            self.chat_list_frame,
            text=self.session_titles[index],
            command=lambda i=index: self.load_chat_session(i)
        )
        button.pack(fill="x", pady=2)
        self.chat_buttons.append(button)

    def update_sidebar_highlight(self):
        for i, btn in enumerate(self.chat_buttons):
            btn.configure(fg_color="#3B82F6" if i == self.current_session_index else "transparent")

    def load_chat_session(self, index):
        if self.current_session_index >= 0:
            self.chat_sessions[self.current_session_index] = self.chatbot.history[:]

        self.current_session_index = index
        self.clear_chat()
        self.chatbot = ChatbotLogic(self)
        self.chatbot.history = self.chat_sessions[index][:]
        for role, msg in self.chatbot.history:
            if role == "User":
                self.display_user(msg, save=False)
            else:
                self.display_bot(msg, save=False)
        self.update_sidebar_highlight()

    def process_input(self, event=None):
        text = self.entry.get().strip()
        if not text:
            return
        self.display_user(text)
        self.entry.delete(0, "end")
        self.clear_options()
        self.chatbot.handle_free_text(text)

    def display_user(self, text, save=True):
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", f"You: {text}\n")
        self.chat_display.configure(state="disabled")
        self.chat_display.see("end")
        if save:
            self.chatbot.history.append(("User", text))

    def display_bot(self, text, save=True):
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", f"Bot: {text}\n\n")
        self.chat_display.configure(state="disabled")
        self.chat_display.see("end")
        if save:
            self.chatbot.history.append(("Bot", text))

    def show_options(self, options):
        self.clear_options()
        for label, callback in options:
            btn = ctk.CTkButton(self.options_frame, text=label, command=callback)
            btn.pack(side="left", padx=5, pady=5)

    def clear_options(self):
        for widget in self.options_frame.winfo_children():
            widget.destroy()

    def clear_chat(self):
        self.chat_display.configure(state="normal")
        self.chat_display.delete("1.0", "end")
        self.chat_display.configure(state="disabled")
        self.clear_options()

    def toggle_sidebar(self):
        if self.sidebar_visible:
            self.sidebar.pack_forget()
            self.sidebar_visible = False
        else:
            self.sidebar.pack(side="left", fill="y")
            self.sidebar_visible = True

