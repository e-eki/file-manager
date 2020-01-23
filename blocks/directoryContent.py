from tkinter import *
import os
from utils.baseUtils import showMessage

# Элементы управления содержимым текущей директории
class DirectoryContent:
	def __init__(self, root, currentDirStr = os.getcwd()):
		self.root = root
		self.currentDirStr = currentDirStr
		# название добавляемой папки
		self.newItemName = StringVar()
		# список содержимого текущей директории
		self.listContentDir = []

		scrollbar = Scrollbar(root)
		scrollbar.pack(side=RIGHT, fill=Y)
		self.contentListbox = Listbox(yscrollcommand=scrollbar.set, bg='YellowGreen')
		scrollbar.config(command=self.contentListbox.yview)

	# обновить значение текущей директории
	def updateCurrentDirStr(self, currentDirStr):
		self.currentDirStr = currentDirStr
		self.resetInnerContent()

		if (os.path.exists(self.currentDirStr)):
			self.getInnerContent()
		else:
			showMessage('Specified directory does not exist')

	# сброс списка содержимого
	def resetInnerContent(self):
		length = self.contentListbox.size()
		self.contentListbox.delete(0, length-1)

	# получить список содержимого
	def getInnerContent(self):
		dirNames = os.listdir(self.currentDirStr)
		self.listContentDir = []

		for dirName in dirNames:
			dirPath = os.path.join(self.currentDirStr, dirName)

			dirType = 'Directory'
			if (os.path.isfile(dirPath)):
				dirType = 'File'

			dir = (dirName, dirType)
			self.listContentDir.append(dir)

		for dir in self.listContentDir:
			name, type = dir
			itemName = "{} ({})".format(name,type)
			self.contentListbox.insert(END, itemName)

	# Обработка клика по кнопке "Add" - добавление новой папки
	def clickAddItemButton(self):
		if (not os.path.exists(self.currentDirStr)):
			showMessage('Specified directory does not exist.You cannot add an item here.')
		elif (len(self.newItemName.get()) == 0):
			showMessage('Empty name for new directory.')
		else:
			newItemPath = os.path.join(self.currentDirStr, self.newItemName.get())

			if os.path.exists(newItemPath):
				showMessage('Specified file exists') 
			else:	
				try:
					os.mkdir(newItemPath)
					self.resetInnerContent()
					self.getInnerContent()
				except Exception as e:
					showMessage('Something crashed: {}'.format(e))

	# Обработка клика по кнопке "Delete" - удаление папки или файла
	def clickDeleteItemButton(self):
		selection = self.contentListbox.curselection()
		itemName, itemType = self.listContentDir[selection[0]]
		itemPath = os.path.join(self.currentDirStr, itemName)

		try:
			if (itemType == 'Directory'):
				os.rmdir(itemPath)
			elif (itemType == 'File'):
				os.remove(itemPath)

			self.resetInnerContent()
			self.getInnerContent()
		except Exception as e:
			showMessage('Something crashed: {}'.format(e))

	# Вывод на экран элементов управления содержимым текущей директории
	def display(self):
		self.getInnerContent()

		contentLabel = Label(text="Inner content:")
		contentLabel.place(relx=0.05, rely=0.35)

		newItemEntry = Entry(textvariable=self.newItemName, bg='YellowGreen')
		newItemEntry.place(relwidth=0.8, relx=0.05, rely=0.4)

		addItemButton = Button(text="Add", command=self.clickAddItemButton)
		addItemButton.place(relx=0.9, rely=0.42, anchor="c")

		# scrollbar = Scrollbar(self.contentListbox)
		# scrollbar.pack(side=RIGHT, fill=Y)

		# self.contentListbox = Listbox(yscrollcommand=scrollbar.set, bg='YellowGreen')
		self.contentListbox.place(relx=0.05, rely=0.47, relwidth=0.9)
		# scrollbar.config(command=self.contentListbox.yview)

		deleteItemButton = Button(text="Delete", command=self.clickDeleteItemButton)
		deleteItemButton.place(relx=0.88, rely=0.93, anchor="c") 


