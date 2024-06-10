import asyncio
import time
import customtkinter
import threading

class Message(customtkinter.CTkFrame):
    def __init__(self, master, author: str, message: str):
        super().__init__(master)
        self.author = customtkinter.CTkLabel(self, width=380, text=author.capitalize(), justify="left", compound="left", font=("Arial", 12, "bold")).pack()
        self.text = customtkinter.CTkTextbox(self, width=370, font=("Arial", 12))
        self.text.insert("0.0", message)
        self.text.pack()
        
class MainFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, width=380, height=730)

    def add(self, message: Message):
        message.pack(pady=10)

class App(customtkinter.CTk):
    def __init__(self):
        customtkinter.CTk.__init__(self)
        self.title("Local GPT")
        self.geometry("400x800")
        self.resizable(0, 0)
        self.attributes("-topmost", True)
        
        self.prompt = customtkinter.CTkEntry(self, width=360)
        self.prompt.place(rely=0.982, relx=0.47, anchor="s")
        
        self.send_button = customtkinter.CTkButton(self, text="✅", command=self.on_send, width=20)
        self.send_button.place(rely=0.982, relx=0.96, anchor="s")
        
        self.main_frame = MainFrame(self)
        self.main_frame.place(y=0, x=0, anchor="nw")
        
        self.bind('<Return>', self.on_send)
        
        self.mainloop()
        
    def add_message(self, author: str, message: str):
        message = Message(self.main_frame, author=author, message=message)
        self.main_frame.add(message)