'''
Created by Chris Clunie for SilverCloud inc

To use you must pip install docx2txt  
'''
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox

import docx2txt

LARGE_FONT = ("Verdana", 12)

def file_select():
	global file_selection
	file_selection = fd.askopenfilename(title="Select a PDF", filetypes=(("docx files", "*.docx"),("Not tested for Mac", "*.docx")))

def dir_select():
	global dir_selection
	dir_selection = fd.askdirectory(title="Pick a directory")

def scrape_images(path, folder):
	docx2txt.process(path, folder)
	messagebox.showinfo("Task Completed", "Images have been placed in the folder you selected.")

class MainApp(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		#tk.Tk.iconbitmap(self, default="")    <---Add later
		tk.Tk.wm_title(self, "PDF to XLSX")
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand = True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		#for F in (MainPage, FuturePages):    <--Add later

		frame = MainPage(container, self)

		self.frames[MainPage] = frame

		frame.grid(row=0, column=0, stick="nsew")

		self.show_frame(MainPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

class MainPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label1 = tk.Label(self, text="1. Choose a DOCX.", font=LARGE_FONT)
		button1 = ttk.Button(self, text="Browse", command=lambda: file_select())

		label2 = tk.Label(self, text="2. Choose a directory for your files.", font=LARGE_FONT)
		button2 = ttk.Button(self, text="Browse", command=lambda: dir_select())

		label3 = tk.Label(self, text="3. Scrape images.", font=LARGE_FONT)
		button3 = ttk.Button(self, text="Generate", command=lambda: scrape_images(file_selection, dir_selection))

		label1.grid(row=0, column=0)
		button1.grid(row=0, column=1)

		label2.grid(row=1, column=0)
		button2.grid(row=1, column=1)

		label3.grid(row=2, column=0)
		button3.grid(row=2, column=1)

if __name__ == "__main__":
	root = MainApp()
	root.mainloop()
