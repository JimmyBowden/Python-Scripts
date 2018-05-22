import tkinter as tk 
from tkinter import ttk
from tkinter import filedialog as fd

from tabula import read_pdf

LARGE_FONT = ("Verdana", 12)

def file_select():
	global file_selection
	file_selection = fd.askopenfilename(title="Select a PDF", filetypes=(("pdf files", "*.pdf"),("Not tested for Mac", "*.pdf")))

def dir_select():
	global dir_selection
	dir_selection = fd.asksaveasfilename(title="Pick a directory and name your XLSX file.", filetypes=(("excel files" ,"*.xlsx"), ("not tested for Mac", "*.xlsx")))
	
def pdf_xlsx(path, name):
	df = read_pdf(path, encoding="cp1252", pages="all")
	df.to_excel(name)

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
		
		label1 = tk.Label(self, text="1. Choose a PDF.", font=LARGE_FONT)
		button1 = ttk.Button(self, text="Browse", command=lambda: file_select())
		
		label2 = tk.Label(self, text="2. Choose a directory and filename for your new file.", font=LARGE_FONT)
		button2 = ttk.Button(self, text="Browse", command=lambda: dir_select())
		
		label3 = tk.Label(self, text="3. Generate your file.", font=LARGE_FONT)
		button3 = ttk.Button(self, text="Generate", command=lambda: pdf_xlsx(file_selection, dir_selection))
		
		label1.grid(row=0, column=0)
		button1.grid(row=0, column=1)
		
		label2.grid(row=1, column=0)
		button2.grid(row=1, column=1)
		
		label3.grid(row=2, column=0)
		button3.grid(row=2, column=1)
		
if __name__ == "__main__":
	root = MainApp()
	root.mainloop()