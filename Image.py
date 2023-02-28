import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import Image


class ImageRecognitionApp:
	def __init__ (self, master):
		self.master = master
		master.title ("Image Recognition App")

		# Create buttons
		self.browse_button = tk.Button (master, text = "Browse", command = self.browse_file)
		self.recognize_button = tk.Button (master, text = "Recognize", command = self.recognize_image())

		# Create label to display selected image
		self.image_label = tk.Label (master)
		self.image_label.pack ()

		# Gets the file path
		self.file_path = tk.filedialog.askopenfilename()

		# Position buttons
		self.browse_button.pack ()
		self.recognize_button.pack ()

		# Load Haar Cascade classifier for face detection
		self.face_cascade = cv2.CascadeClassifier ("haarcascade_frontalface_default.xml")

		# Initialize selected file path and recognized face count
		self.file_path = ""
		self.face_count = 0

	def browse_file (self):
		# Open file dialog to select image file
		self.file_path = filedialog.askopenfilename ()

		# Load image from file and display it in label
		img = cv2.imread (self.file_path)
		img = cv2.cvtColor (img, cv2.COLOR_BGR2RGB)
		img = cv2.resize (img, (300, 300))
		img = np.rot90 (img)
		img = np.flipud (img)
		img_bytes = cv2.imencode ('.png', img) [1].tobytes ()
		img = tk.PhotoImage (data = img_bytes)
		self.image_label.configure (image = img)
		self.image_label.image = img

		# Reset face count
		self.face_count = 0

	def recognize_image (self):
		if self.file_path:
			# Load image from file
			img = cv2.imread (self.file_path)

			# Convert to grayscale for face detection
			gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)

			# Detect faces in image using Haar Cascade classifier
			faces = self.face_cascade.detectMultiScale (gray, 1.1, 4)

			# Draw rectangles around detected faces
			for (x, y, w, h) in faces:
				cv2.rectangle (img, (x, y), (x + w, y + h), (0, 255, 0), 2)

			# Display image with detected faces
			cv2.imshow ("Image", img)
			cv2.waitKey (0)

			# Count number of detected faces
			self.face_count = len (faces)

		# Display number of detected faces in message box
		message = f"Detected {self.face_count} face(s) in image."
		tk.messagebox.showinfo ("Result", message)

	# def recognize_image (self, img):
	# 	gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
	# 	faces = self.face_cascade.detectMultiScale (gray, 1.1, 4)
	# 	if len (faces) == 0:
	# 		print ("No faces detected")
	# 	else:
	# 		for (x, y, w, h) in faces:
	# 			cv2.rectangle (img, (x, y), (x + w, y + h), (0, 255, 0), 2)
	# 		img = cv2.cvtColor (img, cv2.COLOR_BGR2RGB)
	# 		img = Image.fromarray (img)
	# 		img = Image.PhotoImage (img)
	# 		self.panel2.configure (image = img)
	# 		self.panel2.image = img


root = tk.Tk ()
app = ImageRecognitionApp(root)
root.mainloop ()
