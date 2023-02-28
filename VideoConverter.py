import tkinter as tk
from tkinter import filedialog
import moviepy.editor as mp

class VideoConverter:
    def __init__(self, master):
        self.master = master
        master.title("Video Converter")

        self.canvas = tk.Canvas(master, width=300, height=250)
        self.canvas.pack()

        self.input_label = tk.Label(master, text="Select input file:")
        self.input_label.pack()

        self.input_text = tk.Entry(master)
        self.input_text.pack()

        self.input_button = tk.Button(master, text="Browse", command=self.browse_input)
        self.input_button.pack()

        self.format_label = tk.Label(master, text="Select output format:")
        self.format_label.pack()

        self.format_list = ["mp4", "mov", "avi"]
        self.format_var = tk.StringVar(master)
        self.format_var.set(self.format_list[0])
        self.format_dropdown = tk.OptionMenu(master, self.format_var, *self.format_list)
        self.format_dropdown.pack()

        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.pack()

    def browse_input(self):
        input_file = filedialog.askopenfilename()
        self.input_text.delete(0, tk.END)
        self.input_text.insert(0, input_file)

    def convert(self):
        input_file = self.input_text.get()
        output_format = self.format_var.get()
        output_file = filedialog.asksaveasfilename(defaultextension=f".{output_format}")

        video = mp.VideoFileClip(input_file)
        video.write_videofile(output_file)

root = tk.Tk()
my_converter = VideoConverter(root)
root.mainloop()
