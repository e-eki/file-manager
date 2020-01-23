from tkinter import *
import os
from utils.baseUtils import showMessage
from blocks.directoryContent import DirectoryContent

# Элементы управления текущей директорией
class CurrentDirectory:
	def __init__(self, root, defaultCurrentDirStr = os.getcwd()):
		self.root = root
		self.defaultCurrentDirStr = defaultCurrentDirStr
		self.lastCurrentDirStr = defaultCurrentDirStr
		self.currentDir = StringVar()
		self.currentDir.set(defaultCurrentDirStr)

		# инициализация элементов управления содержимым текущей директории
		self.directoryContent = DirectoryContent(root, defaultCurrentDirStr)

	# Обработка клика по кнопке "Go!" - обновление текущей директории на указанную в поле ввода
	def clickChangeDirButton(self):
		currentDirStr = self.currentDir.get()

		if (self.lastCurrentDirStr != currentDirStr):
			self.lastCurrentDirStr = currentDirStr

			self.directoryContent.updateCurrentDirStr(currentDirStr)

	# Обработка клика по кнопке "Up" - обновление текущей директории на ту, что уровнем выше (если есть)
	def clickGoUpDirButton(self):
		currentDirStr = self.currentDir.get()
		dirname, fname = os.path.split(currentDirStr)
		
		if (os.path.exists(dirname)):
			self.currentDir.set(dirname)
			self.lastCurrentDirStr = dirname

			self.directoryContent.updateCurrentDirStr(dirname)

	# Обработка клика по кнопке "Reset to default directory" - сброс текущей директории к начальному значению
	def clickResetDirButton(self):
		self.lastCurrentDirStr = self.defaultCurrentDirStr
		self.currentDir.set(self.defaultCurrentDirStr)

		self.directoryContent.updateCurrentDirStr(self.defaultCurrentDirStr)
	
	# Вывод на экран элементов управления текущей директорией
	def display(self):
		currentDirLabel = Label(text="Current directory:")
		currentDirLabel.place(relx=0.1, rely=0.05)
 
		currentDirEntry = Entry(textvariable=self.currentDir, bg='DarkGreen', fg='white')
		currentDirEntry.place(relwidth=0.75, relx=0.1, rely=0.15)

		changeDirButton = Button(text="Go!", command=self.clickChangeDirButton)
		changeDirButton.place(relx=0.9, rely=0.18, anchor="c")

		goUpDirButton = Button(text="Up", command=self.clickGoUpDirButton)
		goUpDirButton.place(relx=0.05, rely=0.18, anchor="c")

		resetDirButton = Button(text="Reset to default directory", command=self.clickResetDirButton)
		resetDirButton.place(relx=0.5, rely=0.27, anchor="c")

		self.directoryContent.display()

	
