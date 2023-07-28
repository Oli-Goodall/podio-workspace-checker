import tkinter as tk
import backendProcesses
import entryWithPlaceholder

class WorkspaceCheckerGUI:

    def __init__(self):

        #Defines the root, i.e. the window that opens when code is run
        self.root = tk.Tk()
        self.root.geometry("500x300")

        self.listboxFrame = tk.Frame(self.root)
        self.listboxScrollbar = tk.Scrollbar(self.listboxFrame, orient=tk.VERTICAL)
        self.franchiseeListBox = tk.Listbox(self.listboxFrame, width=20, height=10, yscrollcommand=self.listboxScrollbar.set)

        
        self.listboxScrollbar.config(command=self.franchiseeListBox.yview)
        self.listboxScrollbar.config(command=self.franchiseeListBox.yview)

        
        #Hide listbox initially
        self.franchiseeListBox.pack_forget()
        self.listboxScrollbar.pack_forget()

        #Update the listbox
        def update(data):
            self.franchiseeListBox.delete(0, tk.END)
            for item in data:
                self.franchiseeListBox.insert(tk.END, item)
        
        #Puts selected item into input field
        def fillout(e):
            self.franchiseeSelectionInput.delete(0, tk.END)
            self.franchiseeSelectionInput.insert(0, self.franchiseeListBox.get(tk.ANCHOR))

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
            # Show the listbox only when there are matching results and the input field has focus
            if data and self.franchiseeSelectionInput.focus_get() == self.franchiseeSelectionInput:
                self.listboxFrame.pack()
                self.franchiseeListBox.pack(side=tk.LEFT)
                self.listboxScrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            else:
                self.franchiseeListBox.pack_forget()
                self.listboxScrollbar.pack_forget()           

        #Displays an input field with placeholder
        self.franchiseeSelectionInput = entryWithPlaceholder.EntryWithPlaceholder(self.root, "Start typing location...")
        self.franchiseeSelectionInput.pack()

        #Retrieve list of franchisee space names from Podio
        franchiseSpaceNames = [space['name'].split('Accountants', 1)[-1].strip() for space in backendProcesses.franchiseeWorkspacesList]

        #Add franchisee space names to listbox
        update(franchiseSpaceNames)

        #Create a binding on the listbox onclick
        self.franchiseeListBox.bind("<<ListboxSelect>>", fillout)

        #Create a binding on the input field
        self.franchiseeSelectionInput.bind("<KeyRelease>", check)
        
        #Tells the root window to render
        self.root.mainloop()
    
