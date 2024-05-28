import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from smart_mirror_manager import SmartMirrorHelper


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Mirror")
        self.geometry("1900x1000")
        self.style = ttk.Style()
        self.style.configure(
            "Transparent.TLabel", background="black", foreground="white"
        )
        self.style.configure("Transparent.TFrame", background="black")

        self.create_widgets()
        self.smartMirrorHelper = SmartMirrorHelper(self)
        self.button_frame_visibility.config(
            command=self.smartMirrorHelper.toggle_frame_visibility
        )
        self.button_font.config(command=self.smartMirrorHelper.change_font)
        self.smartMirrorHelper.update_camera()
        self.smartMirrorHelper.update_time()
        self.smartMirrorHelper.update_weather()
        self.smartMirrorHelper.update_traffic()
        self.smartMirrorHelper.update_news()

        self.mainloop()

    def create_widgets(self):
        self.create_main_frame()
        self.create_date_and_time_frame()
        self.create_weather_frame()
        self.create_traffic_frame()
        self.create_news_frame()

    def create_main_frame(self):
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(self.main_frame)
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        image = Image.open(r"push.png")
        image = image.resize((50, 50), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        self.button_frame_visibility = tk.Button(
            self.main_frame, image=self.photo, width=50, height=50
        )
        self.button_frame_visibility.place(relx=0.9, rely=0.6)
        self.button_font = tk.Button(
            self.main_frame, image=self.photo, width=50, height=50
        )
        self.button_font.place(relx=0.9, rely=0.7)

    def create_date_and_time_frame(self):
        self.date_and_time_frame = ttk.Frame(
            self.main_frame, padding=10, style="Transparent.TFrame"
        )
        self.date_and_time_frame.place(relx=0.05, rely=0.05, anchor=tk.NW)
        self.time_label = ttk.Label(
            self.date_and_time_frame,
            text="",
            style="Transparent.TLabel",
        )
        self.time_label.pack()

    def create_weather_frame(self):
        self.weather_frame = ttk.Frame(self.main_frame, style="Transparent.TFrame")
        self.weather_frame.place(relx=0.05, rely=0.25, anchor=tk.NW)
        self.weather_label = ttk.Label(
            self.weather_frame,
            text="",
            style="Transparent.TLabel",
        )
        self.weather_label.pack()

    def create_traffic_frame(self):
        self.traffic_frame = ttk.Frame(self.main_frame, style="Transparent.TFrame")
        self.traffic_frame.place(relx=0.95, rely=0.05, anchor=tk.NE)
        self.traffic_text = tk.Text(
            self.traffic_frame,
            bd=0,
            bg="black",
            fg="white",
            highlightthickness=0,
            wrap=tk.WORD,
            width=30,
            height=10,
        )
        self.traffic_text.pack(fill=tk.BOTH, expand=True)

    def create_news_frame(self):
        self.news_frame = ttk.Frame(self.main_frame, style="Transparent.TFrame")
        self.news_frame.place(relx=0.5, rely=0.95, anchor=tk.S)
        self.news_text = tk.Text(
            self.news_frame,
            bd=0,
            bg="black",
            fg="white",
            highlightthickness=0,
            wrap=tk.WORD,
            width=80,
            height=5,
        )
        self.news_text.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    app = Application()
