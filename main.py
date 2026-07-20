import customtkinter as ctk

def show_message():
    app = ctk.CTk()
    app.geometry("512x512")
    app.title("Advice")

    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
 
    label = ctk.CTkLabel(app, text="Should I use venvs?\nYes, Always!", font=("Arial", 20))
    label.grid(row=0, column=0, sticky="nsew")
    
    app.mainloop()

if __name__ == "__main__":
    show_message()
