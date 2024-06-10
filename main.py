import App
import generator
from tkinter import messagebox

model = generator.Model(open('model_path.txt', 'r').read())

class App(App.App):
    def on_send(self, *args):
        text = self.prompt.get()
        self.add_message("You", text)
        self.prompt.delete(0, 'end')
        if text:
            print(text)
            response = model.generate(text)
            self.add_message(response.role, response.response)
        else:
            messagebox.showinfo("Error", "Please enter a prompt.")
            
app = App()