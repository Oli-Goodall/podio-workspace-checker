import tkinter as tk
from backendProcesses import c

class WorkspaceCheckerGUI:

    def __init__(self):

        #Defines the root, i.e. the window that opens when code is run
        self.root = tk.Tk()

        #Adds button to the window
        self.btn = tk.Button(self.root, text="Click me", font=('Arial', 16), command=self.fetch_info)
        self.btn.pack(padx=10, pady=10)

        #Tells the root window to render
        self.root.mainloop()
    
    #Adds functionality to the button to retrieve and display the title of a hard-coded Podio item
    def fetch_info(self):
        self.itemInfo = c.Item.find(2542371339)
        self.displyItemInfo = tk.Label(self.root, text=f'Item name: {self.itemInfo["fields"][0]["values"][0]["value"]}', font=('Arial', 16))
        self.displyItemInfo.pack(padx=10, pady=10)