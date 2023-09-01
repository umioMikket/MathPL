import tkinter as tk

class Console():
    text = []

    # Тип выводов сообщений 
    def info(self, message): 
        self.text += " INFO ", "info", " " + message + "\n", "default"
    def warning(self, message): 
        self.text += " WARNING ", "warning", " " + message + "\n", "default"
    def error(self, message):
        self.text += " ERROR ", "error", " " + message + "\n", "default"

    def show(self):
        window = tk.Tk()
        window.title("MathPL")
        
        text = tk.Text(window, background="#3b3737")
        text.pack(expand=True, fill="both")
        
        # Настройка сообщений
        text.tag_config("info", background="#3b8cff", foreground="#3b3737")
        text.tag_config("warning", background="#ff9d3b", foreground="#3b3737")
        text.tag_config("error", background="#ff3b3b", foreground="#3b3737")
        text.tag_config("debug", background="#3bff7c", foreground="#3b3737")
        text.tag_config("default", foreground="white")

        # Добавление собщений
        for element in range(0, len(self.text), 2):
            text.insert("end", self.text[element], self.text[element + 1])
        
        text.config(state="disabled")
        
        window.mainloop()
