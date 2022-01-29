import tkinter as tk
from voicesearchpackage import VoiceSearch

def startVoiceSearch(windowHandle):
    windowHandle.withdraw()
    voiceObj = VoiceSearch.VoiceSearch()
    voiceObj.voiceSearch()
    windowHandle.deiconify()    
    
mainWindow = tk.Tk()
mainWindow.resizable(0,0)
mainWindow.title('Voice Search')
mainWindow.geometry('200x200')
startButton = tk.Button(mainWindow,text = "Start Conversation", width = 15, height = 5,command = lambda: startVoiceSearch(mainWindow))

startButton.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)

mainWindow.mainloop()