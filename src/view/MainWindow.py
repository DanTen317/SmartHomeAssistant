import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from customtkinter import CTkImage

from src.controller.AppController import AppController


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.app_controller = AppController()
        self.app_controller.startup_conf()
        self.file_path = None
        self.latest_response = None

        self.title("Smart Home Assitant")

        self.configure(bg="#282828", padx=5, pady=5)
        self.geometry("350x500")
        self.minsize(200, 300)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.buttons_frame = ButtonsFrame(self)
        self.buttons_frame.grid(row=1, column=0, pady=5, sticky=tk.NSEW)

        self.mainloop()

    def upload_action(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[('Audio files', '*.wav')]
        )
        if self.file_path:
            print(self.file_path)
            self.buttons_frame.update()

    def run_uploaded(self):
        if self.file_path and self.file_path != "" and self.file_path.endswith(".wav"):
            result_status =self.app_controller.run_command_from_file(self.file_path)
            messagebox.showinfo("Запустить из файла", result_status)
            self.file_path = None
            self.latest_response = result_status
            self.buttons_frame.update()

    def record_action(self):
        result_status = self.app_controller.record_and_run()
        messagebox.showinfo("Записать и запустить", result_status)
        self.latest_response = result_status
        self.buttons_frame.play_button.grid_remove()
        self.buttons_frame.update()

    def play_response(self):
        if self.latest_response:
            self.app_controller.voice_interface.respond_to_user(self.latest_response)
        self.latest_response = None
        self.buttons_frame.play_button.grid_remove()
        self.buttons_frame.update()



class ButtonsFrame(ctk.CTkFrame):
    def __init__(self, parent: MainWindow):
        super().__init__(parent)
        # load icon
        self.parent = parent
        upload_icon = Image.open("./assets/upload.png")
        upload_icon = ctk.CTkImage(upload_icon, size=(32, 32))
        record_icon = Image.open("./assets/voice.png")
        record_icon = ctk.CTkImage(record_icon, size=(32, 32))

        self.upload_button = ctk.CTkButton(self, text="Выберите голосовое \nсообщение",
                                           image=upload_icon,
                                           compound=tk.RIGHT,
                                           corner_radius=8,
                                           fg_color="#d9d9d9",
                                           hover_color="#8c8c8c",
                                           text_color="#010101",
                                           text_color_disabled="f1f1f1",
                                           command=self.parent.upload_action)

        self.run_button = ctk.CTkButton(self, text="Запустить",
                                        compound=tk.RIGHT,
                                        corner_radius=8,
                                        fg_color="#d9d9d9",
                                        hover_color="#8c8c8c",
                                        text_color="#010101",
                                        text_color_disabled="f1f1f1",
                                        command=self.parent.run_uploaded)

        self.record_button = ctk.CTkButton(self, text="Записать голосовое \nсообщение",
                                           image=record_icon,
                                           compound=tk.RIGHT,
                                           corner_radius=8,
                                           fg_color="#d9d9d9",
                                           hover_color="#8c8c8c",
                                           text_color="#010101",
                                           text_color_disabled="f1f1f1",
                                           command=self.parent.record_action)

        self.play_button = ctk.CTkButton(self, text="Воспроизвести",
                                         compound=tk.RIGHT,
                                         corner_radius=8,
                                         fg_color="#d9d9d9",
                                         hover_color="#8c8c8c",
                                         text_color="#010101",
                                         text_color_disabled="f1f1f1",
                                         command=self.parent.play_response)

        self.grid_columnconfigure(0, weight=1)
        self.upload_button.grid(row=0, column=0, pady=8)
        self.record_button.grid(row=1, column=0, pady=8)

    def update(self):
        if self.parent.file_path and self.parent.file_path != "" and self.parent.file_path.endswith(".wav"):
            upload_name = self.parent.file_path.split("/")[-1]
            self.upload_button.configure(text=upload_name)
            self.upload_button.grid(row=0, column=0, pady=8)
            self.run_button.grid(row=1, column=0, pady=8)
            self.record_button.grid(row=2, column=0, pady=8)
            if self.parent.latest_response is not None:
                self.play_button.grid(row=3, column=0, pady=8)
        else:
            self.upload_button.configure(text="Выберите голосовое \nсообщение")
            self.upload_button.grid(row=0, column=0, pady=8)
            self.record_button.grid(row=1, column=0, pady=8)
            if self.parent.latest_response is not None:
                self.play_button.grid(row=2, column=0, pady=8)
