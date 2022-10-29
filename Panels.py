from tkinter import Frame, Tk
from tkinter import filedialog as fd
from ConfigFile import ConfigFile

from Settings import SETTINGS
from Widgets import Button, Details, Heading, Text

class Window(Tk):
	padding = 10
	inset = 150
	def __init__(self, title: str):
		super().__init__()
		self.title(title)
		width = self.winfo_screenwidth()
		height = self.winfo_screenheight()
		# in case the OS doesn't support zoomed window
		self.geometry(f"{width-Window.inset*2}x{height-Window.inset*2}+{Window.inset}+{Window.inset//2}")
		self.wm_state("zoomed")
		self.protocol('WM_DELETE_WINDOW', self.on_exit)

	def on_exit(self):
		SETTINGS.save_to("settings.json")
		self.destroy()
		exit(0)

class Controls(Frame):
	"""The control panel for the program to the left of the output window"""
	def __init__(self, master: Tk):
		super().__init__(master, bg=SETTINGS.theme.bg_0, width=200)
		Heading(self, text="AUTOMATIC MARKER").pack(anchor="n", pady=Window.padding)

		self.pack(side="left", fill="both", expand=True)

class InitialConfig(Frame):
	def __init__(self, master: Tk | Frame):
		super().__init__(master, bg=SETTINGS.theme.bg_0)
		Heading(self, "CONFIGURATION FILE", 2).pack(anchor="n", pady=Window.padding)

		Text(self, f"Choose a configuration file to specify the files to compile and check and the inputs & expected outputs. If you run this script in a directory containing a file called {SETTINGS.default.config_file} it will be loaded automatically.").pack(anchor="n")

		Button(self, text="CHOOSE", command=self.choose_config).pack(anchor="n", pady=Window.padding)


		# d = Details(self, "CONFIGURATION FILE", self, level=2, open=True)
		# d.pack(anchor="n", fill="x", pady=Window.padding)
		# d.set_body(Frame(d))
		# Text(d.body, "Current configuration file:").pack(anchor="n")
		# Button(d.body, text="CHOOSE", command=self.choose_different_config).pack(anchor="n", pady=Window.padding)



	def choose_config(self):
		# open a tkinter file dialog asking for a json file
		file_path = fd.askopenfilename(initialdir="./", title="Select Automarker configuration file",filetypes=(("json files","*.json"),("all files","*.*")))
		file = ConfigFile(file_path)
		print(file.error)
		# hide options and show AM options if valid

	def choose_different_config(self):
		self.choose_config()