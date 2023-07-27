import tkinter as tk
import backendProcesses
import entryWithPlaceholder

class WorkspaceCheckerGUI:

    def __init__(self):

        #Defines the root, i.e. the window that opens when code is run
        self.root = tk.Tk()
        self.root.geometry("500x300")

        self.franchiseeSelectionInput = entryWithPlaceholder.EntryWithPlaceholder(self.root, "Start typing...")
        self.franchiseeSelectionInput.pack(pady=20)

        #Adds button to the window
        self.btn = tk.Button(self.root, text="Click me", font=('Arial', 16), command=self.fetch_info)
        self.btn.pack(padx=10, pady=10)

        #Tells the root window to render
        self.root.mainloop()
    
    #Adds functionality to the button to retrieve and display the title of a hard-coded Podio item
    def fetch_info(self):
        app_names_str = '\n'.join(app['name'] for app in backendProcesses.templateAppList)
        self.displyItemInfo = tk.Label(self.root, text=f'Apps: {app_names_str}', font=('Arial', 16))
        self.displyItemInfo.pack(padx=10, pady=10)