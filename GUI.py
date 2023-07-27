import tkinter as tk
import backendProcesses
import entryWithPlaceholder

class WorkspaceCheckerGUI:

    def __init__(self):

        #Update the listbox
        def update(data):
            self.franchiseeListBox.delete(0, tk.END)
            for item in data:
                self.franchiseeListBox.insert(tk.END, item)
        
        #Puts selected item into input field
        def fillout(e):
            self.franchiseeSelectionInput.delete(0, tk.END)
            self.franchiseeSelectionInput.insert(0, self.franchiseeListBox.get(tk.ACTIVE))

        #Shows only results that contain the string in the input field
        def check(e):
            typed = self.franchiseeSelectionInput.get()

            if typed == '':
                data = franchiseSpaceNames
            else:
                data = []
                for item in franchiseSpaceNames:
                    if typed.lower() in item.lower():
                        data.append(item)
            
            update(data)

        #Defines the root, i.e. the window that opens when code is run
        self.root = tk.Tk()
        self.root.geometry("500x300")

        #Displays an input field with placeholder
        self.franchiseeSelectionInput = entryWithPlaceholder.EntryWithPlaceholder(self.root, "Start typing location...")
        self.franchiseeSelectionInput.pack()

        #Displays listbox populated with franchisee workspaces
        self.franchiseeListBox = tk.Listbox(self.root)
        self.franchiseeListBox.pack()

        #Retireve list of franchisee space names from Podio
        franchiseSpaceNames = list(space['name'] for space in backendProcesses.franchiseeWorkspacesList)

        #Add franchisee space names to listbox
        update(franchiseSpaceNames)

        #Create a binding on the listbox onclick
        self.franchiseeListBox.bind("<<ListboxSelect>>", fillout)

        #Create a binding on the input field
        self.franchiseeSelectionInput.bind("<KeyRelease>", check)

        #Tells the root window to render
        self.root.mainloop()
    
