import tkinter as tk
from PIL import Image, ImageTk
import cv2
import time
import weather
import traffic
import news


class SmartMirrorHelper:
    def __init__(self, app):
        self.app = app
        self.frames = [
            app.date_and_time_frame,
            app.weather_frame,
            app.traffic_frame,
            app.news_frame,
        ]
        self.fonts = [8, 14, 20]
        self.current_font_index = 0
        self.font = self.fonts[self.current_font_index]
        self.frame_positions = {frame: frame.place_info() for frame in self.frames}
        self.current_frame_index = 0
        self.all_frames_hidden = False
        self.cap = cv2.VideoCapture(0)

    def update_camera(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Greška u čitanju frame-a sa kamere.")
            return

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = img.resize((self.app.winfo_width(), self.app.winfo_height()))
        imgtk = ImageTk.PhotoImage(image=img)

        self.app.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
        self.imgtk = imgtk

        self.app.after(10, self.update_camera)

    def update_weather(self):
        weather_info = weather.get_local_weather()
        self.app.weather_label.config(text=weather_info)
        self.app.after(600000, self.update_weather)

    def update_time(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.app.time_label.config(text=current_time)
        self.app.after(1000, self.update_time)

    def update_traffic(self):
        traffic_info = traffic.get_traffic_status()
        self.app.traffic_text.delete("1.0", tk.END)
        self.app.traffic_text.insert(tk.END, traffic_info)
        self.app.after(600000, self.update_traffic)

    def update_news(self):
        news_info = news.get_news()
        self.app.news_text.delete("1.0", tk.END)
        self.app.news_text.insert(tk.END, news_info)
        self.app.after(600000, self.update_news)

    def toggle_frame_visibility(self):
        if self.all_frames_hidden:
            # Show frames one by one
            frame = self.frames[self.current_frame_index]
            frame_position = self.frame_positions[frame]
            frame.place(relx=frame_position["relx"], rely=frame_position["rely"])
            self.current_frame_index += 1
            if self.current_frame_index >= len(self.frames):
                self.current_frame_index = 0
                self.all_frames_hidden = False
        else:
            # Hide frames one by one
            frame = self.frames[self.current_frame_index]
            frame.place_forget()
            self.current_frame_index += 1
            if self.current_frame_index >= len(self.frames):
                self.current_frame_index = 0
                self.all_frames_hidden = True

    def change_font(self):
        self.current_font_index = (self.current_font_index + 1) % len(self.fonts)
        self.font = self.fonts[self.current_font_index]
        self.update_fonts()

    def update_fonts(self):
        self.app.time_label.config(font=("Helvetica", self.font))
        self.app.weather_label.config(font=("Helvetica", self.font))
        self.app.traffic_text.config(font=("Helvetica", self.font))
        self.app.news_text.config(font=("Helvetica", self.font))
