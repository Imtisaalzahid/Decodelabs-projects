import tkinter as tk
from tkinter import ttk, scrolledtext
import datetime

class RuleBasedChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rule-Based AI Chatbot 🤖")
        self.root.geometry("550x650")
        self.root.configure(bg="#1e1e2e")
        
        self.is_active = True
        
        # Apply style configuration
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Configure Colors
        self.bg_dark = "#1e1e2e"
        self.bg_card = "#2b2b3b"
        self.accent_color = "#7f5af0"
        self.text_color = "#fffffe"
        self.bot_msg_color = "#94a3b8"
        
        self.setup_ui()
        
    def setup_ui(self):
        # Header Frame
        header_frame = tk.Frame(self.root, bg="#16161e", height=70)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="🤖 Rule-Based AI Assistant", 
            font=("Helvetica", 16, "bold"), 
            fg="#fffffe", 
            bg="#16161e"
        )
        title_label.pack(side=tk.LEFT, padx=20, pady=15)
        
        self.status_label = tk.Label(
            header_frame, 
            text="● Active", 
            font=("Helvetica", 10, "bold"), 
            fg="#2cb67d", 
            bg="#16161e"
        )
        self.status_label.pack(side=tk.RIGHT, padx=20, pady=15)
        
        # Chat Display Area
        chat_frame = tk.Frame(self.root, bg=self.bg_dark)
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame, 
            wrap=tk.WORD, 
            font=("Segoe UI", 11), 
            bg=self.bg_card, 
            fg=self.text_color,
            insertbackground="white",
            relief=tk.FLAT,
            bd=0,
            padx=15,
            pady=15
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        self.chat_display.config(state=tk.DISABLED)
        
        # Configure Tags for Message Styling
        self.chat_display.tag_config("user_tag", foreground="#7f5af0", font=("Segoe UI", 11, "bold"))
        self.chat_display.tag_config("bot_tag", foreground="#2cb67d", font=("Segoe UI", 11, "bold"))
        self.chat_display.tag_config("sys_tag", foreground="#ef4444", font=("Segoe UI", 10, "italic"))
        self.chat_display.tag_config("msg_body", foreground="#fffffe", font=("Segoe UI", 11))
        
        # Input Frame
        input_frame = tk.Frame(self.root, bg="#16161e", height=70)
        input_frame.pack(fill=tk.X, side=tk.BOTTOM)
        input_frame.pack_propagate(False)
        
        self.entry_box = tk.Entry(
            input_frame, 
            font=("Segoe UI", 12), 
            bg="#2b2b3b", 
            fg="#fffffe", 
            insertbackground="white",
            relief=tk.FLAT,
            bd=5
        )
        self.entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(15, 10), pady=15)
        self.entry_box.bind("<Return>", self.send_message)
        self.entry_box.focus()
        
        self.send_btn = tk.Button(
            input_frame, 
            text="Send ➔", 
            font=("Segoe UI", 11, "bold"), 
            bg=self.accent_color, 
            fg="#ffffff", 
            activebackground="#6246ea", 
            activeforeground="#ffffff",
            relief=tk.FLAT,
            bd=0,
            padx=20,
            cursor="hand2",
            command=self.send_message
        )
        self.send_btn.pack(side=tk.RIGHT, padx=(0, 15), pady=15)
        
        # Display Welcome Message
        self.append_message("Bot 🤖", "Hello! I am a rule-based AI chatbot. Type 'hello', 'how are you', 'what is your name', or 'bye' to exit!", "bot")

    def append_message(self, sender, text, msg_type):
        self.chat_display.config(state=tk.NORMAL)
        timestamp = datetime.datetime.now().strftime("%H:%M")
        
        if msg_type == "user":
            self.chat_display.insert(tk.END, f"\n{sender} ({timestamp}):\n", "user_tag")
            self.chat_display.insert(tk.END, f"{text}\n", "msg_body")
        elif msg_type == "bot":
            self.chat_display.insert(tk.END, f"\n{sender} ({timestamp}):\n", "bot_tag")
            self.chat_display.insert(tk.END, f"{text}\n", "msg_body")
        elif msg_type == "sys":
            self.chat_display.insert(tk.END, f"\n[System]: {text}\n", "sys_tag")
            
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.yview(tk.END)

    def send_message(self, event=None):
        if not self.is_active:
            return
            
        user_text = self.entry_box.get().strip()
        if not user_text:
            return
            
        self.entry_box.delete(0, tk.END)
        self.append_message("You", user_text, "user")
        
        # Process user input using rule-based decision logic (if-else)
        self.process_rules(user_text)

    def process_rules(self, raw_input):
        text = raw_input.lower().strip()
        
        # Core IF-ELSE Decision Logic
        if text in ["hello", "hi", "hey", "greetings", "good morning", "good evening"]:
            response = "Hello there! 👋 Welcome! How can I help you today?"
            self.append_message("Bot 🤖", response, "bot")
            
        elif text in ["bye", "exit", "quit", "goodbye", "see ya"]:
            response = "Goodbye! 👋 Have a wonderful day!"
            self.append_message("Bot 🤖", response, "bot")
            self.terminate_chat()
            
        elif "how are you" in text or "how do you do" in text:
            response = "I'm doing great, thank you for asking! 😊 Ready to help you."
            self.append_message("Bot 🤖", response, "bot")
            
        elif "name" in text or "who are you" in text:
            response = "I am RuleBot 🤖! A Python chatbot built with explicit if-else decision rules."
            self.append_message("Bot 🤖", response, "bot")
            
        elif "help" in text or "what can you do" in text:
            response = "I respond to predefined commands:\n• Greetings: hello, hi, hey\n• Questions: how are you, what is your name\n• Jokes: tell me a joke\n• Time: what time is it\n• Exit: bye, exit, quit"
            self.append_message("Bot 🤖", response, "bot")
            
        elif "joke" in text or "funny" in text:
            response = "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂"
            self.append_message("Bot 🤖", response, "bot")
            
        elif "time" in text or "clock" in text:
            now_str = datetime.datetime.now().strftime("%I:%M %p")
            response = f"The current time is 🕒 {now_str}."
            self.append_message("Bot 🤖", response, "bot")
            
        else:
            response = "I don't understand that command yet 🤔. Try saying 'hello', 'help', or 'bye'."
            self.append_message("Bot 🤖", response, "bot")

    def terminate_chat(self):
        self.is_active = False
        self.entry_box.config(state=tk.DISABLED)
        self.send_btn.config(state=tk.DISABLED, bg="#555555", cursor="default")
        self.status_label.config(text="● Disconnected", fg="#ef4444")
        self.append_message("System", "Chat loop terminated by exit command. Restart program to chat again.", "sys")

if __name__ == "__main__":
    root = tk.Tk()
    app = RuleBasedChatbotGUI(root)
    root.mainloop()
